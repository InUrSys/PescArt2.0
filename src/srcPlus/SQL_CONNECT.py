'''
Created on 10/08/2017

@author: chernomirdinmacuvele
'''
from PyQt5.QtSql import QSqlDatabase
import File_config as Fcj

def creatConn():
    dictCon= Fcj.configDict
    _db = QSqlDatabase.addDatabase("QPSQL")
    _db.setDatabaseName(dictCon['database'])
    _db.setUserName(dictCon['username'])
    _db.setPassword(dictCon['password'])
    _db.setPort(int(dictCon['port']))
    _db.setHostName(dictCon['host'])
    if _db.open():
        return _db    
    else:
        return False
    