'''
Created on 25/10/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QModelIndex, QStandardItemModel, QStandardItem
import rscForm
import mixedModel
import Rules
import re
import FuncSQL
import QT_msg
class GenericReferencias(QDialog):
    
    
    def justView(self):
        '''
        Metodo para configurar o form para so vizualizar
        '''
        lstWdg = self.dictFields['lstWidget']
        if self.level is not None:
            if int(self.level) <= 10:
                rscForm.setReadOnlyAll(True, lstWdg)
                rscForm.setReadOnly(True, self.PBGuardar)
                
                          
                          
    '''
    Class Generica das tabelas de referencia, onde iremos criar 
    os metodos para levar, inicializar etc.. os dados nos widgets
    sem termos que repetir para cada nova janela que for Criada.
    
    '''
    
    def toEdit(self):
        '''
        Metodo to edit, este e o metodo usado para editar os Dados,
        verificando se foi passado o modelIndex Do elemento na tabela 
        selecionada.
        Se for passamos o widget e model para ele atribuir os dados a 
        cada widget.
        '''
        if isinstance(self.mIdx, QModelIndex):
            indexModel = self.mIdx
            lstwidgt = self.dictFields['lstWidget']
            rscForm.setClicked2Widget(indexModel, lstwidgt)
        
    
    def getValues(self):
        '''
        Metodo para levar os valores Que se encontram nos widgets proceder para insercao
        ou atulizacao de dados.
        Levando a lista de widgets existentes, depois Colocando no Default o que precisa ficar
        em default, depois verifica se o widget e combox caso seja vamos levar o id inves do CurrentText
        caso nao seja combox levamos o texto dentro do widget.
        '''
        lstWidgt= self.dictFields['lstWidget']
        lstRel= self.dictFields['lstRel']
        lstOut= []
        bOK= self._verfVals()
        if bOK:
            for idx, val in enumerate(lstWidgt):
                if lstRel[idx]:
                    lstOut.append(mixedModel.getDataCombox(widg= val))
                else:
                    lstOut.append(rscForm.getText(widg= val))
        return bOK, lstOut

        
    def setModelInCombox(self):
        for idx, val in enumerate (self.dictSql['lstRelTblMain']):
            tblName= val
            lstNames= self.dictSql['lstRelName'][idx]
            widg= self.dictSql['lstRelWidg'][idx]
            condName= self.dictSql['lstCond'][idx]
            condVal= self.dictSql['lstCondVal'][idx]
            condQuot= self.dictSql['lstToQuote'][idx]
            mixedModel.setModel4CombBox(tblName=tblName, lstNames=lstNames, widg=widg, condName=condName, condVal=condVal, condQuot=condQuot)
    
    
    def configCombox(self):
        '''
        Metodo para configurar o Modelo e Text Hint no Combox.
        '''
        lstWdgt = self.dictCB['widget']
        lstQuer = self.dictCB['quer']
        for idx, val in enumerate (lstWdgt):
            model = mixedModel.setQueryModel(lstQuer[idx])
            val.setModel(model)
            val.setModelColumn(1)
            self.CBTextHint(Combox=val)
    
    def CBTextHint(self, Combox=None):
        mdel = QStandardItemModel(Combox.model())
        firstIndex = mdel.index(0, Combox.modelColumn(), Combox.rootModelIndex())
        firstItem = QStandardItem(mdel.itemFromIndex(firstIndex))
        firstItem.setSelectable(False)
        
        
    def _verfVals(self):
        wdgt = self.dictFields['lstWidget']
        toDefault = self.dictFields['lstDefault']
        toUpercase = self.dictFields['lstUpercase']
        for idx, val in enumerate(wdgt):
            if toDefault[idx]:
                Rules.setNull(wdgt=val)
            if toUpercase[idx]:
                Rules.setUPPER(wdgt=val)
            if toDefault[idx] is False:
                bOK = Rules.notNull(wdgt=val)
                if bOK is False:
                    break
        return bOK
    
    
    def pre_operacao(self):
        try:
            tblName= self.tblName
            lstName= self.dictFields['lstName']
            lstQuot= self.dictFields['lstToQuote']
            if self.mIdx is not None:
                cond = self.dictFields['lstName'][0]
                getId= lambda mIdx: mIdx.model().record(mIdx.row()).value(0)
                conVal = getId(self.mIdx)
                condQuot = self.dictFields['lstToQuote'][0]
            else:
                cond = None
                conVal = None
                condQuot = None
            bOK, lstVal = self.getValues()
        except:
            bOK = False
        if bOK:
            self._operacao(tblName= tblName, lstNames= lstName, lstVals= lstVal, lstQuot =lstQuot, cond=cond, conVal=conVal, condQuot=condQuot)
        else:
            lstNotNull=self.dictFields['lstDefault']
            for idx, val in enumerate(self.dictFields['lstWidget']):
                if lstNotNull[idx] is False:
                    self._warning(widgt=val)
            QT_msg.aviso(txt="PorFavor reveja os dados que esta para ser inseridos e certifique-se que os campos Amarelos estao todos preenchidos e nao Estao repetidos")
    
    
    def _operacao(self, tblName= None, lstNames= None, lstVals= None, lstQuot= None, cond= None, conVal= None, condQuot= None):
        if (cond is None) or (conVal is None) or (condQuot is None):
            bOK, msgOut = FuncSQL.insertVal(tblName= tblName, lstNames= lstNames, lstVal= lstVals, lstQuot= lstQuot)
        else:
            bOK, msgOut= FuncSQL.updateVal(tblName= tblName, lstNames = lstNames, lstVals = lstVals, lstQuot = lstQuot, cond=cond, conVal=conVal, condQuot=condQuot)
        if bOK:
            self.bOK= (True, msgOut)
            self.mIdx= None
            self.close()
        else:
            self.bOK= (False, None)
            
    
    def _warning(self, widgt=None):
        color = rscForm.warningFocus(obj=widgt)
        widgt.setStyleSheet(color)
        
            
class GenericReferencias_ (GenericReferencias):   


    def splitInID(self):
        txt = self.LECodigo.text()
        tstRegex = re.compile(r'\w{,3}')
        mo = tstRegex.findall(txt)
        if len(mo) >= 2:
            id_codigo = mo[0]
            Id= mo[1]
            self.LBid.setText(str(id_codigo))
            self.LECodigo.setText(Id)


    def specialID(self):
        id_grupo = self.LBid.text()
        Id = self.LECodigo.text()
        newID = id_grupo+Id    
        newID = newID.upper()
        return (newID)


    def getValues(self):
        lstWidgt = self.dictFields['lstWidget']
        lstOut = []
        bOK = self._verfVals()
        Id = self.specialID()
        if bOK:
            for idx, val in enumerate(self.dictFields['lstRel']):
                if idx is 0:
                    lstOut.append(Id)  
                else:
                    if val:
                        lstOut.append(mixedModel.getDataCombox(lstWidgt[idx]))
                    else:
                        lstOut.append(rscForm.getText(lstWidgt[idx]))
        return bOK, lstOut


    def setIDFromCB(self, widget=None):
        Id = mixedModel.getDataCombox(widg=widget)
        self.LBid.setText(str(Id))