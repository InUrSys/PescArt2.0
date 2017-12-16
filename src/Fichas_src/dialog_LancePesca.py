'''
Created on 05/09/2017

@author: chernomirdinmacuvele
'''

from ui_LancesPesca  import Ui_frmLancesPesca
import GenericAmostrasQDialog
class dialog_LancePesca(GenericAmostrasQDialog.CustomForm_Amostras, Ui_frmLancesPesca):
    def __init__(self, parent=None, TblName=None, dbcon=None, Id=None, lstValToEdit=None,dictRules = None):  
        super(dialog_LancePesca, self).__init__(parent)
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
        
        self.PBSalvar.clicked.connect(self.operacao)
        self.PBCancelar.clicked.connect(self.close)
    
    def setDict(self):
        self.dictFields= {
                        'fldWidget': [None, None, self.DSBCapTotal, self.TEInicio, self.TEFim, self.SBNSeqLance],
                        'toDefault':[None],
                         }
  
        
        self.dictFields= {
                            'fldName': ["id", "id_viagem_pesca", "cap_total_peso", "hora_inicio", "hora_fim",'n_seq_lance'],
                            'objName': ['id', 'id_viagem_pesca', 'DSBCapTotal', 'TEInicio', 'TEFim', 'SBNSeqLance'],
                            'fldWidget': [None, None, self.DSBCapTotal, self.TEInicio, self.TEFim, self.SBNSeqLance],
                            'isRel':[False, False, False, False, False, False],
                            'toDefault':[False, False, False, False, False, False],
                            'toCheck': [False, False, True, True, True, True],
                            "toQuote":[False, False, True, True, True, False]
                             }
            

        self.dictSql= {
                        'fldRelTblMain': [None],
                        'fldRelWidg': [None],
                        'fldRelName': [None],
                        'fldToQuote': [None],
                        'fldCond': [None],
                        'fldCondVal':[None]
                      }
    
    