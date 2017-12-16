'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_AmostraEspecie import Ui_frmEspeciesAmostradas
import GenericAmostrasQDialog
class dialog_AmostEspecies(GenericAmostrasQDialog.CustomForm_Amostras, Ui_frmEspeciesAmostradas):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None, lstValToEdit=None, dictRules = None):
        super(dialog_AmostEspecies, self).__init__(parent)
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
        self.configCombox()
        self.setValuesToEdit()
    
    
        self.PBSalvar.clicked.connect(self.operacao)
        self.PBCancelar.clicked.connect(self.close)
        
     
    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_amost_desem_cat_comercial", "id_especie", "peso_amost", "n_indiv_amost"],
                        'objName': ['id', 'id_amost_desem_cat_comercial', 'CBEspecies', 'DSBPesoAmost', 'SBN_Indiv'],
                        'fldWidget': [None, None, self.CBEspecies, self.DSBPesoAmost, self.SBN_Indiv ],
                        'isRel':[False, False, True, False, False],
                        'toDefault':[False, False, False, False, False],
                        'toCheck': [False, False, True, True, True],
                        "toQuote":[False, False, True, True, False]
                        }

        
        self.dictCB= {
                        'quer':["select null as id, '-Especies-' as nome union all select id, nome from ref_especies where activo =true;"],
                        
                        'widget':[self.CBEspecies]
                      }
        
    