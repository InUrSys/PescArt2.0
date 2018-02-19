'''
Created on 13/02/2018

@author: chernomirdinmacuvele
'''

from ui_imageToPDF import Ui_Form
from PyQt5.Qt import QDialog, QFileDialog
import File_config
from PIL import Image
import os
from fpdf.fpdf import FPDF
from pdfrw.pdfreader import PdfReader
from pdfrw.objects.pdfdict import PdfDict
from pdfrw.pdfwriter import PdfWriter
from pprint import pprint
import rscForm
import shutil
import QT_msg
import subprocess


class frmImageToPdf(QDialog, Ui_Form):
    def __init__(self,codigo=None, data=None, centroPesca=None, registadores=None):
        super().__init__()
        self.setupUi(self)
        
        self.setForm()
        self.lstPath = []
        self.mdx = None
        self.LEN_Sequencial.setText(codigo)
        self.LEDataAmost.setText(data)
        self.LECentroPesca.setText(centroPesca)
        self.LERegistadores.setText(registadores)
        
    
        
    #Prencher os Campos com que vem da ficha 1
    def setForm(self):
        self.outPath = File_config.configDict['in_report']
        self.PBAdd.clicked.connect(self.getFile)
        self.PBSave.clicked.connect(self.check)
        self.PBremove.clicked.connect(self.removeItem)
        self.LWidgetPaths.clicked.connect(self.clickedItem)
        
    
    #Abrir Dialog para insercao de path
    def getFile(self):
        pic, _ = QFileDialog().getOpenFileName(self)
        if pic != '':
            format = pic[-3:]
            if format == "pdf":
                #add tags and move the copy to the folder
                self.LWidgetPaths.addItem(pic)
                self.lstPath.append(pic)
                print(pic+ ' e PDF')
                
            elif format in ('jpg', 'png', 'jpeg','PNG', 'JPG', 'JPEG'):
                pictOut = self.ResizeToA4(pic=pic)
                picFileName =  self.Renaming()
                pictOut.save(picFileName)
                self.LWidgetPaths.addItem(picFileName)
                self.lstPath.append(picFileName)

            
    
    def ResizeToA4(self, pic=None):
        size = 550, 800
        newPic = Image.open(pic)
        newPic.thumbnail(size, Image.ANTIALIAS)
        return newPic
        
        
    def Renaming(self, format=".png"):
        i = 0
        bOK = False
        if format== ".pdf":
            while bOK == False:
                i+=1
                if os.path.isfile(os.path.join(self.outPath, str(i)+format)) != True:
                    bOK = True
            i = str(i)
            return os.path.join(self.outPath, str(i)+format)
        
        else:
            try:
                os.makedirs(os.path.join(self.outPath,'trash'))
            except FileExistsError:
                pass
            while bOK == False:
                i+=1
                if os.path.isfile(os.path.join(self.outPath,'trash',str(i)+format)) != True:
                    bOK = True
            i = str(i)
            return os.path.join(self.outPath,'trash',str(i)+format)

        
        
    #Fazer o PDF
    def ConvertIMG_PDF(self, lstPath=None):
        pdf = FPDF(orientation= 'P', unit= 'cm', format = 'A4')
        for Path in lstPath:
            pdf.add_page()
            x,y,w,h = 0, 0, 20, 28
            pdf.image(Path,x,y,w,h)
        path = self.Renaming(format=".pdf")
        pdf.output(path, "F")
        self.AddTags(pdfPath=path)



#===============================================================================
# 
#===============================================================================

    def check(self):
        lstIMGFormat = ['jpg', 'png', 'jpeg', 'PNG', 'JPG', 'JPEG']
        lstPdf = []
        lstIMG = []
        for pathFile in self.lstPath:
            pathFormat = pathFile[-3:]
            if pathFormat == "pdf":
                lstPdf.append(pathFile)
            elif pathFormat in lstIMGFormat:
                lstIMG.append(pathFile)
            
        
        if lstIMG is not []:
            self.ConvertIMG_PDF(lstPath= lstIMG)
        
        if lstPdf is not []:
            for pdfFile in lstPdf:
                #copy to Directory
                newPath = shutil.copy(pdfFile, self.outPath)
                #add tags
                self.AddTags(pdfPath = newPath)
                
        
        QT_msg.Sucessos(txt="PDF Criado Com sucesso.")
        self.close()

#===============================================================================
# 
#===============================================================================
    
    
    def AddTags(self, pdfPath): 
        
        lstVal = self.getData()
          
        trailer = PdfReader(pdfPath)
          
        metadata = PdfDict(Id = lstVal[0], Data_Registo = lstVal[1], 
                           CentroPesca = lstVal[2], Registador= lstVal[3], 
                           Info = lstVal[4])

        trailer.Info.update(metadata)
        PdfWriter().write(pdfPath, trailer)
        
        trailer = PdfReader(pdfPath)
        pprint(trailer.Info)
    
    
    def getData(self): 
        lstWdg = [self.LEN_Sequencial, self.LEDataAmost, self.LECentroPesca, self.LERegistadores, self.PTEInfo]
        lstVal = rscForm.getTextAll(lstWidg=lstWdg)
        return lstVal
        
    
    def clickedItem(self,mdx=None):
        self.mdx=mdx
        path = mdx.model().data(mdx)
        
        sop = File_config.configDict['sistema']
        if sop == 'Darwin':
            subprocess.Popen(['open', path])
        print(path)
    
    
    def removeItem(self):
        if self.mdx != None:
            item = self.mdx.row()
            self.LWidgetPaths.takeItem(item)
            try:
                self.lstPath.remove(self.mdx.model().data(self.mdx))
            except ValueError:
                pass
            self.mdx = None
            