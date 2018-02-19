'''
Created on 10/08/2017

@author: chernomirdinmacuvele
'''
from ui_tableas_POT import Ui_Form
from PyQt5.Qt import QModelIndex
from  GenericReferenciasQDialog import GenericReferencias_

class dlg_tabela(GenericReferencias_, Ui_Form):
    def __init__(self, parent = None, dbcon=None, tblName=None, indexModel=None, idx=None, level=None):
        super(dlg_tabela, self).__init__(parent=None)
        self.setupUi(self)
        
        self.tblName = tblName
        self.curText = idx        
        self.mIdx = indexModel
        self.setDict()
        self.configCombox()
        self._setSame()
        self.toEdit()
        self._toEdit()
        self.bOK = (False, None)
        
        self.level = level
        self.justView()
        
        self.PBGuardar.clicked.connect(self.pre_operacao)
        self.PBCancelar.clicked.connect(self.close)
    
        
    def _toEdit(self):
        if isinstance(self.mIdx, QModelIndex):
            self.splitInID()
        else:
            self.setIDFromCB(widget=self.CBGrupos)
        self.LECodigo.setMaxLength(3)
            
                
    def _setSame(self):
        self.CBGrupos.setCurrentText(self.curText)
      
      
    def setDict(self):
        ''' 
        Metodo para configurar os dicionarios 
        '''    
        self.dictFields= {
                        'lstName': ["id", "id_grupo", "nome", "descricao", "comentario", "activo"],
                        'lstToQuote': [True, True, True, True, True, False],
                        'lstWidget': [self.LECodigo, self.CBGrupos, self.LENome, self.PTEDescricao, self.PTEComentarios, self.CHBActivo],
                        'lstRel': [False, True, False, False, False, False],
                        'lstDefault':[False, False, False, True, True, True],
                        'lstUpercase':[True, False, False, False, False, False]
                         }
        
        self.dictCB= {
                'quer':["select null as id, '-Seleciona o Grupo-' union all select id, nome from ref_grupo"],                      
                'widget':[self.CBGrupos]
                       }