'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_AmostraEspecie_ToView import Ui_Dialog
from GenericToViewQDialog import GenericToView
class toView_AmostEspecies(GenericToView, Ui_Dialog):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None):
        super(toView_AmostEspecies, self).__init__(parent)
        self.setupUi(self)        
        
        self.filtro=("id_amost_desem_cat_comercial = {id}".format(id=Id))
        self.tblName = TblName
        self.con = dbcon
        
        self.lstClicked=None
        self.setDict()
        self.setModelInView(tblView= self.TVAmostEspecie)
        self.TVAmostEspecie.clicked.connect(self.setNextView)
        self.PBAdicionarEspecies.clicked.connect(self.insertClicked)
        self.PBEditarEspecies.clicked.connect(self.updatedClicked)
        
        
    def unlockEdit(self,Bstate=True):
        self.PBEditarEspecies.setDisabled(Bstate)
    
    
    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_amost_desem_cat_comercial", "id_especie", "peso_amost", "n_indiv_amost"],
                        'fldToHide':[True, True, False, False, False, False],
                        'HeaderNames':["ID", "ID AMOSTRA DA CATEGORIA", "ESPECIE", "PESO AMOST.", "Nº INDIV"],    
                        'fldRelTblMain':[None, None, "ref_especies", None, None],
                        'fldRelName': [None, None ,["id", "nome"] ,None ,None],
                        'sizeCol':[0, 0, 180, 80, 80],
                        }
