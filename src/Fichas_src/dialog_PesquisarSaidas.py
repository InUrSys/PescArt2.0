'''
Created on 27/09/2017

@author: chernomirdinmacuvele
'''
from ui_PesquisarSaidas import Ui_Form
import GenericPesquisas
class PesquisarSaidas(GenericPesquisas.GenericPesquisas, Ui_Form):
    def __init__(self, parent=None, dbcon=None, tblName=None):
        super(PesquisarSaidas, self).__init__(parent)
        self.setupUi(self)
        
        self.tblName= tblName
        self.lstVal = None
        self.bOK= False
        self.configAndSets()
        
    
    def configAndSets(self):
        self.setDicts()
        self.configComboxLocal()
        self.configCombox()
        self.CBProvincia.currentIndexChanged.connect(self.configRegistador)
        self.PBPesquisar.clicked.connect(self.buldingTheQuery)
        self.TVSaidas.clicked.connect(self.selectedRow)
        self.PBOK.clicked.connect(self.close)
    
    def setDicts(self):
        self.dictSaidas = { 
                            'fldName' : ["id", "data_amostragem", "id_centro", "id_registrador",
                                    "hora_inicioamo", "hor_fimamo", "id_diasemana", "id_forcavento",
                                    "id_estadomare", "id_direccao", "hora_vento", "id_tipomare",
                                    "altura_preamar", "hora_preamar", "altura_baimar", "hora_baixamar", 
                                    "id_faselua", "id_nebulosidade", "hora_nebulosidade", "actividade_pesq", 
                                    "total_artes_amos", "total_artes_act", "total_artes_n_activas", "total_artes_prov_outo_cent", 
                                    "observacoes"],
                           
                           'newNames': ["Cod.", "Data", "Centro", "Registador", "Inicio", "Fim","Dia da Semana","",""
                                        ,"","","","","","","","","","","Act.Pesq","","","","",""],
                           
                           'toHide': [False,False,False,False,False,False,False,True,True,True,
                                      True,True,True,True,True,True,True,True,True,False,True,True,
                                      True,True,True,],
                           
                           'sizeCol':[80, 100, 200, 200, 80,80,150,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0 ]
                           }
         
        self.dictCB = {'quer':["select null as id, '-Registador-' as nome union all select id, nome from ref_registador",
                               "select null as id, '-Dia da Semana-' as nome union all select id, nome from ref_diasemana",
                               """  select 'actividade_pesq = true or actividade_pesq = false' as id, 'Houveram e Nao houveram Actividades Pesqueiras' as nome union all 
                                    select 'actividade_pesq = true' as id, 'Houveram Actividades Pesqueiras' as nome union all
                                    select 'actividade_pesq = false' as id, 'Nao houveram Actividades Pesqueiras' as nome"""],
                       'widget':[self.CBRegistador, self.CBDiaSemana, self.CBActividadePesqueria]
                       
                       }
        
        
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