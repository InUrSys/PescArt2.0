'''
Created on 05/09/2017

@author: chernomirdinmacuvele
'''

from ui_AmostradCatComercial  import Ui_frmAmostCatComercial
import GenericAmostrasQDialog
class dialog_AmostCategoria(GenericAmostrasQDialog.CustomForm_Amostras, Ui_frmAmostCatComercial):
    def __init__(self, parent=None, TblName=None, dbcon=None, Id=None, lstValToEdit=None, dictRules = None):  
        super(dialog_AmostCategoria, self).__init__(parent)
        self.setupUi(self)
        
        self.N_Sequencial_Parent = str(Id)
        self.tblName = TblName
        self.lstToEdit = lstValToEdit
        self.dictRules = dictRules
        self.bOK= (False, None)
        self.setDict()
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
                        'fldName': ["id", "id_desem_cat_comercial", "id_metodo_select", "peso", "n_indiv", "comentario"],
                        
                        'objName': ['id', 'id_desem_cat_comercial', 'CBMetSelecao', 'DSBPeso', 'SBN_Indiv_Amost', 'LEComentarios'],
                        
                        'fldWidget': [None, None, self.CBMetSelecao ,self.DSBPeso, self.SBN_Indiv_Amost, self.LEComentarios],
                        
                        'isRel':[False, False, True, False, False, False],
                        
                        'toDefault':[None, None, False, False, False, True],
                        
                        'toCheck': [False, False, True, True, True, True],
                        
                        "toQuote":[False, False,True, True, False,True],
                         }

    
        self.dictCB= {
                        'quer':["select null as id, '-Metodo de Selecao-' as nome union all select id, nome from ref_table where id_grupo = 'MTS' and activo =true;"],
                        
                        'widget':[self.CBMetSelecao]
                      }
    