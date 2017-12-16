'''
Created on 24/11/2017

@author: chernomirdinmacuvele
'''

from ui_CalculoEstim import Ui_FrmCalculoEst
import mixedModel
import GenericCalculoEstim
import QT_msg
from PyQt5.Qt import QTableView, QRadioButton

class frmCalculoEstim (GenericCalculoEstim.GenericCalculoEstim, Ui_FrmCalculoEst):
    def __init__(self, parent=None, tblName=None, DbCon=None):
        super(frmCalculoEstim, self).__init__(parent)
        
        self.setupUi(self)
        
        self.dbcon = DbCon
        self.tblName = tblName
        self.mModel = mixedModel
        self.setMainDict()
        self.arteClicked = None
        self.categoriaClicked = None
        self.textHintAll()
        self.onChangePeriodo_Ano()
        self.onChangePeriodo_Mes()
        self.setCB()
        self.configButtons()
        self.setTView()
        self.CBAgrupamento.currentIndexChanged.connect(self.calAgrupamento)
        self.PBCalcular.clicked.connect(self.getAllToCalculo)
        self.onClickTView()
    
    
    def onClickTView(self):
        lstTView  = [self.TViewArtes, self.TViewCategorias]
        for idx, val in enumerate(lstTView):
            val.clicked.connect(self.clickedTView)
    
    def clickedTView(self, mIdx):
        if self.sender().objectName() == self.TViewArtes.objectName():
            self.arteClicked = mIdx
        else:
            self.categoriaClicked = mIdx
            
    
    def configButtons(self):
        lstWdget= [self.TBEspecies, self.TBSexo]
        for val in lstWdget:
            val.clicked.connect(self.openToSearch)  

    def onChangePeriodo_Ano(self):
        lstWdget = [self.CBAno_inicio, self.CBAno_Fim]
        for val in lstWdget:
            val.currentIndexChanged.connect(self.getVal_Combox)
            
        
    def onChangePeriodo_Mes(self):
        lstWdget = [self.CBAno_inicio, self.CBMes_inicio]
        for val in lstWdget:
            val.currentIndexChanged.connect(self.setAgruToDefault)
        
                
    def textHintAll(self):
        lstWdg= [self.CBAno_inicio, self.CBAno_Fim, self.CBMes_inicio, self.CBMes_Fim,
                 self.CBAgrupamento, self.CBPeriodoDia, self.CBTipDia, self.CBEstratificacao,
                 self.CBEspecie, self.CBSexo]
        for wdg in lstWdg:
            self.CBTextHint(Combox=wdg)
        
    
    def calAgrupamento(self):
        agrupamento = mixedModel.getDataCombox(self.CBAgrupamento)
        start_month = mixedModel.getDataCombox(self.CBMes_inicio)
        start_year = mixedModel.getDataCombox(self.CBAno_inicio)
        if agrupamento > 0 and start_month is not '' and start_month is not 'NULL':
            mes = int(start_month) + agrupamento
            mes -= 1 
            if mes > 12:
                newMes = mes - 12 
                newAno = int(start_year) +1
                self.CBAno_Fim.setCurrentText(str(newAno))
                self.CBMes_Fim.setCurrentIndex(newMes)
                if self.CBMes_Fim.currentText() is '':
                    QT_msg.aviso(txt="Nao e possivel agrupar os Dados "+str(self.CBAgrupamento.currentText())+"mente porfavor tente outro tipo de agrupamento. Porque nao existem dados suficientes.")
                    self.CBMes_Fim.setCurrentIndex(0)
            elif mes <= 12:
                self.CBAno_Fim.setCurrentIndex(self.CBAno_inicio.currentIndex())
                self.CBMes_Fim.setCurrentIndex(mes)
                if self.CBMes_Fim.currentText() is '':
                    QT_msg.aviso(txt="Nao e possivel agrupar os Dados "+str(self.CBAgrupamento.currentText())+"mente porfavor tente outro tipo de agrupamento. Porque nao existem dados suficientes.")
                    self.CBMes_Fim.setCurrentIndex(0)
    
    
    def setMainDict(self):
        self.dictTblView =  {
                            'lstquer' : ["select null as id, 'Nenhuma Arte' as Nome union all SELECT id, nome FROM public.ref_unidpescatipo;",
                                        "select null as id, 'Nenhuma Categoria' as Nome union all SELECT id, nome FROM public.ref_table where id_grupo = 'CAT'"],
                            'lstView' : [self.TViewArtes, self.TViewCategorias],
                            'size' : [[0,250], [0,150]],
                            'toHide':[[True, False], [True, False]]
                            }
        
        self.dictQuery= {
                        'ano_inicio': [],
                        'mes_inicio': [],
                        'ano_fim': [],
                        'mes_fim': [],
                        'agrupamento': [],
                        'periodo_dia': [],
                        'tipo_dia': [],
                        'artes': [],
                        'estimativa': [],
                        'categorias': [],
                        'especies': [],
                        'sexo': [],
                        'max_cm': [],
                        'min_cm': [],
                        'estatificacao': [],
                        }
