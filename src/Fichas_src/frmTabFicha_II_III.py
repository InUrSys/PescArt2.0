'''
Created on 05/11/2017

@author: chernomirdinmacuvele
'''
from ui_Ficha_Recolha_Tab_Amostras import Ui_frmFichaRecolhaAmostras
from frmFichaRecolhaParte2 import FichaRecolhaParte2

from frmFichaRecolhaParte3 import frmFichaRecolhaParte3
from PyQt5.Qt import QDialog

class frmTabFicha(QDialog, Ui_frmFichaRecolhaAmostras):
    def __init__(self, dbcon=None, Id=None, dictRules=None, mIdxe=None):
        super(frmTabFicha, self).__init__()
        
        self.setupUi(self)
        self.Id= Id
        self.dictRules= dictRules
        self.mIdx= mIdxe
        self.configTabViagem()
        self.TablstLastClicked= []
        self.tabAmostra.tabBar().tabBarClicked.connect(self.updateLastClicked)
        self.PBSair.clicked.connect(self.close)
        self.PBVoltar.clicked.connect(self.close)

    def configTabViagem(self):#Configuracao do primeiro tab
        wdgViagem= FichaRecolhaParte2(dbcon=None, Id= self.Id, dictRules=self.dictRules, mIdxe= self.mIdx)
        self.GLtabViagem.addWidget(wdgViagem)
    
    
    def configTabEspecies(self):#Pode Mudar
        if self.TablstLastClicked != []:
            wdgEspecies= frmFichaRecolhaParte3(dbcon=None, lstLastClicked= self.TablstLastClicked, dictRules=self.dictRules )
            self.GLtabAmostEspecies.addWidget(wdgEspecies)
    
    
    def getListSelected(self):
        lstOut= []
        if self.GLtabViagem.itemAt(0).isEmpty() is False:
            wdg = self.GLtabViagem.itemAt(0).widget()
            lstIn = wdg.GLAmostCat.itemAt(0).widget().TVAmostCategoria.selectedIndexes()
            if lstIn == []:
                lstOut = lstIn
            else:
                row = lstIn[0].row()
                model = lstIn[0].model()
                numCol= lstIn[0].model().columnCount()
                for idx in range(numCol):
                    val = model.record(row).value(idx)
                    lstOut.append(val)
        return lstOut
    
     
    def updateLastClicked(self, idx=None):
        try:
            item = self.GLtabAmostEspecies.takeAt(0)
            widget = item.widget()
            widget.deleteLater()
            self.GLtabAmostEspecies.removeWidget(widget)
        except AttributeError:
            pass
        lstIN = self.getListSelected()
        if self.TablstLastClicked != lstIN:
            self.TablstLastClicked= lstIN
        self.configTabEspecies()
        
            


