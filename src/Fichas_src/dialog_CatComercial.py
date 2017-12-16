'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_CategoriaComercial import Ui_frmCatComercialAmostra
import GenericAmostrasQDialog
class dialog_CatComercial(GenericAmostrasQDialog.CustomForm_Amostras, Ui_frmCatComercialAmostra):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None, lstValToEdit=None,dictRules = None):
        super(dialog_CatComercial, self).__init__(parent)
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
                        'fldName': ["id", "id_lance_pesca", "id_categoria", "n_seq_categoria", "peso_total_amost", "uni_total"],
                        'fldWidget': [None, None, self.CBCategoria, self.SBN_Seq_Categoria, self.DSBPeso_total_captura, self.SBPesoUnidade ],
                        'objName': ['id', 'id_lance_pesca', 'CBCategoria', 'SBN_Seq_Categoria', 'DSBPeso_total_captura', 'SBPesoUnidade'],
                        'isRel':[False, False, True, False, False, False],
                        'toDefault':[False, False, False, False, False, False],
                        'toCheck': [False, False, True, True, True, True],
                        "toQuote":[False, False, True, False, True, False]
                         }
        
        self.dictCB= {
                        'quer':["select null as id, '-Categorias-' as nome union all select id, nome from ref_table where id_grupo = 'CAT' and activo =true;"],
                        
                        'widget':[self.CBCategoria]
                      }

    