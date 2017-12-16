'''
Created on 17/08/2017

@author: chernomirdinmacuvele
'''
from ui_geometric_POT import Ui_Form
import Sub_GenericReferencias

class dlg_geometric(Sub_GenericReferencias.sub_GenericReferencias_Geometric,Ui_Form):
    def __init__(self, parent = None, dbcon=None, tblName=None, indexModel=None, id=None):
        super(dlg_geometric, self).__init__(parent=None)
        self.setupUi(self)
        
        self.tblName = tblName
        self.mIdx = indexModel
        self.setDict()
        self.configCombox()
        self.setIDFromCB()
        self.bOK = (False, None)
        self.PBGuardar.clicked.connect(self.pre_operacao)
        self.PBCancelar.clicked.connect(self.close)
        self.CBTipLocal.currentIndexChanged.connect(self.setIDFromCB)
        self.toEdit()
        
        
    def setDict(self):
        self.dictFields= {
                        'lstName': ["id", "id_tiplocal", "id_parent" , "nome",  "descricao", "comentario", "activo"],
                        'lstToQuote': [True, True, True, True, True, True,  False],
                        'lstWidget': [self.LECodigo, self.CBTipLocal, self.CBCentroPesca, self.LENome, self.PTEDescricao, self.PTEComentarios,
                                    self.CHBActivo],
                        'lstRel': [False, True, True, False, False, False, False],
                        'lstDefault':[False, False, False, False, True, True, True],
                        'lstUpercase':[True, False, False, False, False, False, False]
                         }
        
        self.dictCB= {
                'quer':["select null as id, '-Tipo de Local-' as nome  union all (SELECT id, nome from ref_tiplocal order by id_nivel);",
                        "SELECT id, nome from ref_geometric where id_tiplocal = 'PIS';",
                        "select null as id, '-Provincia-' as nome",
                        "select null as id, '-Distrito-' as nome",
                        "select null as id, '-Posto Administrativo-' as nome",
                        "select null as id, '-Centros Existentes-' as nome"],
                                         
                'widget':[self.CBTipLocal, self.CBPais, self.CBProvincia, self.CBDistrito, self.CBPostoAdmin, self.CBCentroPesca]
                       }