'''
Created on 01/09/2017

@author: chernomirdinmacuvele
'''
from ui_Ficha_Recolha_Part_II import Ui_Form

from dialog_ArtesAmostradas import dialog_ArtesAmostradas
from dialog_LancePesca import dialog_LancePesca
from dialog_CatComercial import dialog_CatComercial
from dialog_AmostCategoria import dialog_AmostCategoria
from dialog_ViagensPesca import dialog_ViagemPesca

from toView_ArtesAmostradas import toView_ArtesAmostradas
from toView_ViagensPesca import toView_ViagemPesca
from toView_LancePesca import toView_LancePesca
from toView_CatComercial import toView_CatComercial
from toView_AmostCategoria import toView_AmostCategoria

from GenericTabGridLayout import GenericTabs

class FichaRecolhaParte2(GenericTabs, Ui_Form ):
    def __init__(self, dbcon=None, Id=None, dictRules = None, mIdxe=None):
        super(FichaRecolhaParte2, self).__init__()
        self.setupUi(self)
        
        self.configDict()
        self.dbcon= dbcon
        self.DictGridLay['ItemClicked'][0] = (str(Id),None)
        self.dictRules = dictRules
        self.mIdex = mIdxe
        
        self.lstLastClicked = []
        self.setMVCtoAll()
        self.setRowToSameAsClickedOnSaidas()
            
    def setRowToSameAsClickedOnSaidas(self):
        '''
        Metodo para deixara a mesma linha selecionada como a que foi
        selecionada nas saidas/Artes.
        '''
        self.DictGridLay['WidgetRuning'][0].setSameClicked()
        
    
    def configDict(self): 
        self.dictDlgArtesAmostradas={
                        "names": ["id", "id_saida", "id_centro", "id_tip_uni_pesca", "n_activas", "n_nao_activas", "n_amostradas"],
                        
                        "toQuote":[False, False, True, True, False, False, False],
                        
                        "relTblName":[None, None, "ref_geometric", "ref_unidpescatipo", None, None],
                        
                        "val2Rel":[None, None, ["id", "nome"] ,["id", "nome"]  ,None ,None]
                            }
                        
                        
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
                        'TVArtePesca':0 ,
                        'PBAdicionarArtes':0 ,
                        'PBEditarArtes':0,
                        'PBAmostras':0,
                         
                        'PBNext':1 ,
                        'PBBack':1 ,
                        'PBAdicionarViagens':1,
                        'PBEditarViagens':1,
                         
                        'TVLances':2 ,
                        'PBAdicionarLances':2,
                        'PBEditarLAnces':2,
                         
                        'TVCatComercial':3 ,
                        'PBAdicionarCatComerical':3,
                        'PBEditarCatComercial':3,
                         
                        'TVAmostCategoria':4 ,
                        'PBAdicionarAmostCat':4,
                        'PBEditarAmostCat':4,
                        }
     
     
        self.DictIdxDepend= {
                        'TVArtePesca':1,
                        'PBAmostras':1,
                         
                        'PBNext':2 ,
                        'PBAdicionarViagens':2,
                        'PBEditarViagens':2,
                        'PBBack':2 ,
                         
                        'TVLances':3 ,
                        
                        'TVCatComercial':4 ,
                        
                        'TVAmostCategoria':None
                            }
        
        
        
        
        self.DictGridLay = {
                            'MainDict': [self.dictDlgArtesAmostradas, self.dictDlgViagemPesca, self.dictDlgLancesPesca,
                                          self.dictDlgCatComercial, self.dictDlgAmostCategoria], 
     
                            'TblName': ["t_activ_tip_unidade", "t_viagem_pesca", "t_lance_pesca", "t_desem_cat_comercial", "t_amost_desem_cat_comercial"],
                             
                            'GridLayout': [self.GLArtes, self.GLViagens, self.GLLances, self.GLCategorias, self.GLAmostCat ] ,
                             
                            'WidgetToView': [toView_ArtesAmostradas, toView_ViagemPesca, toView_LancePesca, toView_CatComercial, toView_AmostCategoria],
                             
                            'dialogsToOpen': [dialog_ArtesAmostradas, dialog_ViagemPesca, dialog_LancePesca, dialog_CatComercial, dialog_AmostCategoria],
             
                            'WidgetRuning': [None, None, None, None, None],
                             
                            'ItemClicked': [None, None, None, None, None],
                             
                            'lstLastClicked': [None, None, None, None, None],
                             
                            'filtros':["id_saida ={id}", "id_activ_tip_unidade ={id}", "id_viagem_pesca ={id}", "id_lance_pesca ={id}", "id_desem_cat_comercial ={id}"]       
                                
                                }