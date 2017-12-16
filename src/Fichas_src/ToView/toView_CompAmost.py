'''
Created on 05/09/2017

@author: chernomirdinmacuvele
'''

from ui_compAmostra_TOView  import Ui_Dialog
from GenericToViewQDialog import GenericToView
class toView_CompAmost(GenericToView, Ui_Dialog):
    def __init__(self, parent=None, TblName=None, dbcon=None, Id=None):  
        super(toView_CompAmost, self).__init__(parent)
        self.setupUi(self)   
        self.Id=Id
        self.tblName = TblName
        
        self.filtro=("id_amost_comp_sexo = {id}".format(id=Id))
        self.tblName = TblName
        self.con = dbcon
        self.lstClicked=None
        self.setDict()
        self.setModelInView(tblView= self.TVComprimentos)
        
        self.TVComprimentos.clicked.connect(self.setNextView)
        self.PBAdicionarComprimentos.clicked.connect(self.insertClicked)
        self.PBEditarComprimentos.clicked.connect(self.updatedClicked)
        
        
    def setNextView(self, midx=None):
        newVal = self.getClicked(mIdx=midx)     
        self.parent().parent().getModelClicked(mIdx=midx)
    
    def toInsert(self):
        #open a new Dialog
        pass
    
    def toEdit(self):
        #open a New Dialog with Data To edit
        pass

    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_amost_comp_sexo", "class_comp", "n_indiv"],
                        'fldToHide':[True, True, False, False],
                        'HeaderNames':["ID", "ID AMOSTRA DA SEXO", "COMPRIMENTO", "Nº MEDIDOS"],
                        'fldRelTblMain':[None, None, None, None,],
                        'fldRelName': [None, None, None ,None ],
                        'sizeCol': [0,0,50,50]
                        }
        