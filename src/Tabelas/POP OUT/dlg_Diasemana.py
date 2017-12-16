'''
Created on 17/08/2017

@author: chernomirdinmacuvele
'''
from ui_diasemana_POT import Ui_Form
from GenericReferenciasQDialog import GenericReferencias

class dlg_diasemana(GenericReferencias,Ui_Form):
    def __init__(self, parent = None, dbcon=None, tblName=None,  indexModel=None, id=None):
        super(dlg_diasemana, self).__init__(parent=None)
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
                            'lstName': ["id", "id_tipdia",  "nome",  "descricao", "comentario", "activo"],
                            'lstToQuote': [True, True, True, True, True,  False],
                            'lstWidget': [self.LECodigo, self.CBTipDia, self.LENome, self.PTEDescricao, self.PTEComentarios, self.CHBActivo],
                            'lstRel': [False, True, False, False, False, False],
                            'lstDefault':[False, False, False, True, True, True],
                            'lstUpercase':[True, False, False, False, False, False]
                            }
        
        self.dictCB=        {
                            'quer':["select null as id, '-Tipo de dia-' as nome union all select id, nome from ref_table where id_grupo = 'TPD' and activo = true;"],    
                                              
                            'widget':[self.CBTipDia]
                                   }