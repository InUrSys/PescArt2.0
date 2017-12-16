'''
Created on 14/07/2017
@author: chernomirdinmacuvele
'''
#Imports

from PyQt5.Qt import QApplication, QDesktopWidget
from PyQt5.QtWidgets import QMainWindow
from ui_main import Ui_MainWindow
from dlg_MenuTypes import dlg_MenuTypes
import frmFichaRecolhaParte1
import Rules
import WhatLog
from frmCalculoEstim import frmCalculoEstim
from datetime import datetime
import frm_config_user
import rscForm
from dialog_PesquisarSaidas import PesquisarSaidas


class frmMain(QMainWindow,Ui_MainWindow):
    '''
    Classe, para tratar dos metodos da main form, fornecendo os paramentros bases para 
    abrir ou manusear os dados.
    '''
    def __init__(self, parent=None, dbCon=None, user_info = None):
        super(frmMain,self).__init__(parent=parent)
        self.setupUi(self)
        
       
        #Para deixar Com o estilo Diferente
        self.makeMainFull()
        self.showCentered()
        
        '''    
                            Connections    
        Aqui chamamos a connecao para a base de Dados Pescart 
        '''
        self.dbPescArt = dbCon
        self.user_info = user_info
        self.configTblNames()        
        self.configRules()
        self.configUser()
        tempo = datetime.today()
        rscForm.configprivilege(dictIn=self.dictToHide)
        WhatLog.logIN(user=self.user_info, tempox=tempo)
        
        """
                            triggeres        
        Este e o block dos eventos como:
            - triggered -> quando um elemento no menubar e selecionado o evento triggered e activado.
        """
        self.actionTabelas_de_Referencia.triggered.connect(self._openMenuRef)
        self.actionFicha_de_Recolha_de_Dados.triggered.connect(self._openFichaRecolha)
        self.actionCalculo_das_Estimativas.triggered.connect(self._openEstimativas)
        self.actionRegistar.triggered.connect(self._openConfigUser)
        self.actionAdicionar_Composicao_Especifica.triggered.connect(self._openPesquisar)

    
    def _openMenuRef(self):
        '''
        Metodo para abrir o Menu das referencias.
        '''
        self.menuBar = dlg_MenuTypes(dbcon=self.dbPescArt)
        self.menuBar.exec_()


    def _openFichaRecolha(self):
        '''
        Metodo para abrir o A Ficha de recolha de Dados.
        '''
        self.Ficha = frmFichaRecolhaParte1.FichaRecolha(dbcon = self.dbPescArt, dictTblName=self.dictTblNames, dictRules=self.dictRules)
        self.Ficha.exec_()
    
    def _openEstimativas(self):
        tblName = "NUMB"
        self.CalEstim = frmCalculoEstim(DbCon=self.dbPescArt)
        self.CalEstim.exec_()
     
    def _openConfigUser(self):
        tblName = "log_user"
        self.User = frm_config_user.user_config(dbcon=self.dbPescArt, tblName=tblName, user_info=self.user_info)
        self.User.exec_()
        
    #Note This Is just For Delevopment porpess
    def _openPesquisar(self):
        self.Pesq = PesquisarSaidas(dbcon=self.dbPescArt)
        self.Pesq.exec_()
    
    def makeMainFull(self):
        size = QApplication.desktop()
        h = size.frameSize().height()
        w = size.frameSize().width()
        self.setGeometry(0,0,h,w)
        
        
    def showCentered(self):
        rectSpe = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        rectSpe.moveCenter(centerPoint)
        self.move(rectSpe.topLeft())
        
        
    def configRules(self):
        self.dictRules = {}
        bok_w, matWdgt = Rules.getRules_Wdgt()
        bok_f, matfrm = Rules.getRules_Frm()
        if bok_w is True and bok_f is True:
            matfrm= Rules.splitObjectName(matxIn= matfrm)
            matOut = (matWdgt+matfrm)
            Rules.exeBuidAndFill(mainDict=self.dictRules, matxOut=matOut,  matxWdgt=matWdgt, matxFrm=matfrm)
            
    
    def configUser(self):
        self.dictToHide= {
                            'menus':[self.actionTabelas_de_Referencia],
                            'level':[50]
                            }
        
        
    def configTblNames(self):
        '''
                        Data base Tables   
        Neste Block encotramos os dicionarios com os nomes das tabelas,
        que sera usado para abrir os forms correspondetes a cada tabela.
            - dictTablNames -> dicionarios com os nomes das tabelas da Base de Dados pescart
                        
        '''
        self.dictTblNames = {
                            "Grupo": "ref_grupo",
                            "Table": "ref_table",
                            "Especies": "ref_especies",
                            "Nivel": "ref_nivel",
                            "Tiplocal": "ref_tiplocal",
                            "Artes": "ref_Artes",
                            "Diasemana": "ref_diasemana",
                            "Geometric": "ref_geometric",
                            "Motor": "aux_motor",
                            "Unipesca": "aux_unipesca",
                            "Saidas": "t_saidas",
                            "ArtesOutCentros":"t_arte_outros_centros",
                            "SaidasFactores": "t_saidas_factores_externos",
                            "ArtePesca":"t_activ_tip_unidade",
                            "ViagemPesca":"t_viagem_pesca",
                            "LancePesca":"t_lance_pesca",
                            "CatComercial":"t_categoria_comercial",
                            "AmostCat":"t_amost_cat",
                            "AmostEspe":"t_amost_espe",
                            "AmostEspEspe":"t_amost_amost_espe",
                            "AmostSexo":"t_amost_sexo",
                            "CompAmost":"t_comp_amost",
                            "FormNames":"ui_formnames",
                            "Form":"ui_form",
                            "Rules":"ui_rules",
                            "TypeRules":"ui_typerules",
                            }
        