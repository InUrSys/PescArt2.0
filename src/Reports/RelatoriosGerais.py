'''
Created on 30/01/2018

@author: chernomirdinmacuvele
'''
from ui_GenerateReports import Ui_Form
import ReportAPI
import mixedModel
import QT_tblViewUtility
from PyQt5.Qt import QProgressBar

class GenerateReports(ReportAPI.JasperReports, Ui_Form):
    def __init__(self, parent=None, dbcon=None):
        super(GenerateReports, self).__init__(parent)
        self.setupUi(self)
        
        self.configSets()
        
    def configSets(self):
        self.setWidgets()
        self.setDataInWdg()
        self.setModel()
        self.PBUp.clicked.connect(self.toDown)
        self.PBDown.clicked.connect(self.toUp)
        self.TVReports.clicked.connect(self.onTableClick)
        self.PBGerar.clicked.connect(self.GenerateReport)
        self.PBCancelar.clicked.connect(self.close)
        
        
    def setDataInWdg(self):
        self.CBFormato.addItems(self.lstWdgFormats)
    
    
    def setWidgets(self):
        self.lstWdgFormats = ['pdf','rtf','xls', 'xlsx', 'docx', 'odt', 'ods', 'pptx', 'csv', 'html', 'xhtml', 'xml','jrprint']
        
        
    def setModel(self):
        tblName = 'prc_relatorios'
        fldToMap = [self.LECod, self.LENome, self.PTEDescricao]
        fldSize = [50, 150,150]
        bOK, model = mixedModel.setViewModel(tblName= tblName, filtro='parametros = False')
        if bOK:
            QT_tblViewUtility.setModelInView(tblView= self.TVReports, ViewModel=model)
            QT_tblViewUtility.setViewCustom(tblView= self.TVReports, lstSizeCol=fldSize)
            mixedModel.withWidgets.setMapper(self, model=model, fldToMap= fldToMap)
            
    
    def onTableClick(self, mIdx):
        _,idx = QT_tblViewUtility.getClicked(indexModel= mIdx)
        mixedModel.withWidgets.setMapperToIdx(self, idx= idx)
           
        
    def toUp(self):
        mixedModel.withWidgets.mapperToNext(self)
    
    
    def toDown(self):
        mixedModel.withWidgets.mapperToPerv(self)
        
        
    def GenerateReport(self):
        file = self.LENome.text()
        formato = self.CBFormato.currentText()
        self.getTemplateFile(file=file, format=formato)
        
