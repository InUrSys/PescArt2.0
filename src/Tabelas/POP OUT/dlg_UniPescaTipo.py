'''
Created on 17/08/2017

@author: chernomirdinmacuvele
'''
from ui_UniPescaTipo_POT import Ui_Dialog
from GenericReferenciasQDialog import GenericReferencias

class dlg_UniPescaTipo(GenericReferencias, Ui_Dialog):
    def __init__(self, parent = None, dbcon=None, tblName=None,  indexModel=None, idx=None, level=None):
        super(dlg_UniPescaTipo, self).__init__(parent=None)
        self.setupUi(self)
        
        self.tblName = tblName
        self.mIdx = indexModel
        self.setDict()
        self.configCombox()
        self.toEdit()
        self.bOK = (False, None)
        
        self.level = level
        self.justView()
        
        self.PBGuardar.clicked.connect(self.pre_operacao)
        self.PBCancelar.clicked.connect(self.close)

        
        
    def setDict(self):
        self.dictFields=    {
                            'lstName': ["id", "nome", "id_arte", "id_tipbarco", "activo", "descricao"],
                            'lstToQuote': [True, True, True, True, False, True],
                            'lstWidget': [self.LECodigo, self.LENome, self.CBArtes, self.CBTipBarco, self.CHBActivo, self.PTEDescricao],
                            'lstRel': [False, False, True, True, False, False],
                            'lstDefault':[False, False, False, False, False, True],
                            'lstUpercase':[True, False, False, False, False, False]
                            }
        #
        #
        self.dictCB= {
                'quer':["select null as id, '-Selecione o Tipo de barco-' union all (select id, nome from ref_table where id_grupo = 'TPB' order by nome)",
                        "select null as id, '-Selecione a Arte-' union all (select id, nome from ref_artes order by nome)"],                      
                'widget':[self.CBTipBarco, self.CBArtes]
                       }