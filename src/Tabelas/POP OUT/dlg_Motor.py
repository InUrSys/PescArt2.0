'''
Created on 17/08/2017

@author: chernomirdinmacuvele
'''
from ui_motor_POT import Ui_Form
from GenericReferenciasQDialog import GenericReferencias

class dlg_motor(GenericReferencias,Ui_Form):
    def __init__(self, parent = None, dbcon=None, tblName=None, indexModel=None, id=None):
        super(dlg_motor, self).__init__(parent=None)
        self.setupUi(self)
        
        self.tblName = tblName
        self.mIdx = indexModel
        self.setDict()
        self.toEdit()
        self.bOK = (False, None)
        self.PBGuardar.clicked.connect(self.pre_operacao)
        self.PBCancelar.clicked.connect(self.close)
        
        
    def setDict(self):
        self.dictFields= {
                            'lstName': ["id", "marca", "model", "potencia", "ano", "tipo"],
                            'lstToQuote': [True, True, True, True, True, True],
                            'lstWidget': [self.TabMotor_LEN_Sequencial, self.TabMotor_LEMarca, self.TabMotor_LEModelo, self.TabMotor_LEPotencia, self.TabMotor_DEAno, self.TabMotor_LETipo ],
                            'lstRel': [False, False, False, False, False, False],
                            'lstDefault':[False, False, True, True, True, True],
                            'lstUpercase':[True, True, True, False, False, False]
                        }