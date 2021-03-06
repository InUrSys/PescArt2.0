'''
Created on 07/11/2017

@author: chernomirdinmacuvele
'''
from platform import platform, machine, version, uname, system, processor, node
import os
from datetime import datetime
import File_config
import shelve
from PyQt5.Qt import QFileDialog
import QT_msg
'''
Sera um modulo com Diferentes regras a serem implementadas
'''

tempo = datetime.today()
dictMachineInfo = {
            'machine':machine(),
            'version':version(),
            'node':node(),
            'system':system(),
            'processor':processor(),
            'platform':platform(),
            }

dictWho ={
            'user': None,
            'time': None,
            'machine': dictMachineInfo
            }

                
myCWD = File_config.configDict['configFiles']


        

def logIN(user=None, tempox=tempo):
    dictWho['user'] = user
    dictWho['time'] = tempox
    with open(myCWD, 'a+') as file:
        if file.writable():#verifica se o ficheiro pode ser escrito
            file.write('Registo da Data: '+str(dictWho['time'])+'\n'+
                       'Usuario: '+str(dictWho['user'])+'\n'+
                       'Informacao do sistem: '+str(dictWho['machine'])+'\n'+
                       'Log: Log IN \n'+
                       "\n"+
                       "\n")
            
            
def logOUT(user=None):
    dictWho['time'] = tempo
    with open(myCWD, 'a+') as file:
        if file.writable():#verifica se o ficheiro pode ser escrito
            file.write('Registo da Data: '+str(dictWho['time'])+'\n'+
                       'Usuario: '+str(dictWho['user'])+'\n'+
                       'Informacao do sistem: '+str(dictWho['machine'])+'\n'+
                       'Log: Log OUT \n'+
                       "\n"+
                       "\n")


def whatHappen(info= None):
    dictWho['time'] = tempo
    with open(myCWD, 'a+') as file:
        if file.writable():#verifica se o ficheiro pode ser escrito
            file.write('Registo da Data: '+str(dictWho['time'])+'\n'+
                       'Usuario: '+str(dictWho['user'])+'\n'+
                       'Informacao do sistem: '+str(dictWho['machine'])+'\n'+
                       'Log: QUERY: '+(str(info))+' \n'+
                       '\n'+
                       '\n')


def errorHappen(info= None):
    dictWho['time'] = tempo
    with open(myCWD, 'a+') as file:
        if file.writable():#verifica se o ficheiro pode ser escrito
            file.write('Registo da Data: '+str(dictWho['time'])+'\n'+
                       'Usuario: '+str(dictWho['user'])+'\n'+
                       'Informacao do sistem: '+str(dictWho['machine'])+'\n'+
                       'Log: ERROR: '+(str(info))+' \n'+
                       "\n"+
                       "\n")