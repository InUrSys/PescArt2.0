'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_CategoriaComercial_ToView import Ui_Dialog
from GenericToViewQDialog import GenericToView
class toView_CatComercial(GenericToView, Ui_Dialog):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None):
        super(toView_CatComercial, self).__init__(parent)
        self.setupUi(self)
        
        self.filtro=("id_lance_pesca = {id}".format(id=Id))
        self.tblName = TblName
        self.con = dbcon
        
        self.lstClicked=None
        self.setDict()
        self.setModelInView(tblView=self.TVCatComercial)
        self.TVCatComercial.clicked.connect(self.setNextView)
        self.PBAdicionarCatComerical.clicked.connect(self.insertClicked)
        self.PBEditarCatComercial.clicked.connect(self.updatedClicked)
        

    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_lance_pesca", "id_categoria", "n_seq_categoria", "peso_total_amost", "uni_total"],
                        'fldToHide':[True, True, False, False,False,False,False],
                        'HeaderNames':["ID", "ID DO LANCE", "CATEGORIA", "Nº DA CATEGORIA", "CAT.TOTAL PESO", "CAT.TOTAL UNI."],    
                        'fldRelTblMain':[None, None, "ref_table", None, None, None],
                        'fldRelName': [None, None, ["id", "nome"] ,None ,None ,None],
                        'sizeCol':[0, 0,120, 50, 50, 50]
                        }