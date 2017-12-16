'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_AmostraSexo_ToView import Ui_Dialog
from GenericToViewQDialog import GenericToView
class toView_AmostSexo(GenericToView, Ui_Dialog):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None):
        super(toView_AmostSexo, self).__init__(parent)
        self.setupUi(self)
        
        self.filtro=("id_amost_comp_especifica = {id}".format(id=Id))
        self.tblName = TblName
        self.con = dbcon
        
        self.lstClicked=None
        self.setDict()
        self.setModelInView(tblView= self.TVAmostSexo)
        self.TVAmostSexo.clicked.connect(self.setNextView)
        self.PBAdicionarSexo.clicked.connect(self.insertClicked)
        self.PBEditarSexo.clicked.connect(self.updatedClicked)
        

    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_amost_comp_especifica", "id_sexo", "peso_amost", "n_indiv_amost"],
                        'fldToHide':[True, True, False, False, False],
                        'HeaderNames':["ID", "ID AMOSTRA DA ESPECIE", "SEXO", "PESO AMOST", "Nº INDIV"],
                        'fldRelTblMain':[None, None, "ref_table", None, None],
                        'fldRelName': [None, None ,["id", "nome"]  ,None ,None],
                        'sizeCol': [0,0,80,80,80]
                        }