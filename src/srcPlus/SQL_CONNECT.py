'''
Created on 10/08/2017

@author: chernomirdinmacuvele
'''
from PyQt5.QtSql import QSqlDatabase
def creatConn():
    _db = QSqlDatabase.addDatabase("QPSQL")
    _db.setDatabaseName("DBBeforeGo")
    _db.setUserName("postgres")
    _db.setPassword("postgres")
    _db.setPort(5432)
    _db.setHostName("localhost")
    if _db.open():
        return _db     
    else:
        return False
    