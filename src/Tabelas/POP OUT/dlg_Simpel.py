'''
Created on 18/09/2017

@author: chernomirdinmacuvele
'''
from ui_codificadores_POT import Ui_Form
from GenericReferenciasQDialog import GenericReferencias

class dlg_simpel(GenericReferencias, Ui_Form):
    def __init__(self, parent = None, dbcon=None, tblName=None, indexModel=None, id=None):
        super(dlg_simpel, self).__init__(parent)
        self.setupUi(self)   
        
        self.tblName = tblName
        self.mIdx = indexModel
        self.setLst()
        self.lockCodigo_Grupo()
        self.bOK = (False, None)
        self.PBGuardar.clicked.connect(self.pre_operacao)
        self.PBCancelar.clicked.connect(self.close)
        
        
    def lockCodigo_Grupo(self):
        if self.tblName == 'ref_grupo':
            if self.mIdx is not None:
                self.LECodigo.setReadOnly(True)
        self.toEdit()


    def setLst(self):
        self.dictFields= {
                            'lstName': ["id", "nome","descricao", "comentario", "activo"],
                            'lstToQuote': [True, True, True, True, False],
                            'lstWidget': [self.LECodigo, self.LENome, self.PTEDescricao, self.PTEComentarios, self.CHBActivo],
                            'lstRel': [False, False, False, False, False],
                            'lstDefault':[False, False, True, True, True],
                            'lstUpercase':[True, False, False, False, False]
                        }