'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_AmostraSexo import Ui_frmAmostSexo
import GenericAmostrasQDialog
class dialog_AmostSexo(GenericAmostrasQDialog.CustomForm_Amostras, Ui_frmAmostSexo):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None, lstValToEdit=None ,dictRules = None):
        super(dialog_AmostSexo, self).__init__(parent)
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
                        'fldName': ["id", "id_amost_comp_especifica", "id_sexo", "peso_amost", "n_indiv_amost"],
                        'fldWidget': [None, None, self.CBSexo, self.DSBPeso,  self.SBN_indiv ],
                        'objName': ['id', 'id_amost_comp_especifica', 'CBSexo', 'DSBPeso', 'SBN_indiv'],
                        'isRel':[False, False, True, False, False],
                        'toDefault':[False, False, False, False, False],
                        'toCheck': [False, False, True, True, True],
                        "toQuote":[False, False, True, True, False]
                         }
        
        self.dictCB= {
                        'quer':["select null as id, '-Sexo-' as nome union all select id, nome from ref_table where id_grupo = 'SEX' and activo =true;"],
                        
                        'widget':[self.CBSexo]
                      }