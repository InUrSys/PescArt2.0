'''
Created on 27/11/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QApplication, QStyleFactory, QSqlQuery
from SQL_CONNECT import creatConn
from ui_user_Log import Ui_Form
from PyQt5.Qt import QDialog
from frmMain import frmMain
import QT_msg
import config
import WhatLog

class logIn(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(logIn, self).__init__(parent)
        self.setupUi(self)
        
        self.dbPescArt = creatConn()
        self.PBEntrar.clicked.connect(self.logIn)
        QApplication.setStyle(QStyleFactory.create(QStyleFactory.keys()[1]))

        
    def logIn(self):
        bOK, (idx, username, user_level) = self.getUserInfo()
        if bOK:
            lstCre = (idx, username, user_level)
            self.hide()
            config.dictSession['userName']= str(lstCre[1])
            config.dictSession['Level']= str(lstCre[2])
            WhatLog.dictWho['user'] = str(lstCre[1])
            WhatLog.dictWho['time'] = WhatLog.tempo 
            self.mainForm = frmMain(dbCon=self.dbPescArt,user_info=lstCre)
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
        