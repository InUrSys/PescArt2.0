'''
Created on 27/11/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QApplication, QStyleFactory, QSqlQuery, QFileDialog
from SQL_CONNECT import creatConn
from ui_user_Log import Ui_Form
from PyQt5.Qt import QDialog
from frmMain import frmMain
import QT_msg
import config
import File_config
import shelve
import os

class logIn(QDialog, Ui_Form):
    
    def __init__(self, parent=None):
        super(logIn, self).__init__(parent)
        self.setupUi(self)
        
        self.makeConfigPublic()
        
        
    def makeConfigPublic(self):
        if os.path.isfile("PathConfig.db"):
            with shelve.open("PathConfig") as PathConfigFile: 
                PathOut = PathConfigFile['path']
                
            with shelve.open(PathOut) as ConfigDictOut: 
                File_config.configDict = ConfigDictOut['configDict']
            
        else:
            with shelve.open("PathConfig") as PathConfigFile: 
                QT_msg.aviso(txt = "Selecione o Directorio onde estao os ficheiros de Configuracao")
                FileDlg = QFileDialog()
                PathOut, _ = FileDlg.getOpenFileName(self)
                PathOut= PathOut.replace(".db", "")
                PathConfigFile['path']= PathOut

            with shelve.open(PathOut) as ConfigDictOut: 
                File_config.configDict = ConfigDictOut['configDict']
                
        #Set The Form        
        self.setForm()
        
        
    def setForm(self):
        self.dbPescArt = creatConn()
        self.PBEntrar.clicked.connect(self.logIn)
        self.setAppStyle()
        
    def setAppStyle(self):
        style = File_config.configDict
        QApplication.setStyle(QStyleFactory.create(style['theme']))

        
    def logIn(self):
        bOK, (idx, username, user_level) = self.getUserInfo()
        if bOK:
            lstCre = (idx, username, user_level)
            self.hide()
            config.dictSession['userName']= str(lstCre[1])
            config.dictSession['Level']= str(lstCre[2])
            self.mainForm = frmMain(dbCon=self.dbPescArt, user_info=lstCre)
            self.mainForm.show()
        
        
    def getUserInfo(self):
        psw = self.LEPassword.text()
        user = self.LEName.text()
        idx, username, user_level = None, None, None
        query = '''SELECT tbl1.id, username, user_level, tbl2.nome 
                FROM public.log_user as tbl1 
                inner join log_level as tbl2 on tbl1.user_level = tbl2.id
                where username like '{nome}' and user_psw='{psw}' and activo = True;
                '''.format(nome= user, psw= psw)
        toExe = QSqlQuery()
        bOK= toExe.exec_(query)
        if bOK:
            bOK = toExe.first()
            if bOK:
                idx = toExe.value(0)
                username = toExe.value(1)
                user_level = toExe.value(2)
            else:
                QT_msg.aviso(txt="Username or password doesnt exist, Please try a valid one.")  
        else:
            QT_msg.aviso(txt="Please try a valid information dont try SQL Commands.")
        return bOK, (idx, username, user_level)
        