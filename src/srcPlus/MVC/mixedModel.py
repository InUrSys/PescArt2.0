'''
Created on 18/09/2017

Este e um metodo livre que vai misturar varios modelos num so, o QueryModel e Relation Modal 
para facilitar a usuabilidade e vizualizacao dos dados, porque o relation model tem os pontos fracos 
como nao permitir relacoes dentro de relacoes entao uma mistuira com querymodel visa fortificar e reduzier 
a necessidade de criacao de longas linhas de codigo para tarefas simples, e o query model tem as suas faquezas como 
a vizulicao de dados em widgets porvezes costuma conter falhas na sicronizaocao.
o metodo vai permitir vizualizar os dados com mais mais facilidade, cricar os dados com paramentros passados e edicao de dados com mais flexibilidade 
e independencia.

o Modulo vai poder 
 - pegar qualquer elemento da tabela selecionada com base no dicionario
 - 
 -
 -
 
@author: chernomirdinmacuvele
'''
from PyQt5.Qt import Qt, QSqlRelationalTableModel, QSqlQueryModel,\
    QSqlTableModel, QDataWidgetMapper
from PyQt5 import QtSql
import QT_msg as msg
import FuncMakeScript


txt_306 = "Erro nº:309 \nPorfavor tente de novo."
txt_100 = "Erro nº: 100 \nPorfavor tente de novo."

def setViewModel(tblName=None, filtro=None, lstVal2Rel=None, lstRelTblName=None,lstNewNames=None, sort=0):
    '''
    Funcao para settar (ahahahaha) ou configurar o modelo, usando o built in relationTable.
    Tem como objectivo facilitar o mapeamento e visualizacao de dados, o modelo tem como 
    princinpal objectivo o uso na vizulizacao de dados em mapper e Views. 
    O Metodo tem a habilida de ser util em passando todos paramentros ou nao mais o paramentro
    fundamental e tblName.
    
    Args:
        tblName = Nome da tabela aqual queremos ligar na base de dados,  (Obrigatorio)
        filtro = filtro ou where e como desejamaos filtrar, (opicional)
        lstVal2Rel = os valores que desejamos fazer a relacao, (opicional)
        lstRelTblName = a tabela aqual desejamaos nos relacionar (obrigatorio se o campo anterior foi passado)
        lstNewNames =  os novos nomes que irao aparecer no header  (opicional)
        sort = como desejamos organizar a tabela por padrao e sempre o primeiro elemento e pode ser mudado (opicional)
    
    dictModel['val2Rel'] = lstVal2Rel
    dictModel["relTblName"] = lstRelTblName
    dictModel['newNames'] = lstNewNames
    '''
    bOK = False
    try:
        Model = QSqlRelationalTableModel()
        Model.setTable(tblName)
        if filtro is not None: #verificacao do Filtro
            Model.setFilter(filtro)
        if lstVal2Rel is not None and lstRelTblName is not None: #verificacao da lista de valores relacionais 
            for idx, val in enumerate (lstVal2Rel):
                if val is not None:
                    Model.setRelation(idx, QtSql.QSqlRelation(lstRelTblName[idx], val[0], val[1]))  
                    Model.setJoinMode(QSqlRelationalTableModel.LeftJoin)
        if lstNewNames is not None:
            for idx, val in enumerate (lstNewNames): #verificao dos Novos nomes na tabela
                Model.setHeaderData(idx, Qt.Horizontal, val)
        Model.setSort(sort, Qt.AscendingOrder) 
        bOK = Model.select()
        
        if not bOK:
            msg.error(txt="Erro na configuracao do Modelo", verbTxt=str(Model.lastError().text()))
            return (bOK, Model)
        else:
            return (bOK, Model)
        
    except TypeError as TE:
        msg.error(txt="Erro na configuracao do Modelo", verbTxt=str(TE))
        return (bOK, None)


