'''
Created on 14/07/2017
@author: chernomirdinmacuvele
'''
#Imports

from PyQt5.Qt import QDesktopWidget, QMenuBar
from PyQt5.QtWidgets import QMainWindow
from ui_main import Ui_MainWindow
from dlg_MenuTypes import dlg_MenuTypes
import frmFichaRecolhaParte1
import Rules
from frmCalculoEstim import frmCalculoEstim
from datetime import datetime
import frm_config_user
import rscForm
import RelatoriosGerais
from Relatorio_SaidasPorProvinica import Relatorio_SaidasPorProvincia
import File_config
from frm_EstroturaHierarquia import frmEstroturaHierarquia


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
        
        self.menubar.setNativeMenuBar(True)
        '''    
                            Connections    
        Aqui chamamos a connecao para a base de Dados Pescart 
        '''
        self.dbPescArt = dbCon
        self.user_info = user_info#id, Nome, level
        self.configTblNames()        
        self.configRules()
        self.configUser()
        tempo = datetime.today()
        rscForm.configprivilege(dictIn=self.dictToHide)
        
        """
                            triggeres        
        Este e o block dos eventos como:
            - triggered -> quando um elemento no menubar e selecionado o evento triggered e activado.
        """
        self.actionTabelas_de_Referencia.triggered.connect(self._openMenuRef)
        self.actionFicha_de_Recolha_de_Dados.triggered.connect(self._openFichaRecolha)
        self.actionCalculo_das_Estimativas.triggered.connect(self._openEstimativas)
        self.actionRegistar.triggered.connect(self._openConfigUser)
        self.actionRelatorios_Gerais.triggered.connect(self._openGenerateReports)
        self.actionTotal_das_Saidas_Registadas_Por_Provincia.triggered.connect(self._openRelatoriosEspecificos)
        self.actionHierarquiaDoPais.triggered.connect(self._openHierarquiaPais)

    
    '''
    Metodos Para abrir Forms/Janelas 
    '''
    def _openHierarquiaPais(self):
        '''
        Hierarquia do Pais.
        '''
        self.Estrotura = frmEstroturaHierarquia(dbcon = self.dbPescArt)
        self.Estrotura.exec_()
    
    
    def _openMenuRef(self):
        '''
        Menu das referencias.
        '''
        self.menuBar = dlg_MenuTypes(dbcon=self.dbPescArt,user_info=self.user_info)
        self.menuBar.exec_()


    def _openFichaRecolha(self):
        '''
        Ficha de recolha de Dados.
        '''
        self.Ficha = frmFichaRecolhaParte1.FichaRecolha(dbcon = self.dbPescArt, dictTblName=self.dictTblNames, dictRules=self.dictRules)
        self.Ficha.exec_()
    
    
    def _openEstimativas(self):
        '''
        Processamento de Dados
        '''
        tblName = "NUMB"
        self.CalEstim = frmCalculoEstim(DbCon=self.dbPescArt)
        self.CalEstim.exec_()
        
     
    def _openConfigUser(self):
        tblName = "log_user"
        self.User = frm_config_user.user_config(dbcon=self.dbPescArt, tblName=tblName, user_info=self.user_info)
        self.User.exec_()
        
        
    def _openGenerateReports(self):
        self.Rep = RelatoriosGerais.GenerateReports(dbcon=self.dbPescArt)
        self.Rep.exec_()
        
    
    def _openRelatoriosEspecificos(self):
        self.RepEsp = Relatorio_SaidasPorProvincia(dbcon=self.dbPescArt)
        self.RepEsp.exec_()
    
    
    def makeMainFull(self):
        width = int(File_config.configDict['screenWidth'])
        hight = int(File_config.configDict['screenHight'])
        self.setMaximumHeight(hight)
        self.setMaximumWidth(width)
        
        
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
        self.dictToHide=   {
                            'menus':[self.actionTabelas_de_Referencia],
                            'level':[0]
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
        
        