'''
Created on 15/08/2017

@author: chernomirdinmacuvele
'''
from ui_tipLocal_POT import Ui_Form
from GenericReferenciasQDialog import GenericReferencias

class dlg_tiplocal(GenericReferencias,Ui_Form):
    def __init__(self, parent = None, dbcon=None, tblName=None, indexModel=None, id=None):
        super(dlg_tiplocal, self).__init__(parent=None)
        self.setupUi(self)
        
        self.tblName = tblName
        self.mIdx = indexModel
        self.setDict()
        self.configCombox()
        self.toEdit()
        self.bOK = (False, None)
        self.PBGuardar.clicked.connect(self.pre_operacao)
        self.PBCancelar.clicked.connect(self.close)
        
        
    def setDict(self):
        self.dictFields=    {
                            'lstName': ["id", "id_nivel",  "nome",  "descricao", "comentario", "activo"],
                            'lstToQuote': [True, True, True, True, True,  False],
                            'lstWidget': [self.LECodigo, self.CBNivel, self.LENome, self.PTEDescricao, self.PTEComentarios, self.CHBActivo],
                            'lstRel': [False, True, False, False, False, False],
                            'lstDefault':[False, False, False, True, True, True],
                            'lstUpercase':[True, False, False, False, False, False]
                            }
        
        self.dictCB= {
                'quer':["select null as id, '-Selecione o Nivel-' union all select id, nome from ref_nivel"],                      
                'widget':[self.CBNivel]
                       }