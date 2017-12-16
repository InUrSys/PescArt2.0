'''
Created on 05/11/2017

@author: chernomirdinmacuvele
'''
from ui_Ficha_Recolha_Part_III import Ui_Form

from dialog_AmostEspecies import dialog_AmostEspecies
from dialog_AmostEspecificaEspe import dialog_AmostEspecificaEspe
from dialog_AmostSexo import dialog_AmostSexo
from dialog_CompAmost import dialog_CompAmost

from toView_AmostEspecies import toView_AmostEspecies
from toView_AmostEspecificaEspe import toView_AmostEspecificaEspe
from toView_AmostSexo import toView_AmostSexo
from toView_CompAmost import toView_CompAmost
from toView_AmostCompSexo import toView_AmostCompSexo
from dialog_AmosComptSexo import dialog_AmostCompSexo

from GenericTabGridLayout import GenericTabEspecies

class frmFichaRecolhaParte3(GenericTabEspecies, Ui_Form):
    def __init__(self, dbcon= None, lstLastClicked= None, dictRules= None):
        super(frmFichaRecolhaParte3, self).__init__()
        self.setupUi(self)
        
        self.dbcon= dbcon
        self.dictRules= dictRules
        self.lstLastClicked = lstLastClicked
        self.configDict()
        self.configItem0()
        self.setMVCtoAll()
        self.setHDWGH()
    

    def configItem0(self):
        id_parent = self.lstLastClicked[0]
        row = None
        self.DictGridLay['lstLastClicked'][0]= self.lstLastClicked
        self.DictGridLay['ItemClicked'][0] = (id_parent, row)
           

    def configDict(self):
        self.dictDlgEspecie={
                        "names": ["id", "id_amost_desem_cat_comercial", "id_especie", "peso_amost", "n_indiv_amost"],
                        
                        "toQuote":[False, False, True, True, False],
                        
                        "relTblName":[None, None, "ref_especies", None, None],
                        
                        "val2Rel":[None, None ,["id", "nome"] ,None ,None],
                            }
         
         
        self.dictDlgAmostEspe={
                        "names": ["id", "id_comp_especifica", "id_metodo_select", "peso", "n_indiv", "comentario"],
                        
                        "toQuote":[False, False, True, True, False, True],
                        
                        "relTblName":[None, None,"ref_table", None, None, None],
                        
                        "val2Rel":[None, None, ["id", "nome"] ,None ,None ,None]
                            }
         
         
        self.dictDlgSexo={
                        "names": ["id", "id_amost_amost_espe", "id_sexo", "peso_amost", "n_indiv_amost"],
                        
                        "toQuote":[False, False, True, True, False],
                        
                        "relTblName":[None, None, "ref_table", None, None],
                        
                        "val2Rel":[None, None ,["id", "nome"]  ,None ,None]
                            }
        
        
        self.dictAmostSexo={
                            "names": ["id", "id_comp_sexo", "id_metodo_select", "id_medida_comp", "id_aproxima",
                                      "id_intervalo_class", "comp_minimo", "peso", "n_indiv", "comentario", "id_especie"],
                            
                            "toQuote":[False, False, True, True, True,True, True, True, False, True, True],
                            
                            "relTblName":[None, None, "ref_table", "ref_table", "ref_table", None ,None, None ,None, None, "ref_especies"],
                            
                            "val2Rel":[None, None ,["id", "nome"] ,["id", "nome"], ["id", "nome"], None  ,None ,None ,None, None,["id", "nome"]]
                            }
         
         
        self.dictDlgCompAmost={
                        "names": ["id", "id_amost_comp_sexo", "class_comp", "n_indiv"],
                        
                        "toQuote":[False, False, True, True],
                        
                        "relTblName":[None, None, None, None],
                        
                        "val2Rel":[None, None ,None ,None]
                            }
        
        
        self.DictSenderIdx= { 
                        'TVAmostEspecie':0 ,
                        'PBAdicionarEspecies':0,
                        'PBEditarEspecies':0,
                         
                        'TVAmostEspecificaEspecie':1 ,
                        'PBAdicionarAmostEspecificaEspecie':1,
                        'PBEditarEspecieEspecifica':1,
                         
                        'TVAmostSexo':2 ,
                        'PBAdicionarSexo':2,
                        'PBEditarSexo':2,
                        
                        'TVAmostCompSexo':3 ,
                        'PBAdicionarCompSexo':3,
                        'PBEditarCompSexo':3,
                         
                        'TVComprimentos':4 ,
                        'PBAdicionarComprimentos':4,
                        'PBEditarComprimentos':4
                        }
     
     
        self.DictIdxDepend= {
                        'TVAmostCategoria':0 ,
                        
                        'TVAmostEspecie':1 ,
                        
                        'TVAmostEspecificaEspecie':2 ,
                        
                        'TVAmostSexo':3 ,
                        
                        'TVAmostCompSexo':4,
                        
                        'TVComprimentos':None 
                            }
        
        
 
        self.DictGridLay = {
                            'MainDict': [self.dictDlgEspecie, self.dictDlgAmostEspe, self.dictDlgSexo, self.dictAmostSexo, self.dictDlgCompAmost], 
     
                            'TblName': ["t_comp_especifica", "t_amost_comp_especifica", "t_comp_sexo", "t_amost_comp_sexo", "t_comp_amost"],
                             
                            'GridLayout': [self.GLEspecies, self.GLAmostEspe, self.GLSexo, self.GLAmostSexo, self.GLComprimentos ] ,
                             
                            'WidgetToView': [toView_AmostEspecies, toView_AmostEspecificaEspe, toView_AmostSexo, toView_AmostCompSexo, toView_CompAmost],
                             
                            'dialogsToOpen': [ dialog_AmostEspecies, dialog_AmostEspecificaEspe, dialog_AmostSexo, dialog_AmostCompSexo, dialog_CompAmost],
             
                            'WidgetRuning':[None, None, None, None, None],
                             
                            'ItemClicked':[None, None, None, None, None],
                             
                            'lstLastClicked':[None, None, None, None, None],
                             
                            'filtros':["id_amost_desem_cat_comercial ={id}", "id_comp_especifica ={id}", "id_amost_comp_especifica ={id}", "id_comp_sexo ={id}", "id_amost_comp_sexo ={id}"]
         }