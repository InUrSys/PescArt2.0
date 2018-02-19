'''
Created on 06/11/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QTimer
import QT_msg
import QT_tblViewUtility
import QT_widgetsCustom
from toViewKeepTrack import KeepTrack
from toView_keep_track_ArtesPesca import toView_Keep_track_ArtesPesca 
class GenericTabs(QDialog):
    
    def setHDWGH(self):#how do we got here
        wdg = toView_Keep_track_ArtesPesca(dbcon=self.dbcon, Id=self.mIdex)
        lastID, LastRow = wdg.getData()
        self.DictGridLay['ItemClicked'][0] = lastID, LastRow
        self.GLArtes.addWidget(wdg)
        
        

    def setMVCtoAll(self):
        '''
        Metodo para configurar o MVC para todos POPIN'S  existentes
        no Dicionario Este metodo so Corre uma vez.
        Os POPIN'S sao configuradas passando o id e idx,
        o id e extraido do Dicionario no ItemClicked, 
        e caso nao tenha passamos -99.
        Args:
            idx= index/posicao do elemento pretendido 
            id_parente= Id do parente (Distribuisaoporclass parente Sexo parente AmostEspecies parente Especies parente AmostCatComercial parente Lances para Viagens para Artes parente Saidas
        '''
        for idx in range (len(self.DictGridLay['TblName'])):
            try:
                Id, _ = self.DictGridLay['ItemClicked'][idx]
            except TypeError:
                Id= -99
            self.setDialogWidget(idx= idx, id_parent= Id)
    
    
    def openToInser(self):
        '''
        Metodo para abrir o dialog para insersao de Dados
        '''
        bOK, idx= self.getSenderIdx(dictIdx=self.DictSenderIdx)
        if bOK:
            bOK= self.openDlg(idx=idx)
        return bOK
    
         
    def setDialogWidget(self, idx=None, id_parent=-99):
        '''
        Metodo para Colocar os POPIN'S no Dialog principal, 
        abrindo o POPIN'S/Widgets num GridLayout no Dialog principal
        depois atribuimos o POPIN'S/Widgets ao Dicionario na posicao WIDGETRUNING 
        para mais tarde podermos aceder o widget sem precisarmos criar um novo POPIN'S/Widgets 
        e depois a dicionamos a GridLayout
        Args:
            idx= index/posicao do elemento pretendido 
            id_parente= Id do parente (Distribuisaoporclass parente Sexo parente AmostEspecies parente Especies parente AmostCatComercial parente Lances para Viagens para Artes parente Saidas
        '''
        wdg = self.DictGridLay['WidgetToView'][idx](dbcon=self.dbcon, TblName= self.DictGridLay['TblName'][idx], Id=id_parent)
        self.DictGridLay['WidgetRuning'][idx] = wdg
        self.DictGridLay['GridLayout'][idx].addWidget(wdg)

        
         
    def updateModelOnNextView(self):
        '''
        Metodo para atulizar o modelo do Dialog descendente do Dailog corrente,
        Artes -> Viagens -> lances -> CategoriaComercial -> Amost.CatComercial ->
        Especies -> Amost.Especies -> sexo -> CompAmostra.
        E Depois Limpar os Ultimos elementos selecionada a partir do idx.
        '''
        bOK, idx = self.getSenderIdx(dictIdx=self.DictIdxDepend) 
        if bOK:
            Id, _ = self.DictGridLay['ItemClicked'][idx]
            self.updateModelInView(idx=idx, id_parent= Id)
          
               
               
    def clearlastClicked(self, idx=None):
        '''
        Metodo para limpar, a lista dos ultimos elementos 
        selecionados e os modelindexs, Para quando se for a selecionar num
        elemento diferent, atualizar todos os views dependetes.
        Depois atualizar o model.
        Args:
            idx= index/posicao do elemento pretendido 
        '''
        lstClickedMidx= self.DictGridLay['lstLastClicked']
        for idx1 in range (idx+1, len(lstClickedMidx)):
            self.DictGridLay['lstLastClicked'][idx1]= None
            self.DictGridLay['ItemClicked'][idx1]= None
            if idx1 < len(lstClickedMidx):
                self.updateModelInView(idx=idx1)
       
       
    def updateItemClicked(self, newVal=None, idx=None):
        
        #=======================================================================
        # Metodo para atulizar a lista de Valores selecionadaos 
        # com o novo valor selecionado
        # Args:
        #     newVal= tupla do novo valore (id, row)
        #     idx= index/posicao do elemento pretendido 
        #=======================================================================
        
        if idx is None:
            bOK, Newidx = self.getSenderIdx(dictIdx=self.DictIdxDepend)
            if bOK :
                idx=Newidx
        self.DictGridLay['ItemClicked'][idx] = newVal

           
    def updateModelInView(self, idx=None, id_parent= -99):
        
        #=======================================================================
        # Metodo para atualizar o modelo Dentro dos POPIN'S/Widgets sem precisarmos reniciar a POPIN'S/Widgets. 
        # Args:
        #     idx= index/posicao do elemento pretendido 
        #     id_parente= Id do parente (Distribuisaoporclass parente Sexo parente AmostEspecies parente Especies parente AmostCatComercial parente Lances para Viagens para Artes parente Saidas
        #=======================================================================
        
        filtro = self.DictGridLay['filtros'][idx]
        filtro = filtro.format(id = id_parent)#Depois de se levar o filtro correspondente, formatamos ele com id correcto.
        self.DictGridLay['WidgetRuning'][idx].model.setFilter(filtro)#Depois acessamos ao modelo no WIDGETRUNING e alteramos o seu filtro
        self.DictGridLay['WidgetRuning'][idx].model.select()#Depois Seleciona todos elementos para prencher o modelo
        self.clearlastClicked(idx= idx)#Depois a limpamos os LastClicked de todo elementos apartir de idx+1 ate 8
        if idx is 1:
            try:
                '''
                Quando idx for 1 devemos mover para o mappper para o next depois leva-se o valor para 
                atualizar o item Clicked e por fim atulizamos o modelo dos Elementos no 2 lugar e
                Depois atribuimos o valor ao LCD
                '''
                self.DictGridLay['WidgetRuning'][idx].clearWidgets_Viagens()
                self.DictGridLay['WidgetRuning'][idx].cMapper.mapper.setModel(self.DictGridLay['WidgetRuning'][idx].model)
                self.DictGridLay['WidgetRuning'][idx].cMapper.mapper.toFirst()
                self.DictGridLay['WidgetRuning'][idx].cMapper.mapper.toNext()
                val = self.DictGridLay['WidgetRuning'][idx].cMapper.getValueFromMapper()
                self.DictGridLay['ItemClicked'][2] = val
                Id, row = self.DictGridLay['ItemClicked'][2]
                self.updateModelInView(idx=2, id_parent=Id)
                self.DictGridLay['WidgetRuning'][idx].setLCD(val= row)
            except AttributeError:
                pass
            
   
    def getSenderIdx(self, dictIdx=None):
        '''
        Method to find the sender index in the dictionary.
        '''
        bOK = False
        sender = self.sender().objectName()
        try:
            bOK =True
            idx = dictIdx[sender]
        except KeyError:
            bOK= False
            idx = -99
        finally:
            return bOK, idx  
  
   
    def openToEdit(self):
        '''
        Metodo para abrir o dialog para Edicao dos Dados,
        para Que se possa fazer edicao o MODELIDXCLICKED tem que 
        ser Dirente de none, porque se for none signifaca que nao-se foi 
        selecionado nenhum elemento no POPIN do parente.
        '''
        bOK, idx= self.getSenderIdx(dictIdx=self.DictSenderIdx)
        try:
            ClickedlstVal = self.DictGridLay['lstLastClicked'][idx]
            if ClickedlstVal is not None:
                bOK= self.openDlg(idx= idx, ClickedlstVal= ClickedlstVal)
            else:
                QT_msg.aviso(txt="Atencao, Se pretende editar Porfavor selecione um elemento na tabela.")       
        except Exception as Er:
            QT_msg.error(txt="Aviso Aconteceu um erro inesperado ao tentar abrir um dialog para editar os elementos.", verbTxt=str(Er))
        return bOK
          
   
    def openDlg(self, idx=None, ClickedlstVal=None):
        '''
        Metodo para abrir um pop out, para inserir dados na Tabela selecionada,
        este metodo abri uma janela para insercao de dados. as janelas podem varia 
        deacordo com a posicao.
        primerio, lavamos o nome da tabela no dicionario,
        depois os nomes das colunas que vamos querer inserir 
        depois a list se os elementos seram quotedes ou nao.
        Depois a Janela e executada, onde quando ele e fechada levamos 
        os elementos do GetVal e inderimos na base de dados e atualizamos o modelo.
        '''
        bOK = False
        try:
            tblName = self.DictGridLay['TblName'][idx]
            Id,_ = self.DictGridLay['ItemClicked'][idx] 
            run = self.DictGridLay['dialogsToOpen'][idx](TblName=tblName , dbcon=self.dbcon, Id=Id, lstValToEdit=ClickedlstVal, dictRules = self.dictRules)
            run.exec_()
            if run.close():
                bOK, msg = run.bOK
                self.DictGridLay['lstLastClicked'][idx] = None
                if bOK:
                    self.showMsg(obj= self.LBwhois, msgAlert= msg)
        except TypeError: 
            bOK=False
            QT_msg.aviso(txt="Atenção, porfavor selecione um elemento da tabela atecedente, para poder proceder com a operacao")
        except Exception: 
            bOK=False
            QT_msg.aviso(txt="Aconteceu um erro inesperado porfavor volte a tentar")
        return bOK
         
         
    def getModelClicked(self, mIdx=None):
        '''
        Metodo para Guardar o model clicked.
        '''
        bOK, idx = self.getSenderIdx(dictIdx=self.DictSenderIdx)
        if bOK:
            lstOut = QT_tblViewUtility.getClickedLstVal(indexModel=mIdx)
            self.DictGridLay['lstLastClicked'][idx] = lstOut
        return bOK
    
    
    def showMsg(self, obj=None, msgAlert=None):
        time = QTimer(self)
        obj.setText(msgAlert)
        QT_widgetsCustom.successDatabase(obj= obj)
        time.start(10000)
        time.setSingleShot(True)
        time.timeout.connect(self.toNormal)
   
   
    def toNormal(self):
        objName = self.LBwhois.objectName()
        css= "#"+str(objName)+"""{
                color:black;
                }"""
        self.LBwhois.setStyleSheet(css)
        self.LBwhois.setText("User Name")

class GenericTabEspecies(GenericTabs):
    
    def setHDWGH(self):
        id_parent = self.lstLastClicked[0]
        wdg = KeepTrack(dbcon=self.dbcon, idx=id_parent)
        self.GLKeppTrack.addWidget(wdg)
    
      
