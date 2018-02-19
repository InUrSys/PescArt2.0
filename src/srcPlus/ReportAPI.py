'''
Created on 30/01/2018

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QThread, pyqtSignal, QFileDialog
import File_config as Fcg
from pyjasper import jasperpy
import QT_msg
import datetime
import os
import File_config
import subprocess

class JasperReports(QDialog):
    
    MainDict = None
    
    def setPaths(self):
        self.MainDict = Fcg.configDict
        self.input_path = self.MainDict['in_report']
        self.output_path = self.MainDict['out_report'] 
    
    
    def getFormat(self):
        return 'PDF'


    def getTemplateFile(self, file=None, format=None, parametro={}):
        self.setPaths()
        
        self.file = file
        self.format = format
        path = self.MainDict['in_report']
        pathFile = Fcg.getReportTemplateFile(path= path, File= file)
        isValid = Fcg.isValidFile(pathFile= pathFile)
        out_format = [format]
        if isValid:
            if parametro == {}:
                self.process_parameter_DB(fileName= pathFile, output_format=out_format, parameter= parametro)
            else:
                lstChaves = self.listing_parameters(fileName= pathFile)
                for index, chave in enumerate(lstChaves):
                    parametroIn = {chave:parametro[index]}
                self.process_parameter_DB(fileName= pathFile, output_format=out_format, parameter= parametroIn)
        else:
            QT_msg.aviso(txt = 'Not valid '+ pathFile)
        
    
    def listing_parameters(self, fileName=None):
        input_file = fileName
        lstOut = []
        jasper = jasperpy.JasperPy()
        output = jasper.list_parameters(input_file)
        for val in output.keys():
            lstOut.append(val)
        return lstOut

    
    def process_parameter_DB(self, fileName=None, output_format=None, parameter=None):
        self.setPaths()
        
        self.output_format = output_format
        input_file = str(fileName)
        output = self.output_path
        jasper = jasperpy.JasperPy()
        out = jasper.process(input_file= input_file, 
                       output_file= output, 
                       format_list= output_format, 
                       parameters= parameter,
                       db_connection= self.MainDict,
                        locale='pt_BR'
                       )
        QT_msg.Sucessos(txt= "Relatorio criado com sucesso!")
        outPathFile = self.set_suffix_Date()
        self.openGenerated(file=outPathFile, path = output)
    
    
    def openGenerated(self, file=None, path=None):
        outPutFilePath = os.path.join(path, file)
        
        sop = File_config.configDict['sistema']
        if sop == 'Darwin':
            subprocess.Popen(['open', outPutFilePath])
        
        #==========================Quando for necessario=============================================
        # test = QFileDialog()
        # test.getOpenFileName(self, "Open File", path)
        #=======================================================================
        
       
        
        
    def set_suffix_Date(self, reportName=None):
        self.setPaths()
        
        outPath = self.MainDict['out_report']
        for fileName in os.listdir(outPath):
            if fileName.startswith(self.file) != False:
                newName = self.file + "_"+str(datetime.date.today())
                for xformat in self.output_format:
                    if os.path.isfile(self.output_path+'/'+self.file+'.'+xformat) != False:
                        n=0
                        if os.path.isfile(self.output_path+'/'+newName+'.'+xformat):
                            n+=1
                            if os.path.isfile(self.output_path+'/'+newName+'_'+str(n)+'.'+xformat) == True:
                                while os.path.isfile(self.output_path+'/'+newName+'_'+str(n)+'.'+xformat):
                                    n+=1
                            os.renames(self.output_path+'/'+self.file+'.'+xformat, self.output_path+'/'+newName+'_'+str(n)+'.'+xformat)
                            return self.output_path+'/'+newName+'_'+str(n)+'.'+xformat
                        else:
                            os.renames(self.output_path+'/'+self.file+'.'+xformat, self.output_path+'/'+newName+'.'+xformat)
                            return self.output_path+'/'+newName+'.'+xformat
        
        

            

        



