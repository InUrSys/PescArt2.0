'''
Created on 17/08/2017

@author: chernomirdinmacuvele
'''
from ui_IntClass_POT import Ui_Form
import rscForm as formHelper
from GenericReferenciasQDialog import GenericReferencias
from PyQt5.Qt import  QModelIndex
import FuncSQL

class dlg_intClass(GenericReferencias,Ui_Form):
    def __init__(self, parent = None, dbcon=None, tblName=None,  indexModel=None, id=None):
        super(dlg_intClass, self).__init__(parent=None)
        self.setupUi(self)
        
        self.tblName = tblName
        self.mIdx = indexModel
        self.setDict()
        self.configCombox()
        self._toEdit()
        self.bOK = (False, None)
        self.PBGuardar.clicked.connect(self.pre_operacao)
        self.PBCancelar.clicked.connect(self.close)

        
    def _toEdit(self):
        if isinstance(self.mIdx, QModelIndex):
            indexModel = self.mIdx
            lstwidgt = self.dictFields['lstWidget']
            formHelper.setClicked2Widget(indexModel, lstwidgt) 
        else:
            bOK, last = FuncSQL.getLast(tblName='ref_intervalo_class' , val='id')
            if bOK:
                idx = int(last) + 1
                self.LECodigo.setText(str(idx))
          
        
    def setDict(self):
        self.dictFields=    {
                            'lstName': ["id","id_especie", "intervalo", "comentario", "activo"],
                            'lstToQuote': [False, True, True, True, True,],
                            'lstWidget': [self.LECodigo, self.CBEspecies, self.DBSIntervalo, self.PTEComentarios, self.CHBActivo],
                            'lstRel': [False, True, False, False, False],
                            'lstDefault':[False, False, False, True, True],
                            'lstUpercase':[False, False, False, False, False]
                            }
        
        self.dictCB= {
                'quer':["select null as id, '-Selecione a Especie-' union all select id, nome from ref_especies"],                      
                'widget':[self.CBEspecies]
                       }