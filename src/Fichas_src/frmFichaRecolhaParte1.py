'''
Created on 01/09/2017
@author: chernomirdinmacuvele
'''
from ui_Ficha_Recolha_Part_I import Ui_frmSaidas
from dialog_Factores import dialog_Factores
from dialog_ArtesAmostradas import dialog_ArtesAmostradas
from Sub_GenericSaidas import Generic_Saidas
import FuncSQL
import QT_msg
import frm_imageToPDF
import rscForm

class FichaRecolha(Generic_Saidas, Ui_frmSaidas):
    def __init__(self, dbcon=None, dictTblName=None, dictRules=None):
        super(FichaRecolha,self).__init__()
        self.setupUi(self)
        
        self.dbcon = dbcon
        self.dictTblName = dictTblName
        self.dictRules = dictRules
        self.LEN_Sequencial.setText(str('-99'))#Coloca -99 no id 
        self.lstTemVal = None #Valores temporarios pois insersao ou pesquisa para editar
        self.shareModelIdex = None #Model index compartilhado entre Saidas e Amostras
        self.int_methods()
        
        
    def int_methods(self):
        self.frmName = 'frmFichaRecolhaParte1'
        self.dictKeepTrack=None
        self.setDicts()
        self.setMainDict()
        self.setDictAuto()
        self.configCombox()
        self.setModelView()
        self.disableAmostras()
        self.CHBActividade.stateChanged.connect(self.verfActiv_Pesqueira)
        self.PBAdicionar.clicked.connect(self.prep_toAdd)
        self.PBEditar.clicked.connect(self.prep_toEdit)
        self.PBGuardar.clicked.connect(self.save)
        self.PBPesquisar.clicked.connect(self.openSearch)
        self.PBAmostras.clicked.connect(self.open_Amostras)
        self.CBProvincia.currentIndexChanged.connect(self.configRegistador)  
        self.setClick()
        self.PBCancelar.clicked.connect(self.close)
        self.PBFoto.clicked.connect(self.addFichaScan)
    
        
    def setClick(self):
        lstWdgInsert = [self.PBArtes, self.PBSaidasObs]
        lstWdgUpdadte = [self.PBEditarArtes, self.PBEditarSaidasObs]
        lstViews = [self.TVArtesAmost, self.TVSaidasObservacoes]
        
        for val in lstViews:
            val.clicked.connect(self.viewClicked)
        for val in lstWdgInsert:
            val.clicked.connect(self.prep_toInseret_POP)  
        for val in lstWdgUpdadte:
            val.clicked.connect(self.prep_toEdit_POP)
            
            
    def addFichaScan(self):
        #Verificar se existem os Dados na Base de dados
        idx = self.LEN_Sequencial.text()
        data = rscForm.getText(self.DEDataAmost)
        centroPesca = rscForm.getText(self.CBCentroPesca)
        registadores = rscForm.getText(self.CBRegistadores)
        quer = "select case when (select True where {id} in (select id from t_saidas)) then True else False end".format(id=idx)
        bOK, resultOut = FuncSQL.anySelectScript(quer)
        if bOK:
            if resultOut[0] == True:
                frmFoto = frm_imageToPDF.frmImageToPdf(codigo=idx, 
                                                       data=data, 
                                                       centroPesca=centroPesca, 
                                                       registadores=registadores)
                frmFoto.exec_()
                
            else:
                QT_msg.aviso(txt="O Registo a inda nao foi inserido na Base de Dados.")
            

            
    def setDicts(self):
        self.dictFields= {
                        'fldName': ["id", "data_amostragem", "id_centro", "id_registrador",
                                    "hora_inicioamo", "hor_fimamo", "id_diasemana", "id_forcavento",
                                    "id_estadomare", "id_direccao", "hora_vento", "id_tipomare",
                                    "altura_preamar", "hora_preamar", "altura_baimar", "hora_baixamar", 
                                    "id_faselua", "id_nebulosidade", "hora_nebulosidade", "actividade_pesq", 
                                    "total_artes_amos", "total_artes_act", "total_artes_n_activas", "total_artes_prov_outo_cent", 
                                    "observacoes"],
                          
                        'objName': ["id", "DEDataAmost", "CBCentroPesca", "CBRegistadores",
                                    "TEInicioAmost", "TEFimAmost", "CBDiaSemana", "CBForca",
                                    "CBNivelMare", "CBDireccao", "TEHoraVent", "CBTipoMare",
                                    "DSBPreaiaMar", "TEPreiamarHora", "DSBBaixaMar", "TEBaixamarHora", 
                                    "CBFaselua", "CBNebulosidade", "TENebulosidadeHora", "CHBActividade", 
                                    "SBAmostras", "SBActivas", "SBNaoActivas", "SBOutrosCentros", 
                                    "PTEObservacao"],
                          
                        'fldWidget': [self.LEN_Sequencial, self.DEDataAmost, self.CBCentroPesca, self.CBRegistadores, 
                                      self.TEInicioAmost, self.TEFimAmost, self.CBDiaSemana, self.CBForca, 
                                      self.CBNivelMare, self.CBDireccao, self.TEHoraVent, self.CBTipoMare, 
                                      self.DSBPreaiaMar, self.TEPreiamarHora, self.DSBBaixaMar, self.TEBaixamarHora,
                                      self.CBFaselua, self.CBNebulosidade, self.TENebulosidadeHora, self.CHBActividade,
                                      self.SBAmostras, self.SBActivas, self.SBNaoActivas, self.SBOutrosCentros, 
                                      self.PTEObservacao],
                        
                        'isRel': [False, False, True, True, 
                                   False, False, True, True, 
                                   True,  True,  False, True, 
                                   False, False, False, False,
                                   True, True, False, False,
                                   False, False, False, False,
                                   False ],
                                    
                        'fldToQuote': [False, True, True, True, 
                                       True, True, True, True,
                                       True, True, True,True, 
                                       True, True, True, True,
                                       True, True, True, False,
                                       False, False, False, False,
                                       True ],
                          
                        'toDefault': [False, True, True, True, 
                                       True, True, True, True,
                                       True, True, True,True, 
                                       True, True, True, True,
                                       True, True, True, False,
                                       False, False, False, False,
                                       True ],
                          
                        'toCheck': [False, True, False, False, 
                                   True, True, False, False, 
                                   False, False, True, False, 
                                   True, True, True, True,
                                   False, False, True, False,
                                   True, True, True, True,
                                   False ],
                          
                        'toTurnOff': [False, True, True, True, 
                                   True, True, True, True, 
                                   True, True, True, True, 
                                   True, True, True, True,
                                   True, True, True, False,
                                   True, True, True, True,
                                   True ]
                                    }
        
        self.dictCB= {
                        'quer':["select null as id, '-Dia da Semana-' as nome union all select id, nome from ref_diasemana where activo = true;",
                                "select null as id, '-Dir. Vento-' as nome union all select id, nome from ref_table where id_grupo = 'DDV' and activo =true;",
                                "select null as id, '-Nivel da Mare-' as nome union all select id, nome from ref_table where id_grupo = 'NVM' and activo =true;",
                                "select null as id, '-Fase da Lua-' as nome union all select id, nome from ref_table where id_grupo = 'FLD' and activo =true;",
                                "select null as id, '-Forca do Vento-' as nome union all select id, nome from ref_table where id_grupo = 'FCV' and activo =true;",
                                "select null as id, '-Nebulosidade-' as nome union all select id, nome from ref_table where id_grupo = 'NBL' and activo =true;",
                                "select null as id, '-Registador-' as nome union all select id, nome from ref_table where id_grupo = 'RGT' and activo =true;",
                                "select null as id, '-Tipo de Mare-' as nome union all select id, nome from ref_table where id_grupo = 'TPM' and activo =true;"],
                        
                        'widget':[self.CBDiaSemana, self.CBDireccao, self.CBNivelMare, self.CBFaselua, 
                                  self.CBForca, self.CBNebulosidade, self.CBRegistadores, self.CBTipoMare]
                      }
        
        self.lstActividade  = [self.SBActivas, self.SBAmostras]
        
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

        
        self.dictDlgFactores={
                        "names": ["id", "id_saida", "id_factore", "comentario"],
                        "toQuote":[False, False, True, True],
                        "relTblName":[None, None, "ref_table", None],
                        "val2Rel":[None, None, ["id", "nome"], None],
                        "newNames":["ID", "ID DA SAIDAS", "FACTORES", "COMENTARIOS"],  
                        "toHide":[True, True, False, False],
                        'sizeCol':[0, 0, 200, 150]
                            }
        
        
        self.dictDlgArtesAmostradas={
                        "names": ["id", "id_saida", "id_centro", "id_tip_uni_pesca", "n_activas", "n_nao_activas", "n_amostradas"],
                        "toQuote":[False, False, True, True, False, False, False],
                        "relTblName":[None, None, "ref_geometric", "ref_unidpescatipo", None, None],
                        "val2Rel":[None, None, ["id", "nome"] ,["id", "nome"]  ,None ,None],
                        "newNames":["ID", "ID DA SAIDAS", "CENTROS", "ARTES", "ACTIVAS", "NAO ACTIVAS", "AMOSTRDAS"],    
                        "toHide":[True, True, False, False,False, False, False],
                        'sizeCol':[0,0,150,150,90,90,90]
                            }

    def setMainDict(self):
        '''
        Dicionario Para Ajudar, a descobrir quem e que mandou o evento, 
        para os views das saidas observacoes ou actividades de Pesca
        '''
        self.dictMainWidg = {
                            'PBSaidasObs':0,
                            'TVSaidasObservacoes':0,
                            'PBEditarSaidasObs': 0,
                            
                            'PBArtes':1,
                            'TVArtesAmost':1,
                            'PBEditarArtes':1,
                            }
        
    
    def setDictAuto(self):
        '''
        Dicionario com os Dados das saidas observacoes ou actividades de Pesca
        '''
        self.dictView={
            'MainDict': [self.dictDlgFactores, self.dictDlgArtesAmostradas], 
    
            'tblName':  ["t_saidas_factores_externos", "t_activ_tip_unidade"],
    
            'tblView': [self.TVSaidasObservacoes, self.TVArtesAmost], 
            
            'dialogsToOpen': [dialog_Factores, dialog_ArtesAmostradas],
            
            'filtro': ["id_saida ={id}", "id_saida ={id}"],
            
            'lastClicked': [None, None]
                    }    
        
    #===========================================================================