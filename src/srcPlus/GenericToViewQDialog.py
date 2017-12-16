'''
Created on 26/10/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog
import mixedModel as mModel
import QT_tblViewUtility
class GenericToView(QDialog):
    
    def setModelInView(self, tblView=None):
        '''
        Metodo de configuracao do modelo, este metodo cria o modelo que sera usado, para-se 
        vizualizar os dados, nos POPIN'S.
        o modelo apois serem Criado, Costumizamos os Headers e o tamanho.
        Args:
            tblView= Nome do TableView
        '''
        lstVal2Rel= self.dictFields['fldRelName']
        lstRelTblName= self.dictFields['fldRelTblMain']
        lstNewNames= self.dictFields['HeaderNames']
        bOK, self.model = mModel.setViewModel(tblName=self.tblName, filtro=self.filtro, lstVal2Rel=lstVal2Rel, lstRelTblName=lstRelTblName, lstNewNames=lstNewNames)
        if bOK:
            toHide = self.dictFields['fldToHide']
            lstSizeCol = self.dictFields['sizeCol']
            QT_tblViewUtility.setModelInView(tblView= tblView, ViewModel=self.model, toHide=toHide)
            QT_tblViewUtility.setViewCustom(tblView= tblView, lstSizeCol=lstSizeCol)
      
      
    def getClicked(self, mIdx):
        '''
        Metodo que retorna um tupla com o elemento selecionado e a linha selecionada.
        args:
            mIdx= modelIndex
        '''
        clickedRowVal, ClickdedRow = QT_tblViewUtility.getClicked(indexModel=mIdx)
        self.lstClicked = clickedRowVal, ClickdedRow
        return clickedRowVal, ClickdedRow
                
                
    def setNextView(self, midx=None):
        '''
        Metodo para ativar a tualizar os modelos dos descendentes, os itens selecionados e os modelIndex selecionadaos.
        args:
            mIdx= modelIndex
        '''
        newVal = self.getClicked(mIdx=midx)
        self.parent().parent().updateItemClicked(newVal=newVal)
        self.parent().parent().updateModelOnNextView() 
        self.parent().parent().getModelClicked(mIdx=midx)


    def insertClicked(self):
        '''
        Metodo para abrir o Dialog para insersao De Dados e Atulizar o model
        '''
        bOK = self.parent().parent().openToInser()
        if bOK:
            bOK= self.model.select()
        return bOK
    
    
    def updatedClicked(self):
        '''
        Metodo para abrir o Dialog para Edicao De Dados e Atulizar o model
        '''
        bOK = self.parent().parent().openToEdit()
        if bOK:
            bOK= self.model.select()
        return bOK 