'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_Artes_Pesca import Ui_frmArtesPesca
import GenericAmostrasQDialog
class dialog_ArtesAmostradas(GenericAmostrasQDialog.CustomForm_Amostras, Ui_frmArtesPesca):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None, lstValToEdit=None, dictRules = None):
        super(dialog_ArtesAmostradas, self).__init__(parent)
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
        self.configComboxLocal()
        self.configCombox()
            
        self.setValuesToEdit()
        self.setValuesToEditArtes()
        
        self.PBSalvar.clicked.connect(self.operacao)
        self.PBCancelar.clicked.connect(self.close)
    
        
    def setValuesToEditArtes(self):
        if self.lstToEdit is not None:
            self.setLocalizacao(nome=self.lstToEdit[2])
    

    def setDict(self):
    #======================================================================================================================
        #Dicionario das Saidas Distritos, Municipios e centros
        self.dictLocal = {
                    'CBProvincia':{'query': "select null as id, '-Provincia-' UNION ALL select id, nome from ref_geometric  where id_tiplocal = 'PRV';",
                                   'wdgt': self.CBProvincia,
                                   'nextLVL':'CBDistrito'
                                   },
                    
                    'CBDistrito':{ 'query':"select null as id, '-Distrito-' UNION ALL select id, nome from ref_geometric  where id_tiplocal = 'DST' and id_parent = '{val}';",
                                   'wdgt': self.CBDistrito,
                                   'nextLVL':'CBPosto'
                                },
                    
                    'CBPosto':{'query':"select null as id, '-Posto Administrativo-' UNION ALL select id, nome from ref_geometric  where id_tiplocal = 'PSD' and id_parent = '{val}';",
                                   'wdgt': self.CBPosto,
                                   'nextLVL':'CBCentroPesca'
                                },
                     
                    'CBCentroPesca':{'query':"select null as id, '-Centro de Pesca-' UNION ALL select id, nome from ref_geometric  where id_tiplocal = 'CTP' and id_parent = '{val}';",
                                     'wdgt': self.CBCentroPesca,
                                     'nextLVL':None
                                }
                     }
        
        self.dictFields= {
                        'fldName': ["id", "id_saida", "id_centro", "id_tip_uni_pesca", "n_activas", "n_nao_activas", "n_amostradas"],
                        'objName': ['id', 'id_saida', 'CBCentroPesca', 'CBArtes', 'SBActivas', 'SBN_Activas', 'SBAmostradas'],
                        'fldWidget': [None, None, self.CBCentroPesca, self.CBArtes, self.SBActivas, self.SBN_Activas, self.SBAmostradas],
                        'isRel':[False, False, True, True, False, False, False],
                        'toDefault':[False, False, False, False, False, False, False],
                        'toCheck': [False, False, True, True, True, True, True],
                        "toQuote":[False, False, True, True, False, False, False]
                         }
        
        self.dictCB= {
                        'quer':["select null as id, '-Tipo de unidade de Pesca-' as nome union all select  id, nome from ref_unidpescatipo where id_tipbarco is null;"],
                        'widget':[self.CBArtes]
                      }
    
    