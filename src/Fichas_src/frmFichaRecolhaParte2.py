'''
Created on 01/09/2017

@author: chernomirdinmacuvele
'''
from ui_Ficha_Recolha_Part_II import Ui_Form

from dialog_LancePesca import dialog_LancePesca
from dialog_CatComercial import dialog_CatComercial
from dialog_AmostCategoria import dialog_AmostCategoria
from dialog_ViagensPesca import dialog_ViagemPesca

from toView_ViagensPesca import toView_ViagemPesca
from toView_LancePesca import toView_LancePesca
from toView_CatComercial import toView_CatComercial
from toView_AmostCategoria import toView_AmostCategoria

from toView_keep_track_ArtesPesca import toView_Keep_track_ArtesPesca 

from GenericTabGridLayout import GenericTabs

class FichaRecolhaParte2(GenericTabs, Ui_Form ):
    def __init__(self, dbcon=None, Id=None, dictRules = None, mIdxe=None):
        super(FichaRecolhaParte2, self).__init__()
        self.setupUi(self)
        
        self.configDict()
        self.dbcon= dbcon
        self.lastClicked = (str(Id),None)
        self.dictRules = dictRules
        self.mIdex = mIdxe
        self.lstLastClicked = []
        
        self.setHDWGH()
        
        self.setMVCtoAll()
    
    
    def configDict(self):                         
                        
        self.dictDlgViagemPesca={
                        "names": ["id", "id_activ_tip_unidade", "id_unipesca", "id_pesqueiro",
                                    "id_uniamostra", "id_tip_uni_pesca" "n_sequnidade", "n_pescadores", "comp_rede",
                                    "comp_cabo", "tam_malha", "n_lances_amostrados", "n_lances_totais",
                                    "cap_total", "data_inicio", "data_fim", "hora_inicio",
                                    "hora_fim"],
                                 
                        "toQuote":[False, False, True, False, 
                                    True, True, False, False, True,
                                    True, True, False,False, 
                                    True, True, True, True,
                                    True],
                                 
                        "relTblName":[None, None, None ,"ref_pesqueiro"
                                    ,"ref_table", "ref_unidpescatipo",None, None, None
                                    ,None, None, None, None,
                                    None,None,None,None,
                                    None],
                            
                        "val2Rel":[None, None, ["id", "nome"], ["id", "nome"], 
                                   ["id", "nome"],["id", "nome"], None, None, None, 
                                   None,  None,  None, None, 
                                   None, None, None, None,
                                   None]
                            }
         
         
        self.dictDlgLancesPesca={
                        "names": ["id", "id_viagem_pesca", "cap_total_peso", "hora_inicio", "hora_fim"],
                        
                        "toQuote":[False, False, True, True, True],
                        
                        "relTblName":[None, None, None, None, None],
                        
                        "val2Rel":[None, None, None ,None ,None]
                            }
         
         
        self.dictDlgCatComercial={
                        "names": ["id", "id_lance_pesca", "id_categoria", "n_seq_categoria", "peso_total_amost", "uni_total"],
                        
                        "toQuote": [False, False, True, False, True, False],
                        
                        "relTblName": [None, None, "ref_table", None, None, None],
                        
                        "val2Rel": [None, None, ["id", "nome"] ,None ,None ,None]
                            }
         
         
        self.dictDlgAmostCategoria={
                        "names": ["id", "id_desem_cat_comercial", "id_metodo_select", "peso", "n_indiv", "comentarios"],
                        
                        "toQuote": [False, False, True, True, False,True],
                        
                        "relTblName": [None, None, "ref_table",None, None, None],
                        
                        "val2Rel": [None, None, ["id", "nome"]  ,None ,None ,None],
                            }
         
         
        self.DictSenderIdx= {

                        'TVViagens':0 ,
                        'PBAdicionar':0,
                        'PBEditar':0,
                         
                        'TVLances':1,
                        'PBAdicionarLances':1,
                        'PBEditarLAnces':1,
                         
                        'TVCatComercial':2,
                        'PBAdicionarCatComerical':2,
                        'PBEditarCatComercial':2,
                         
                        'TVAmostCategoria':3,
                        'PBAdicionarAmostCat':3,
                        'PBEditarAmostCat':3,
                        }
     
     
        self.DictIdxDepend= {
                        'PBDown':0,
                        'PBUp':0,

                        'TVViagens':1,
                         
                        'TVLances':2,
                        
                        'TVCatComercial':3,
                        
                        'TVAmostCategoria':None
                            }
        
        
        self.DictGridLay = {
                            'MainDict': [self.dictDlgViagemPesca, self.dictDlgLancesPesca,
                                          self.dictDlgCatComercial, self.dictDlgAmostCategoria], 
     
                            'TblName': ["t_viagem_pesca", "t_lance_pesca", "t_desem_cat_comercial", "t_amost_desem_cat_comercial"],
                             
                            'GridLayout': [self.GLViagens, self.GLLances, self.GLCategorias, self.GLAmostCat ] ,
                             
                            'WidgetToView': [toView_ViagemPesca, toView_LancePesca, toView_CatComercial, toView_AmostCategoria],
                             
                            'dialogsToOpen': [dialog_ViagemPesca, dialog_LancePesca, dialog_CatComercial, dialog_AmostCategoria],
             
                            'WidgetRuning': [None, None, None, None],
                             
                            'ItemClicked': [None, None, None, None],
                             
                            'lstLastClicked': [ None, None, None, None],
                             
                            'filtros':["id_activ_tip_unidade ={id}", "id_viagem_pesca ={id}", "id_lance_pesca ={id}", "id_desem_cat_comercial ={id}"]       
                                
                            }