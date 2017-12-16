'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_AmostCompSexo_ToView import Ui_Dialog
from GenericToViewQDialog import GenericToView

class toView_AmostCompSexo(GenericToView, Ui_Dialog):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None):
        super(toView_AmostCompSexo, self).__init__(parent)
        self.setupUi(self)
        
        self.filtro=("id_comp_sexo = {id}".format(id=Id))
        self.tblName = TblName
        self.con = dbcon
        
        self.lstClicked=None
        self.setDict()
        self.setModelInView(tblView= self.TVAmostCompSexo)
        self.TVAmostCompSexo.clicked.connect(self.setNextView)
        self.PBAdicionarCompSexo.clicked.connect(self.insertClicked)
        self.PBEditarCompSexo.clicked.connect(self.updatedClicked)
        
        #TO edit when change intervalo_class

    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_comp_sexo", "id_metodo_select", "id_medida_comp", "id_aproxima",
                                      "id_intervalo_class", "comp_minimo", "peso", "n_indiv", "comentario", 'id_especie'],
                          
                        'fldToHide':[True, True, False, False, False, False, False, False, False, True, False],
                        
                        'HeaderNames':["ID", "ID SEXO", "MET. SELECAO", "MED. COMPRIMENTO", "APRIXIMACAO",
                                       "INTER. CLASS", "COMP. MINNIMO", "PESO", "N INDIV", "COMENTARIOS", "ESPECIE"],
                          
                        'fldRelTblMain':[None, None, "ref_table", "ref_table", "ref_table"
                                         , None, None, None, None, None,"ref_especies"],
                        
                        'fldRelName': [None, None ,["id", "nome"], ["id", "nome"], ["id", "nome"],
                                        None, None, None, None, None, ["id", "nome"]],
                          
                        'sizeCol': [0, 0, 80, 80, 80, 80,50, 50, 50, 50, 80]
                        }