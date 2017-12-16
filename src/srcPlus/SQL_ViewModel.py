'''
Created on 04/09/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import Qt, QSqlRelationalTableModel
from PyQt5 import QtSql
import QT_msg

class viewModel():
    def __init__(self, dbcon= None, TblName= None, dictModel=None, filtro=None):
        self.TblName = TblName
        self.dictModel = dictModel
        self.filtro = filtro
        self.msg = QT_msg
        self.txt_306 = "Erro nº:309 \nPorfavor tente de novo."
        self.txt_100 = "Erro nº: 100 \nPorfavor tente de novo."
        
        self.setViewModel()
        
    def setViewModel(self):
        self.Model = QSqlRelationalTableModel()
        self.Model.setTable(self.TblName)
        self.Model.setFilter(self.filtro)
        for idx, val in enumerate (self.dictModel['val2Rel']):
            if val is not None:
                self.Model.setRelation(idx, QtSql.QSqlRelation(self.dictModel["relTblName"][idx], val[0], val[1]))  
        self.Model.setSort(0, Qt.AscendingOrder)
        for idx, val in enumerate (self.dictModel['newNames']):
            self.Model.setHeaderData(idx, Qt.Horizontal, val)
        bOK = self.Model.select()
        if not bOK:
            self.msg.error(txt="Erro na configuracao do Modelo", verbTxt=str(self.Model.lastError().text()))
 
 
    