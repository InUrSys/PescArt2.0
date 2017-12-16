'''
Created on 26/11/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QSortFilterProxyModel
from ui_simpleSearch import Ui_Form
import QT_tblViewUtility
class simpleSearch(QDialog,Ui_Form):
    def __init__(self, lastSelected=None, model=None):
        super(simpleSearch, self).__init__()
        self.setupUi(self)
        
        self.lastSelected = lastSelected
        self.model = model
        self.bOK = False,None
        self.setModel()
        self.toEdit()
        self.LENome.textChanged.connect(self.find)
        self.PBOK.clicked.connect(self.getChecked)
        
        
    def setModel(self):
        QT_tblViewUtility.setModelInView(tblView= self.TView, ViewModel=self.model)
        QT_tblViewUtility.setViewCustom(tblView= self.TView, lstSizeCol= [300])
    
    
    def toEdit(self):
        if self.lastSelected is not None:
            for val in self.lastSelected:
                model = self.TView.model()
                rows = model.rowCount()
                for idx in range(rows):
                    valTxt = model.item(idx).text()
                    if val == valTxt:
                        model.item(idx).setCheckState(2)
                        
                        
    
    def find(self, text=None):
        text= text.capitalize()
        if text is not '': 
            model = QSortFilterProxyModel()
            model.setSourceModel(self.model)
            model.setFilterRegExp(str(text))
            self.TView.setModel(model)
        else:
            self.TView.setModel(self.model)
    
    def getChecked(self):
        self.LENome.setText('')
        lstOut= []
        model = self.TView.model()
        rows = model.rowCount()
        for row in range(rows):
            item= model.item(row)
            state= item.checkState()
            if state == 2:
                val= model.item(row).text()
                lstOut.append(val)
        self.bOK= (True,lstOut)
        self.close()
        
                
        
    
        