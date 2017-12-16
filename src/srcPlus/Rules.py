'''
Created on 05/10/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QLineEdit, QPlainTextEdit, QComboBox
import QT_msg
import FuncSQL
from pprint import pprint
            
def setNull(wdgt=None, txt='n/a'):
    if isinstance(wdgt, QLineEdit):
        if wdgt.text() is '':
            wdgt.setText(str(txt))
    elif isinstance(wdgt, QPlainTextEdit):
        if wdgt.toPlainText() is '':
            wdgt.setPlainText(str(txt))  
    bOK= True
    return bOK


def notNull(wdgt=None):
    bOK=True
    if isinstance(wdgt, QLineEdit):
        if wdgt.text() is '':
            bOK= False
    elif isinstance(wdgt, QPlainTextEdit):
        if wdgt.toPlainText() is '':
            bOK= False
    elif isinstance(wdgt, QComboBox):
        if wdgt.currentText() is '' or wdgt.currentText() is None:
            bOK= False
    return bOK


def setUPPER(wdgt=None):
    try:
        if isinstance(wdgt, QLineEdit):
            txt = wdgt.text()
            txtOut = txt.upper()
            wdgt.setText(txtOut)
    except Exception:
        QT_msg.aviso(txt="Nao foi Possivel colocar o Texto em UPERCASE porfavor tente Manualmente")
        

             
def getRules_Wdgt():
    scpt_Indv = '''
                select ui_form.nome, ui_widgets.nome, ui_typerules.nome, ui_rules.rules,
                ui_rules.msg, ui_rules.react, ui_rules.lstaffected
                from ui_rules
                inner join ui_form on ui_rules.id_form = ui_form.id
                left outer join ui_widgets on ui_rules.id_widget = ui_widgets.id
                inner join ui_typerules on ui_rules.id_type = ui_typerules.id
                where ui_rules.activo=True and ui_typerules.id = 1
                '''
    bOK, lstOut = FuncSQL.multLineSelect(scpt=scpt_Indv)
    return  bOK, lstOut

def getRules_Frm():
    scpt_Indv = '''
                select ui_form.nome, ui_widgets.nome, ui_typerules.nome, ui_rules.rules,
                ui_rules.msg, ui_rules.react, ui_rules.lstaffected
                from ui_rules
                inner join ui_form on ui_rules.id_form = ui_form.id
                left outer join ui_widgets on ui_rules.id_widget = ui_widgets.id
                inner join ui_typerules on ui_rules.id_type = ui_typerules.id
                where ui_rules.activo=True and ui_typerules.id = 2
                '''
    bOK, lstOut = FuncSQL.multLineSelect(scpt=scpt_Indv)
    return  bOK, lstOut


def buildLVL_1(orgDict=None, lstform=None):
    '''
    Metodo para contruir o primerio lvl do dicionario 
    que sera usado mais tarde para juntar e formar o dicionario princinpal o
    primeiro lvl do dicionario e :
    {nomeForm: {'ValidateForm':{},
                'ValidateWidget':{},
                }
    Args:
        orgDict: Dicionario original
        lstForm: lista de forms 
    '''
    for val in lstform:
        orgDict[val]={'ValidateForm':{},'ValidateWidget':{}}
    return orgDict


def buildLVL_2(orgDict=None, lstform=None):
    '''
    metodo build second lvl, metodo que contruio segundo lvl do dicionario de regras
    que e :{'ValidateForm':{'rules':[],
                            'msg':[],
                            'reaction':[],
                            'objects':[]   
                            }
            }
    Args:
        orgDict: Dicionario original
        lstForm: lista de forms
    '''
    for val in lstform:
        orgDict[val]['ValidateForm']=buildLastLVL()
    return orgDict


def buildLVL_3(orgDict, lstform, lstWdgt, lstType):
    '''
    metodo para contruir o 3 lvl do dicionario de regras onde iremos encotrar a contrucao de
    regras para cada vidget do form.
    {'ValidateWidget':{'widgetName':{'rule':[],
                                    'msg':[],
                                    'reaction':[],
                                    'objects':[]
                                    }
                       }
    }
    Args:
        orgDict: Dicionario original 
        lstForm: lista de forms
        lstWdgt: lista de widgets 
        lstType: lista de tipos
    '''
    lstOut = check(lstform, lstWdgt, lstType)
    for form, wdg, type in lstOut:
        if type == 'ValidateWidget' :
            orgDict[form]['ValidateWidget'][wdg]=buildLastLVL()
    return orgDict

        
def buildLastLVL():
    '''
    Metodo para contruir o dicionario de regras e msg,
    para todas a regras seja widget ou form tem sempre rule, msg 
    entao este metodo esta encaregue de os criar.
    '''
    dictOut={'rule':[],
             'msg':[],
             'reaction':[],
             'objects':[]
            }
    return dictOut


def check(lstA,*lstB):
    '''
    Metodo para criar lista de tuplas, onde podem ser passado 2 ou mais listas e retorna
    uma lista de tupla dos elementos, os dicionarios tem que ter mesma dimensao.
    '''
    iter1 = list(zip(lstA, *lstB))
    return(iter1)
    
    
def appendRULEMSG(orgDict, rule, msg, react, objects):
    '''
    Metodo para acrescentar regras e msg na lista de regras e menssagens, 
    Args:
        orgDict: Dicionario original
        rule: regras
        msg: menssagem
        react: reaction
    '''
    orgDict['rule'].append(rule)
    orgDict['msg'].append(msg)
    orgDict['reaction'].append(react)
    orgDict['objects'].append(objects)
    return orgDict
    
    
def exeBuidAndFill(mainDict=None, matxOut=None, matxWdgt=None, matxFrm=None):
    '''
    Metodo para contruir o dicionario de regras juntando todos metodos builds
    do primeiro lvl ate o ultimo e depois preenchendo lhe com as devidas regras nos deviddos lugares 
    '''
    lstForm = [x[0] for x in matxOut]
    lstFld = [x[1] for x in matxOut]
    lstRuleType = [x[2] for x in matxOut]
    mainDict = buildLVL_1(orgDict=mainDict, lstform=lstForm)
    mainDict = buildLVL_2(orgDict=mainDict, lstform=lstForm)
    mainDict = buildLVL_3(orgDict=mainDict, lstform=lstForm, lstWdgt=lstFld, lstType=lstRuleType)    
    mainDict = fillMain_Frm(matxFrm=matxFrm, mainDict=mainDict)
    mainDict = fillMain_Wdgt(matxWdgt=matxWdgt, mainDict=mainDict)
    return mainDict


def fillMain_Frm(matxFrm, mainDict):
    '''
    Metodo para prencher as regras de Forms
    
    Args:
        matxFrm-> matriz das regras dos forms
        mainDict_> dicionario princinpal
    '''
    for val in (matxFrm):
        form = val[0]
        ruleType = val[2]
        rule =  val[3]
        msg = val[4]
        react= val[5]
        objects= val[6]
        dictIn = mainDict[form][ruleType]
        mainDict[form][ruleType] = appendRULEMSG(orgDict=dictIn, rule=rule, msg=msg, react=react, objects=objects)
    return mainDict


def fillMain_Wdgt(matxWdgt, mainDict):
    '''
    Metodo para prencher as regras de Forms
    
    Args:
        matxWdgt-> matriz das regras dos widgets
        mainDict_> dicionario princinpal
    '''
    for val in (matxWdgt):
        form = val[0]
        wdg = val[1]
        ruleType = val[2]
        rule =  val[3]
        msg = val[4]
        react = val[5]
        objects= val[6]
        dictIn = mainDict[form][ruleType][wdg]
        mainDict[form][ruleType][wdg] = appendRULEMSG(orgDict=dictIn, rule=rule, msg=msg, react=react, objects=objects)
    return mainDict

def splitObjectName(matxIn=None):
    try:
        for idx in range(len(matxIn)):
            objects = matxIn[idx][6]
            lstNames = objects.split(sep=", ")
            matxIn[idx][6]= lstNames
    except IndexError:
        print("error ")
    return matxIn

              
def lstToDict(lstNames=None, lstVal=None):
    keys = lstNames
    values = lstVal
    dictOut = dict(zip(keys, values))
    return dictOut


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def exec_Rule(lstNames=None, lstVal=None, dictTrack=None, dictRule=None):
    valDict = lstToDict(lstNames=lstNames, lstVal=lstVal)
    if dictTrack is None:
        toFormat = valDict
    else:
        toFormat = merge_dicts(valDict, dictTrack)
    lstError= []
    lstReac=[]
    lstObjNames = []
    error_bOK = True
    if dictRule is not None:
        for idx, rule in enumerate(dictRule['rule']):
            try:
                querRule = rule.format(**toFormat)
                bOK, Rule_Bok = FuncSQL.anySelectScript(scpt=querRule)
                if bOK:
                    if Rule_Bok[0] is not True:
                        lstError.append(dictRule['msg'][idx])
                        lstReac.append(dictRule['reaction'][idx])
                        lstObjNames.append(dictRule['objects'][idx])
                        error_bOK = False
                    else:
                        error_bOK = True
            except KeyError as ky:
                lstError = ['Error chave nao encontrada reveja o regra '+ str(ky)]
    return error_bOK, lstError, lstReac, lstObjNames
        
    

def Cond2Rule(condIn):
    '''
    Build an "Rule", working in SQL, from a SQL Expression defining a test condition
    '''
    R = "SELECT CASE WHEN (" + condIn + ") THEN TRUE ELSE FALSE;"
    return(R)

