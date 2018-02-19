'''
Created on 17/08/2017

@author: chernomirdinmacuvele
'''
from ui_artes_POT import Ui_Dialog
from GenericReferenciasQDialog import GenericReferencias

class dlg_artes(GenericReferencias,Ui_Dialog):
    def __init__(self, parent = None, dbcon=None, tblName=None, indexModel=None, idx=None, level=None):
        super(dlg_artes, self).__init__(parent=None)
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
        self.dictFields= {
                        'lstName': ["id", "nome", "id_uniesforco", "id_unitrabalho", "id_tippesca", "descricao", "comentario", "activo"],
                        'lstToQuote': [True, True, True, True, True, True, True,  False],
                        'lstWidget': [self.LECodigo, self.LENome, self.CBUniEsforco, self.CBuniTrablho, self.CBTipPesca, self.PTEDescricao, self.PTEComentarios,
                                      self.CHBActivo],
                        'lstRel': [False, False, True, True, True, False, False, False],
                        'lstDefault':[False, False, False,False, False, True, True, True],
                        'lstUpercase':[True, False, False, False, False, False, False, False]
                         }

        self.dictCB= {
                        'quer':["select null as id, '-Unidade de Esforco-' as nome union all select id, nome from ref_table where id_grupo = 'UNE' and activo = true;",
                                "select null as id, '-Unidade de Trabalho-' as nome union all select id, nome from ref_table where id_grupo = 'UNT' and activo = true;",
                                "select null as id, '-Tipo de Pesca-' as nome union all select id, nome from ref_table where id_grupo = 'TPE' and activo = true;"],
                        
                        'widget':[self.CBUniEsforco, self.CBuniTrablho, self.CBTipPesca],
                      }