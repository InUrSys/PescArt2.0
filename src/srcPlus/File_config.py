'''
Created on 31/01/2018

@author: chernomirdinmacuvele
'''
import platform
import os

curPlatform = platform.system()
configFilePath = None
configDict = None


def getReportTemplateFile(path=None, File=None):    
    pathFile= None
    pathFile = os.path.join(path, File+'.jrxml')
    return pathFile


def isValidFile(pathFile= None):
    bOK = os.path.isfile(pathFile)
    return bOK
        
        
    
