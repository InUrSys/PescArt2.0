'''
Created on 05/09/2017

@author: chernomirdinmacuvele
'''

from ui_LancesPesca_ToView  import Ui_Dialog
from GenericToViewQDialog import GenericToView

class toView_LancePesca(GenericToView, Ui_Dialog):
    def __init__(self, parent=None, TblName=None, dbcon=None, Id=None):  
        super(toView_LancePesca, self).__init__(parent)
        self.setupUi(self)

        self.filtro=("id_viagem_pesca = {id}".format(id=str(Id)))
        self.tblName = TblName
        self.con = dbcon
        self.lstClicked=None
        self.setDict()
        self.setModelInView(tblView= self.TVLances)
        self.TVLances.clicked.connect(self.setNextView)
        self.PBAdicionarLances.clicked.connect(self.insertClicked)
        self.PBEditarLAnces.clicked.connect(self.updatedClicked)
        

    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_viagem_pesca", "cap_total_peso", "hora_inicio", "hora_fim","n_seq_lance"],
                        'fldToHide':[True, True, False, False, False, False],
                        'HeaderNames':["ID", "ID DA VIAGEM", "CAPTURA TOTAL", "INICIO", "FIM", "Nº Lance"],
                        'fldRelTblMain':[None, None, None, None, None, None],
                        'fldRelName': [None, None, None ,None ,None, None],
                        'sizeCol': [0,0,80,80,80,50]
                        }
