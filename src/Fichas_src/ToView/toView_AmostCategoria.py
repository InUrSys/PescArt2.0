'''
Created on 05/09/2017

@author: chernomirdinmacuvele
'''

from ui_AmostradCatComercial_ToView  import Ui_Dialog
from GenericToViewQDialog import GenericToView
import QT_tblViewUtility
class toView_AmostCategoria(GenericToView, Ui_Dialog):
    def __init__(self, parent=None, TblName=None, dbcon=None, Id=None):  
        super(toView_AmostCategoria, self).__init__(parent)
        self.setupUi(self)   
        
        self.filtro=("id_desem_cat_comercial = {id}".format(id=Id))
        self.tblName = TblName
        self.con = dbcon
        
        self.lstClicked= None
        self.model= None
        self.setDict()
        self.setModelInView(tblView= self.TVAmostCategoria)
        self.TVAmostCategoria.clicked.connect(self.updatedLastClicked)
        self.PBAdicionarAmostCat.clicked.connect(self.insertClicked)
        self.PBEditarAmostCat.clicked.connect(self.updatedClicked)

    def updatedLastClicked(self, mdIx=None):
        self.parent().parent().getModelClicked(mIdx=mdIx)
        lstOut = QT_tblViewUtility.getClickedLstVal(indexModel=mdIx)
        self.parent().parent().lstLastClicked = lstOut
        

    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_desem_cat_comercial", "id_metodo_select", "peso", "n_indiv", "comentario"],
                        'fldToHide':[True, True, False, False, False, False],
                        'HeaderNames':["ID", "ID DO CATEGORIA", "MET. SELECAO", "PESO", "Nº AMOST", "COMENTARIOS"],
                        'fldRelTblMain':[None, None, "ref_table", None, None, None],
                        'fldRelName': [None, None, ["id", "nome"], None ,None ,None],
                        'sizeCol':[0, 0, 80, 70, 50, 50],
                        }
