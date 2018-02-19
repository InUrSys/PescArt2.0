'''
Created on 29/01/2018

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QRadioButton
from ui_frmSort import Ui_Form

class frmSortting(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(frmSortting, self).__init__(parent)
        self.setupUi(self)
        
        self.PBFechar.clicked.connect(self.toClose)
        self.fQuery = None
    
    def toClose(self):
        self.getSort()
        self.close()
        
    def getSort(self):
        dictAsc = {self.RBAsc1: "data_amostragem asc, ",
                   self.RBAsc2: "tbl2.nome asc, ",
                   self.RBAsc3: "tbl3.nome asc, ", 
                   self.RBAsc4: "hora_inicioamo asc, ", 
                   self.RBAsc5: "hor_fimamo asc, ",
                   self.RBAsc6: "tbl4.nome asc, "
                   }
        
        dictDesc = {self.RBDsc1: "data_amostragem desc, ", 
                    self.RBDsc2: "tbl2.nome desc, ",  
                    self.RBDsc3: "tbl3.nome desc, ",  
                    self.RBDsc4: "hora_inicioamo desc, ", 
                    self.RBDsc5: "hor_fimamo desc, ",  
                    self.RBDsc6: "tbl4.nome desc, "
                    }
        
        lstNone = [self.RBNone_1, self.RBNone_2,  self.RBNone_3, self.RBNone_4, self.RBNone_5, self.RBNone_6]
                    
        
        fQuery = " "
        lstDesc = list(dictDesc.keys())
        for idx, wdg in enumerate (dictAsc.keys()):
            if wdg.isChecked():
                fQuery += dictAsc[wdg]
                
            elif lstDesc[idx].isChecked():
                wdg = lstDesc[idx]
                fQuery += dictDesc[wdg]
                
        for wdg in lstNone:
            if wdg.isChecked() == False:
                fQuery += fQuery[:-2]
                break
            
            
                
        self.fQuery = fQuery