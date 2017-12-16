'''
Created on 05/09/2017

@author: chernomirdinmacuvele
'''

from ui_Saidas_Obs  import Ui_frmFactores
import GenericAmostrasQDialog

class dialog_Factores(GenericAmostrasQDialog.CustomForm_Amostras, Ui_frmFactores):
    def __init__(self, parent=None, TblName=None, dbcon=None, Id=None, lstValToEdit=None, dictRules = None):
        super(dialog_Factores, self).__init__(parent)
        self.setupUi(self)   
        
        self.N_Sequencial_Parent = str(Id)
        self.tblName = TblName
        self.lstToEdit = lstValToEdit
        self.dictRules = dictRules
        self.setDict()
        self.bOK= (False, None)
        self.lastChecked = None
        self.configWidgetTriggeredEvent()
        self.configRules()
        self.configKeepTrack(id_parente=Id)
        self.setValuesToEdit()
        self.configCombox()
        
        self.PBSalvar.clicked.connect(self.operacao)
        self.PBCancelar.clicked.connect(self.close)
    

    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_saida","id_factore", "comentario"],
                        'fldWidget': [None, None, self.CBFactores, self.LEComentarios ],
                        'toDefault':[False, False, False, True],
                        'objName': ['id', 'id_saidas', 'CBFactores', 'LEComentarios'],
                        'isRel':[False, False, True, False],
                        'toCheck': [False, False, True, True],
                        "toQuote":[False, False, True, True],
                         }
        
        self.dictCB= {
                'quer':["select null as id, '-Factor-' as nome union all select  id, nome from ref_table where id_grupo = 'FCT'"],
                'widget':[self.CBFactores]
              }

