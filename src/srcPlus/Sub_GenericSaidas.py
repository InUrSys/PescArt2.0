'''
Created on 27/11/2017

@author: chernomirdinmacuvele
'''
import mixedModel
from GenericAmostrasQDialog import CustomFrm
import rscForm
import FuncSQL
import QT_msg
import QT_tblViewUtility
import dialog_PesquisarSaidas
from frmTabFicha_II_III import frmTabFicha
class Generic_Saidas(CustomFrm):
     
    def verfActiv_Pesqueira(self):
        '''
        Metodo para verificar se houve activade pesqueira e desabilitar ou habilitar os Campos.
        '''
        lstWidget = self.lstActividade
        lstExcept= [True, True]
        if self.CHBActividade.isChecked():
            self.AllWdgOffExceptOne(state=False, lstWdg= lstWidget, lstExcpt= lstExcept)
        else:   
            self.AllWdgOffExceptOne(state=True, lstWdg= lstWidget, lstExcpt= lstExcept)
            lstWdg = [self.SBActivas, self.SBAmostras, self.SBNaoActivas, self.SBOutrosCentros]
            for val in lstWdg:
                rscForm.setTxtToWidget(widget= val, val= -1)
                
        
            
            
    def fieldsToDefault(self):
        '''
        Metodo para colocar os campos no default apois o botao add ser Clickado
        '''
        if self.PBAdicionar.isChecked():
            lstWdg = self.dictFields['fldWidget']
            for val in lstWdg:
                rscForm.setToDefault(wdgt=val)
            self.verfActiv_Pesqueira() #Coloca os SpinBox dentro da Actividade Pesquira off
            
     
    def set_IdSaida(self):
        ''' Metodo para atribuir o proximo ID a ser inserido'''
        next1 = self.getNextSaida()
        self.LEN_Sequencial.setText(str(next1))
    
    
    def getNextSaida(self):
        ''' Metodo para apanhar o ultimo na base de dados '''
        nextSeq = -99
        bOK, numeroSeq = FuncSQL.getLast(tblName= self.dictTblName['Saidas'], val= "id", ordBy= "id")
        if bOK:
            nextSeq = int(numeroSeq) + 1
        return nextSeq
    
    
    def prep_toAdd(self):
        if self.PBAdicionar.isChecked():
            self.PBEditar.setChecked(False)
            self.fieldsToDefault()
            self.set_IdSaida()
            self.verf_activArteTipo()
            self.lstTemVal = None
            self._afterPop()
        else:
            self.LEN_Sequencial.setText(str('-99'))
    
    
    def prep_toEdit(self):
        if self.PBEditar.isChecked():
            if self.LEN_Sequencial.text() == '-99':
                QT_msg.aviso(txt= "Aviso se pretende editar certifique que Tem alguem elemento para edita.")
                self.PBEditar.setChecked(False)
            else:
                numeroSeq = self.getNextSaida()
                if self.LEN_Sequencial.text() == str(numeroSeq):
                    QT_msg.aviso(txt= "Aviso se pretende editar certifique que Tem alguem elemento para edita.")
                    self.PBEditar.setChecked(False)
                else:
                    self.PBAdicionar.setChecked(False)
                    self.setValToAllWdg()
                    self._afterPop()
            
    
    def setValToAllWdg(self):
        if self.lstTemVal is not None:
            wdg = self.dictFields['fldWidget']
            self.setLocalizacao(nome= self.lstTemVal[2])
            for idx, val in enumerate(self.lstTemVal):
                rscForm.setTxtToWidget(widget= wdg[idx], val=val)
            
            
    
    def save(self):
        bOK=False
        R_bOK = self.formValid()
        if R_bOK:
            try:
                if self.PBAdicionar.isChecked():
                    bOK, msgOut = self.insert()
                elif self.PBEditar.isChecked():
                    bOK, msgOut = self.editar()
                if bOK:
                    self.showMsg(obj=self.LBwhois, msgAlert=msgOut)
                    self.lstTemVal = None
                    self.afterOperation()      
            except Exception:
                QT_msg.error(txt='Error Operacao nao realizada', verbTxt=str(Exception))
    
        
    def afterOperation(self):
        self.unPressButton()
        self.tempValues()
        self.verf_activArteTipo()
        self._afterPop()
        
        
    def tempValues(self):
        self.setDefault()
        lstWidg = self.dictFields['fldWidget']
        self.lstTemVal = rscForm.getTextAll(lstWidg)
    
    
    def insert(self):
        '''
        salvar
        ''' 
        lstVal = self.getValues()
        lstNames = self.dictFields['fldName']
        lstQuot = self.dictFields['fldToQuote']
        bOK, msgOut = FuncSQL.insertVal(tblName=self.dictTblName['Saidas'], lstNames=lstNames, lstVal=lstVal, lstQuot=lstQuot)
        return bOK, msgOut
    
        
    def editar(self):
        '''
        Editar
        ''' 
        cond='id'
        Valcond=self.LEN_Sequencial.text()
        Typcond=False
        lstVal = self.getValues()
        lstNames = self.dictFields['fldName']
        lstQuot = self.dictFields['fldToQuote']
        bOK, msgOut = FuncSQL.updateVal(tblName=self.dictTblName['Saidas'], lstNames=lstNames, lstVals=lstVal, 
                                    lstQuot=lstQuot, cond=cond, conVal=Valcond, condQuot=Typcond)
        return bOK, msgOut
        
        
    def unPressButton(self):
        lstWdg = [self.PBAdicionar, self.PBEditar]
        for val in lstWdg:
            val.setChecked(False) #Unpresses The button
        
             
    def setModelView(self):
        for idx, val in enumerate(self.dictView['filtro']):
            filtro = val.format(id = self.LEN_Sequencial.text())
            bOK, model = mixedModel.setViewModel(tblName= self.dictView['tblName'][idx], 
                                                filtro= filtro, 
                                                lstVal2Rel= self.dictView['MainDict'][idx]['val2Rel'] , 
                                                lstRelTblName= self.dictView['MainDict'][idx]['relTblName'] , 
                                                lstNewNames= self.dictView['MainDict'][idx]['newNames'])
                                                            
            if bOK:
                lstSizeCol= self.dictView['MainDict'][idx]['sizeCol']
                tblView= self.dictView['tblView'][idx]
                toHide= self.dictView['MainDict'][idx]['toHide']
                QT_tblViewUtility.setModelInView(tblView= tblView, ViewModel= model, toHide= toHide)
                QT_tblViewUtility.setViewCustom(tblView= tblView, lstSizeCol=lstSizeCol)
                
                
    def verf_activArteTipo(self):
        '''
        metodo Verifica se houve actividade pesqueria, para habilitar ou desabilitar o GB
        '''
        if self.PBAdicionar.isChecked() is False:
            self.GBArtes.setEnabled(True)
            self.GBSaidasObs.setEnabled(True)
        else:
            self.GBSaidasObs.setEnabled(False)
            self.GBArtes.setEnabled(False)
    
    
    def vef_saida(self):
        bOK, numeroSeq = FuncSQL.getLast(tblName= self.dictTblName['Saidas'], val= "id", ordBy= "id")
        return bOK, numeroSeq 
    
    
    def openSearch(self):
        run = dialog_PesquisarSaidas.PesquisarSaidas(self, dbcon=self.dbcon, tblName=self.dictTblName['Saidas'])
        run.exec_()          
        if run.close():
            lstVal = run.lstVal
            bOK = run.bOK
            if bOK:
                self.lstTemVal =  lstVal
                self.unPressButton()
                self.setValToAllWdg()
                self.verf_activArteTipo()
                self.setModelView()
    
    
    def getIdx(self):
        '''
        Metodo para extrair o index do widget Que manda o sinal. 
        '''     
        senderWidg = self.sender().objectName()
        bOK= False
        try:
            idx = self.dictMainWidg[senderWidg]
            bOK = True
        except KeyError:
            idx = None
        finally:
            return bOK, idx
    
    def disableAmostras(self, Bstate=True):
        self.PBAmostras.setDisabled(Bstate)
        

    def viewClicked(self, modIdx=None):
        '''
        '''
        bOK, idx = self.getIdx()
        if bOK:       
            if idx == 1 and modIdx is not None:
                self.ArtesMindex = modIdx #Model index usado para Abrir Amostras
                self.disableAmostras(Bstate=False) #Abilitar o botao Amostras
            self.getClicked(modIdx= modIdx, posNum= idx)
        
    
    def prep_toInseret_POP(self):
        bOK, idx = self.getIdx()
        if bOK:
            self.open_POP(idx=idx)
    
    
    def prep_toEdit_POP(self):
        bOK, idx = self.getIdx()
        if bOK:
            lstValToEdit = self.dictView['lastClicked'][idx]
            if lstValToEdit is not None:
                self.open_POP(idx=idx, ClickedlstVal=lstValToEdit)
            else:
                QT_msg.aviso(txt="Porfavor selecione um elemento para realizar a atualizacao.")
        
    
    def open_POP(self, idx=None, ClickedlstVal=None):
        try:
            tblName = self.dictView['tblName'][idx]
            Id =self.LEN_Sequencial.text()
            run = self.dictView['dialogsToOpen'][idx](TblName=tblName , dbcon=self.dbcon, Id=Id, lstValToEdit=ClickedlstVal, dictRules=self.dictRules)
            run.exec_()
            if run.close():
                bOK, msgIN = run.bOK
                if bOK:
                    self.showMsg(obj=self.LBwhois, msgAlert=msgIN)
                    self._afterPop()
        except Exception as ky:
            QT_msg.error(txt="O correu um erro inesperado a Operacao foi Cancelada.", verbTxt=str(ky))
        
            
    def _afterPop(self):
        self.setModelView()
        self.disableAmostras()
        self.dictView['lastClicked'] = [None, None]
            
            
    def getClicked(self, modIdx=None ,posNum=None):
        '''
        '''
        if modIdx is not None and  posNum is not None:
            totalCol = len(self.dictView['MainDict'][posNum]['names'])
            ClickedlstVal = rscForm.GetSelectedFromView(mIdx=modIdx, totalCol=totalCol)
            self.dictView['lastClicked'][posNum] = ClickedlstVal
        
        
    def open_Amostras(self):
        '''
        '''
        try:
            runAmostras = frmTabFicha(dbcon=self.dbcon, Id=self.LEN_Sequencial.text(), dictRules = self.dictRules, mIdxe=self.ArtesMindex)
            runAmostras.exec_()
            if runAmostras.close():
                self.setModelView()
                self.dictView['lastClicked'] = [None, None]
                self.disableAmostras()
                self.ArtesMindex =None
        except Exception as er:
            QT_msg.aviso(txt=str(er))
    
    
    def configRegistador(self):
        if self.CBProvincia.currentIndex() == 0:
            quer= "select null as id, '-Registador-' as nome union all select id, nome from ref_registador"
        else:
            id_prov = mixedModel.getDataCombox(widg= self.CBProvincia)
            quer = "select null as id, '-Registador-' as nome union all select id, nome from ref_registador where id_centro = '{prov}'".format(prov = id_prov)
        model = mixedModel.setQueryModel(query =quer)
        self.CBRegistadores.setModel(model)
        self.CBRegistadores.setModelColumn(1)   
                
                
                
        
        