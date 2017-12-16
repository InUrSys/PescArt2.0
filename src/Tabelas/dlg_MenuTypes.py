'''
Created on 18/09/2017

@author: chernomirdinmacuvele
'''
from frmMainRef import frmMainRef
from ui_MenuTypes import Ui_Form
from PyQt5.Qt import QDialog
import QT_msg
class dlg_MenuTypes(QDialog, Ui_Form):
    '''
    Esta class abre um Dialog onde permite que o usuario seleciona com que tabela de referencia ele vai querer
    trabalhar.
    0 - Codificadores
    1 - Artes
    2 - Dias da Semana
    3 - Especies
    4 - Geometric
    5 - Nivel
    6 - Tabelas outras
    7  -Tipo de Local
    '''
    def __init__(self, dbcon=None):
        super(dlg_MenuTypes, self).__init__()
        self.setupUi(self)
        
        self.dbcon = dbcon
        self.setDict()
        
        self.PBCodificadores.clicked.connect(self.getSenderID)
        self.PBArtes.clicked.connect(self.getSenderID)
        self.PBEspecies.clicked.connect(self.getSenderID)
        self.PBDiaSemana.clicked.connect(self.getSenderID)
        self.PBEspaco.clicked.connect(self.getSenderID)
        self.PBNivel.clicked.connect(self.getSenderID)
        self.PBTipLocal.clicked.connect(self.getSenderID)
        self.PBOutros.clicked.connect(self.getSenderID)
        self.PBTipUniPesca.clicked.connect(self.getSenderID)
        self.PBIntClass.clicked.connect(self.getSenderID)
        self.PBPesqueiros.clicked.connect(self.getSenderID)
        self.PBRegistadores.clicked.connect(self.getSenderID)
        
    
    def getSenderID(self):
        '''
        metodo que verifica que objecto mandou o sinal 
        e deacordo com nome do objecto trazemos o index e passamos 
        nos paramentos para abrir o proximo dialog.
        '''
        whois = self.sender().objectName()
        try:
            idx = self.dictWidgt[whois]
            toOpen = frmMainRef(dbCon=self.dbcon, mainIndex=idx)
            toOpen.exec_()
        except Exception:
            QT_msg.error(txt="Error ", verbTxt=str(Exception))
            
    
    def setDict(self):
        '''
        Metodo para configurar o dicionario que contem o index de cada pushButton.
        Com esse index poderemos abrir a proxima janela e vizualizar os dados de acordo com index fornecido
        '''
        self.dictWidgt= {
                        'PBCodificadores':0,
                        'PBArtes':1,
                        'PBEspecies':3,
                        'PBDiaSemana':2,
                        'PBEspaco':4,
                        'PBNivel':5,
                        'PBTipLocal':7,
                        'PBOutros':6,
                        'PBPesqueiros':8,
                        'PBRegistadores':9,
                        'PBTipUniPesca':10,
                        'PBIntClass':11
                        }