def setQueryModel(query=None, filtro=None, lstNewNames=None):
        """Funcao para configurar o model script usando script, este model
        e usado para tabelas que muitas das vezes contem relacoes dentro de relacoes,
        nao aconselho a usar com mapper pois havera problemas de sicronizacao de elementos
        e se quiseres usar mesmo sabendo das consequecias, sim tem consequecias como:
        ma scronizacao com o mapper, para ser sincero e o unico problema que vejo hahahahhaha,
        mas e com disse e bem melhor usar so pra vizualizacao de dados complexos
        Args:
            - query = a query que vamos querer executar (obrigatoria)
            - filtro = caso a query precise de lementos adicionas para ser excutada (depende)
            - lstNewNames =  os novos nomes que irao aparecer no header  (opicional)
            - sort = como desejamos organizar a tabela por padrao e sempre o primeiro elemento e pode ser mudado (opicional)
        """
        model = QSqlQueryModel()
        if filtro is None: #lembras de eu ter dito no cometario anterio que depende? aqui esta se o tua query scritp recebe um where aqui esta o local onde deves colocar
            model.setQuery(query)
        else:
            model.setQuery(query.format(filtro))
        if lstNewNames is not None:
            for idx, val in enumerate (lstNewNames): #verificao dos Novos nomes na tabela
                model.setHeaderData(idx, Qt.Horizontal, val)
        model.lastError().isValid()
        if model.lastError().text() != ' ':
            verbTxt = model.lastError().text()
            msg.error(txt="Erro na configuracao do Modelo", verbTxt=str(verbTxt))
            return model
        else:
            return model


def setModel4CombBox(tblName= None, lstNames= None ,widg= None, namePos = 1, condName=None, condVal=None, condQuot=None):
    """
    Esta e a Funcao para configuracao de um model para combox onde o model pera ser script ou nao script,
    e outras palavras a configuracao do model pode ser via script ou usando nome da tabela, fixe nem?
    pois.
    
    Args:
        tblName: Nome da tabela
        lstNames: Lista dos Nomes dos campos da tabela que queremos usar(obrigatorio)
        widg: o combox que iremos usar (obrigatorio)
        namePos: position of the name we want to show in the combox normaly 1 because the name is always in position 1 (opcional)
        condName: Lista dos nomes dos campos que vao pertencer a condicao (opcional)
        condVal: Lista de Valores do campos que vamos usar (Obrigatorio se o condName foi atribuido)
        condQuot: Se queremos ou nao colocar dentro de aspas (Obrigatorio se o condName foi atribuido)
        
     e depois cria uma scritp para fazer-se o modelo do combox.   
    """
    bOK=False
    if tblName is not None and lstNames is not None:#yep  temos que que vericar tudo isso porque nao gostarias que o programa parace so por nao foi passdo um elemento nem?
        CbModel = QSqlQueryModel()
        if condName is not None and condVal is not None and  condQuot is not None:
            bOK, strSelect = FuncMakeScript.readScp(tblName, lstNames, condName, condVal, condQuot)
        else:
            bOK, strSelect = FuncMakeScript.readScp(tblName, lstNames)
        CbModel.setQuery(strSelect)
    else:
        CbModel = QSqlTableModel()
        bOK = True
    if bOK:
        widg.setModel(CbModel)
        widg.setModelColumn(namePos)
        return bOK
    else:
        msg.error(txt=txt_306, verbTxt=CbModel.lastError().text())
        return bOK
        
        
def getDataCombox(widg=None):
    """Get the Combox current ID
    A Busca o id do Combox passado,
    ele busca o index corrente depois, compara no modelo 
    e depois ele traz o ID que estara na possicao 0
    
    Args:
        widg: o widget do combox
    """
    if widg is not None:
        row = widg.currentIndex()
        idx = widg.model().index(row, 0)
        data = widg.model().data(idx)
        if widg.model().data(idx) is '' or widg.model().data(idx) == 0:
            data = 'NULL'
        return data
    if widg is None:
        return None


def reverseGetDataCombox(relText=None,widg=None):
    widg.model()


class withWidgets():
          
    def setMapper(self, model=None, fldToMap=None):
            """
            Metodo para configurar o mapper.
            """
            self.mapper = QDataWidgetMapper()
            self.mapper.setModel(model)
            for cidx, field in enumerate(fldToMap):
                if field is not None:
                    self.mapper.addMapping(field, cidx)
            self.mapper.toFirst()  
           
    def mapperToNext(self):
        self.mapper.toNext()
    
    
    def mapperToPerv(self):
        self.mapper.toPrevious()
    
    
    def getCurrentIndex(self):
        cIdx = self.mapper.currentIndex()
        return cIdx
    
    
    def getValueFromMapper(self, pos=0):
        try:
            val = self.mapper.model().record(self.mapper.currentIndex()).value(0) 
            row = self.mapper.currentIndex()
        except Exception:
            row = None
            val = None 
        return val, row
    
    
    def sychClickWithMap(self,indexModel=None):
            self.mapper.setCurrentModelIndex(indexModel)
    
    
    def setMapperToIdx(self, idx):      
        self.mapper.setCurrentIndex(idx)
               

