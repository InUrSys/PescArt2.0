'''
Created on 01/02/2018

@author: chernomirdinmacuvele
'''
import ReportAPI
from ui_Relatorio_SaidasPorProvincia import Ui_Form
import FuncSQL
from PyQt5.Qt import QPlainTextEdit, QComboBox

class Relatorio_SaidasPorProvincia(ReportAPI.JasperReports, Ui_Form):
    def __init__(self, parent=None, dbcon=None):
        super(Relatorio_SaidasPorProvincia, self).__init__(parent)
        self.setupUi(self)
        
        self.dbcon = dbcon
        self.relatorio = 'Saidas_Distrito'
        self.setForm()
        
        
    def setForm(self):
        self.LEFormato.setText(self.getFormat())
        self.getInfoReport()
        self.setProvincias()
        self.PBGerar.clicked.connect(self.generateReport)
        
        
    def getInfoReport(self):
        quer = "SELECT nome, descricao FROM public.prc_relatorios where nome = '{nome}'".format(nome = self.relatorio)
        bok, valOut = FuncSQL.anySelectScript(scpt= quer)
        if bok:
            self.LENome.setText(str(valOut[0]))
            self.PTEDescricao.setPlainText(str(valOut[1]))
    
    
    def setProvincias(self):
        quer = "select distinct provincia from view_saidas_provincias"
        lstOut = []
        bok, valOut = FuncSQL.multLineSelect(scpt=quer)
        if bok:
            for val in valOut:
                lstOut.append(val[0])
            self.CBProvincia.addItems(lstOut)
    
        
    def generateReport(self):
        file = self.LENome.text()
        formato = self.LEFormato.text().lower()
        provincia = [self.CBProvincia.currentText()]
        self.getTemplateFile(file=file, format=formato, parametro=provincia)