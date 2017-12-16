'''
Created on 05/09/2017

@author: chernomirdinmacuvele
'''

from ui_AmostEspeEspecie_ToView  import Ui_Dialog
from GenericToViewQDialog import GenericToView
class toView_AmostEspecificaEspe(GenericToView, Ui_Dialog):
    def __init__(self, parent=None, TblName=None, dbcon=None, Id=None):  
        super(toView_AmostEspecificaEspe, self).__init__(parent)
        self.setupUi(self)   
        self.id=id

        self.filtro=("id_comp_especifica = {id}".format(id=Id))
        self.tblName = TblName
        self.con = dbcon
        
        self.lstClicked=None
        self.setDict()
        self.setModelInView(tblView=self.TVAmostEspecificaEspecie)
        self.TVAmostEspecificaEspecie.clicked.connect(self.setNextView)
        self.PBAdicionarAmostEspecificaEspecie.clicked.connect(self.insertClicked)
        self.PBEditarEspecieEspecifica.clicked.connect(self.updatedClicked)
        
        
    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_comp_especifica", "id_metodo_select", "peso", "n_indiv", "comentario"],
                        'fldToHide':[True, True, False, False, False, False],
                        'HeaderNames':["ID", "ID DA ESPECIE", "MET. SELECAO" ,"PESO TOTAL", "Nº AMOSTRADO", "COMENTARIOS"],
                        'fldRelTblMain':[None, None, "ref_table", None, None, None],
                        'fldRelName': [None, None, ["id", "nome"], None ,None ,None],
                        'sizeCol':[0,0, 100, 80, 100, 100]
                        }