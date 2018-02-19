'''
Created on 18/09/2017

@author: chernomirdinmacuvele
'''
from ui_pesqueiros_POT import Ui_Form
import rscForm as formHelper
from PyQt5.Qt import QModelIndex
import FuncSQL
from GenericReferenciasQDialog import GenericReferencias

class dlg_pesqueiros(GenericReferencias, Ui_Form):
    def __init__(self, parent = None, dbcon=None, tblName=None, indexModel=None, idx=None, level=None):
        super(dlg_pesqueiros, self).__init__(parent)
        self.setupUi(self)   
        
        self.tblName = tblName
        self.mIdx = indexModel
        self.setDict()
        self.configCombox()
        self.toEdit()
        self._toEdit()
        self.bOK = (False, None)
        
        self.level = level
        self.justView()
        
        self.PBGuardar.clicked.connect(self.pre_operacao)
        self.PBCancelar.clicked.connect(self.close)
            
            
    def _toEdit(self):
        if isinstance(self.mIdx, QModelIndex):
            indexModel = self.mIdx
            lstwidgt = self.dictFields['lstWidget']
            formHelper.setClicked2Widget(indexModel, lstwidgt) 
        else:
            bOK, last = FuncSQL.getLast(tblName='ref_pesqueiro', val='id')
            if bOK:
                idx = int(last) + 1
                self.LECodigo.setText(str(idx))


    def setDict(self):
        self.dictFields= {
                        'lstName': ["id", "id_centro", "nome", "comentario", "activo"],
                        'lstToQuote': [False, True, True, True, False],
                        'lstWidget': [self.LECodigo, self.CBProvincia, self.LENome, self.PTEComentarios, self.CHBActivo],
                        'lstRel': [False, True, False, False, False],
                        'lstDefault':[False, False, False, True, False],
                        'lstUpercase':[False, False, True, False, False]
                        }
        
        self.dictCB= {
                        'quer':["select null as id, '-Provincia-' as nome union all select id, nome from ref_geometric where id_tiplocal = 'PRV' and activo = true;"],
                        
                        'widget':[self.CBProvincia]
                      }