'''
Created on 27/11/2017

@author: chernomirdinmacuvele
'''
from ui_user_conf import Ui_Form
from PyQt5.Qt import QDialog, QListView
import mixedModel
class user_config(QDialog, Ui_Form):
    def __init__(self, parent=None, dbcon=None, tblName=None, user_info=None):
        super(user_config, self).__init__(parent)
        self.setupUi(self)
        
        self.dbcon = dbcon
        self.tblName = tblName
        self.user_info = user_info
        self.setMainDict()
        self.setModel()
        self.setModelCB()
        
    def setModelCB(self):
        relVal = self.dictSql['fld'][3]
        wdg = self.dictSql['wdg'][3]
        relTblName = self.dictSql['tblName'][3]
        mixedModel.setModel4CombBox(tblName= relTblName,
                                    lstNames= relVal, 
                                    widg= wdg)
        
        
    def setModel(self):
        relTblName = self.dictSql['tblName']
        relVal = self.dictSql['fld']
        lstWdgts = self.dictUser['fldName']
        bOK, model = mixedModel.setViewModel(tblName= self.tblName,
                                lstVal2Rel= relVal , 
                                lstRelTblName= relTblName)
        if bOK:
            lstWdgts = self.dictUser['widgets']
            Cmodle = mixedModel.withWidgets()
            Cmodle.setMapper(model= model, fldToMap= lstWdgts)
            self.LViewUser.setModel(model)
            self.LViewUser.setModelColumn(1)
        
        
    def setMainDict(self):
        self.dictUser = {
                    'fldName':['id', 'username', 'user_psw', 'user_level', 'user_info', 'activo'],
                    'widgets':[self.LEId, self.LENome, self.LEPsw, self.CBLevel, self.PTEInformacao, self.CHBActivo],
                    'toQuote':[False, False, False, False, False, True]
                    }
        
        self.dictSql = { 'tblName':[None, None, None,'log_level', None, None],
                    'fld':[None, None, None, ['id','nome'], None, None],
                    'wdg':[None, None, None, self.CBLevel, None, None] 
                    }
        
    