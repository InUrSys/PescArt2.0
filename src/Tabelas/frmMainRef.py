'''
Created on 15/07/2017
Class  Main das Referencias.
Esta e a class que vai nos permitir inserir, editar e vizualizar os dados das tabelas de referencia,
A class abre um Dialog/form com:
    TVMain: table view que vai nos permitir vizualizar os dados contidos no model
    LEPesquisar: um lineEdit que vai servir de auxilo na pesquisa 
    CBGrupo: o Combox Grupo em um combox valido so para um tabela de refencia 
    PBPesquisar: e o botao que tera que se 'clickar', para poder realizar a pesquisa
    PBAtualizar: e o botao que tera quue se 'clickar', para realizar a atulizacao(refresh) do form
    PBAdicionar: e o botao que tera que se 'clickar', para se adicionar novos elementos
    PBCancelar: este botao fecha o Dialog
    PBEditar: e o botao que tera que se 'clickar', para se editar elementos

a class tambem contem os seguintes blocks
    #Inicializacao Class - este e o block onde inicializamos as variaveis da class
    #Inicializacao Data - este e o block onde inicializamos os dados, que iram popular todos elementos
    #Events - este e o block dos eventos que serao realizados e com quem irao se connectar
    #Metodos - Block dos metodos.

@author: chernomirdinmacuvele
'''
from ui_MainRef import Ui_MainForm 
from PyQt5.Qt import QDialog, QTimer
import QT_tblViewUtility
import mixedModel as wrapModel
import QT_msg
from dlg_Diasemana import dlg_diasemana
from dlg_Simpel import dlg_simpel
from dlg_Artes import dlg_artes
from dlg_Especies import dlg_especies
from dlg_Geometric import dlg_geometric
from dlg_Tabelas import dlg_tabela
from dlg_TipLocal import dlg_tiplocal
import QT_widgetsCustom
from dlg_UniPescaTipo import dlg_UniPescaTipo
from dlg_IntClass import dlg_intClass
from dlg_pesqueiros import dlg_pesqueiros
from dlg_registadores import dlg_registadores
import CustomItemDelegates
import rscForm


class frmMainRef(QDialog, Ui_MainForm):
    def __init__(self, parent = None, dbCon=None, mainIndex=None, user_info=None):#0
        super(frmMainRef, self).__init__(parent)
        self.setupUi(self)
        
        #=======================================================================
        #Inicializacao Class
        '''
        Este e o block onde inicializaremos as variaveis da class.
        dbCon = A conneccao com a base de dados.
        mainIndex = E a posicao onde os nossos dados estarao situados no dicionario principal (MainDict)
                    O dicionario principal deve estar organizado cosoante o dicionario de widgets da 
                    Class MenuTypes.
        '''
        self.dbcon = dbCon
        self.idx = mainIndex
        self.mIndex=None
        self.user_info = user_info
        self.setSecurity()
        self.setDict()
        self.setMainDict()
        self._toHide()
        self._setFormToSelected()
        self.costumForm()
        self.toNormal()
        
        
        #Eventos
        self.CBGrupo.currentTextChanged.connect(self.onTextChange)
        self.PBProcurar.clicked.connect(self.search)
        self.PBAtualizar.clicked.connect(self.refresh)
        self.PBAdicionar.clicked.connect(self.operacao)
        self.PBVizualizar.clicked.connect(self.operacao)
        self.PBEditar.clicked.connect(self.operacao)
        self.TVMain.clicked.connect(self.afterClick)
        self.PBCancelar.clicked.connect(self.close)
        
       
        
    #Metodos
    def onTextChange(self):#1
        '''
        Metodo que sera chamado quando houver alguma mudanca de texto no comBox,
        Como funciona:
            primerio levamos o texto que esta ser disposto/disponivel, no comBox,
            para depois procurar o seu Codigo. Quando o codigo for encontrado, sera
            devolvido.
            Depois cria-se o filtro para mostrar so os dados corespondentes a esse
            id.
            E depois criamos o modelo para o view com o filtro.
        '''   
        Id  = wrapModel.getDataCombox(widg=self.CBGrupo)
        filtro = ("id_grupo = '{combox}'").format(combox = Id)
        self.setModelInView(filtro=filtro)
        self.mIndex=None
    
    
    def refresh(self):#2
        '''
        Metodo para atualizar/Refrescar o modelo, chamando o metodo _toHide()
        '''
        self._toHide()
        self.mIndex=None
        
    
    def search(self):#3
        '''
        Metodo para fazer pesquisa de nomes, dentro da tabela/modelo.
        Como faz:
            primerio verificamos se a refencia onde nos escontramos nao precisa do Combox,
                - se nao vamos adicionar um filtro, com o nome digitado no Linha de texto.
                - se sim vamos levar o valor corrente na combox e procuramos o seu codigo, com o codigo
                do combox, e o valor do texto crimaos um filtro.
            Depois reemplementamos o metodo setModelInView com o filtro definido.
        '''
        toHide = self.dictMain['toHideGrupo'][self.idx]
        if toHide:
            filtro = (self.dictMain['fldFiltro'][self.idx]).format(nome = self.LEFiltro.text())
        else:
            Id  = wrapModel.getDataCombox(widg=self.CBGrupo)
            nome = self.LEFiltro.text()
            filtro = (self.dictMain['fldFiltro'][self.idx]).format(combox = Id, nome = nome)
        self.setModelInView(filtro=filtro)
        self.mIndex=None
      
       
    def _toHide(self):#4
        '''
        Metodo para esconder ou nao CombBox depois configurar o modelo e atribuilo ao view.
        Como faz:
            primeiro verificamos se devemos ou nao esconder o combox, 
                - se sim, escodemos e depois chamamos o setModelInView()
                - se Nao, chamamos o metodo setComBoxGrupo, que vai configurar e atribuir um modelo ao combox.
                Depois chamamos o setModelInView agora com o filtro que sera so os elementos ligados ao combox ID.
        '''
        toHide = self.dictMain['toHideGrupo'][self.idx]
        if toHide:
            self.setModelInView()
        else:
            bOK = self.setComboxGrupo()
            if bOK:
                Id  = wrapModel.getDataCombox(widg=self.CBGrupo)
                filtro = ("id_grupo = '{combox}'").format(combox = Id)
                self.setModelInView(filtro=filtro)
          
            
    def setComboxGrupo(self):#5
        '''
        Metodo para configurar e atribuir um modelo a combox.
        Todo processo e feito no modulo.setModel4ComBox
        Args:
            tblName= Nome da tabela
            lstNames= Nome das colunas, sempre sao 2 (id, Nomes) porque nos queremos quer o combox mostre o id das colunas
            widg=  O object widget (combox)
            condName= caso tenhe alguma condicao aqui vamos passar o nome (id)
            condVal= a qui o valor ('XPT')
            condQuot= e aqui sera se sera quoted ou nao (True e false)
        '''
        bOK = False
        try:
            tblName= self.dictMain['fldDlgDict'][self.idx]['condTbl']
            lstNames= self.dictMain['fldDlgDict'][self.idx]['condCol']
            widg= self.CBGrupo
            condName= self.dictMain['fldDlgDict'][self.idx]['condName']
            condVal= self.dictMain['fldDlgDict'][self.idx]['condVal']
            condQuot= self.dictMain['fldDlgDict'][self.idx]['condToQuote']
            wrapModel.setModel4CombBox(tblName=tblName, lstNames=lstNames, widg=widg, condName=condName, condVal=condVal, condQuot=condQuot)
            bOK = True
            return bOK
        
        except KeyError as ky:
            QT_msg.error(txt='Error Elemento nao encontrado', verbTxt=str(ky))
            return bOK
        
      
    def setModel(self, filtro=None):#6
        '''
        Metodo para configurar o modelo que sera usado para relaizar a visualizacao de dados
        Args:
            filtro: sera passado, quando se usar o bottao pesquisar
        '''
        tblName = self.dictMain["tblName"][self.idx]
        lstVal2Rel =self.dictMain['fldDlgDict'][self.idx]['val2Rel']
        lstRelTblName =self.dictMain['fldDlgDict'][self.idx]['fldRelTblMain']
        lstNewNames =self.dictMain['fldDlgDict'][self.idx]['headerTitle']
        bOK, model = wrapModel.setViewModel(tblName = tblName, filtro = filtro, lstVal2Rel = lstVal2Rel, lstRelTblName = lstRelTblName, lstNewNames = lstNewNames)
        

        self.deleg = CustomItemDelegates.CustomItemDelegate()
        lstToHide = self.dictMain['fldDlgDict'][self.idx]['lstToHide']
        QT_tblViewUtility.setModelInView(tblView= self.TVMain, ViewModel= model, toHide= lstToHide)
        self.TVMain.setItemDelegate(self.deleg)
        return (bOK, model)
    
    
    def setModelInView(self, filtro=None):#7
        '''
        Metodo para atribuir um model condfigurado ao view, caso 
        o model tenha sido configurado com sucessos o metodo ira atribuir ao
        view um model.
        Args:
            filtro: sera passado, quando se usar o bottao pesquisar
        '''
        bOK, model = self.setModel(filtro=filtro)
        if bOK:
            self.TVMain.setModel(model)
          
    
    def afterClick(self, mIdx=None):#8
        '''
        metodo so para atualizar o modelIndex depois de se ter selecionado um na tabela.
        '''
        self.mIndex = mIdx  
            
            
    def operacao(self):#9
        bOk=False
        if self.sender() is self.PBEditar or self.sender() is self.PBVizualizar:
            indexModel = self.mIndex
            if indexModel is None:
                QT_msg.aviso(txt='Aviso 9.1: Selecione um elemento na tabela para poder Editar')
            else:
                bOk, msgOut= self.openDlgPOP(indexModel= indexModel)
        elif self.sender() is self.PBAdicionar:
            bOk, msgOut= self.openDlgPOP()  
        if bOk:
            if msgOut is not None:
                self.showMsg(obj= self.LBwhois, msgAlert= msgOut)
            self.refresh()#Changed
            self.mIndex=None
            
            
    def openDlgPOP(self, indexModel=None):#10
        msgOut=None
        toHide = self.dictMain['toHideGrupo'][self.idx]
        _,_,level = self.user_info
        try:
            if toHide:
                run = self.dictMain["dlgToPop"][self.idx](dbcon = self.dbcon, tblName=self.dictMain["tblName"][self.idx], indexModel=indexModel, level= level)
            else:
                curText = self.CBGrupo.currentText()
                run = self.dictMain["dlgToPop"][self.idx](dbcon = self.dbcon, tblName=self.dictMain["tblName"][self.idx], indexModel=indexModel, idx=curText, level= level)
            run.exec_()
            if run.close():
                bOK, msgOut = run.bOK
            else:
                bOK= False
        except Exception:
            QT_msg.error(txt="Error 10.1: A Pagina fechou inesperadamente porfavor tente novamente.", verbTxt = str(Exception))
            bOK= False
        return bOK, msgOut

        
    def _setFormToSelected(self):#13
        '''
        Metodo para formatar o Form para o que estiver selecionado.
        '''
        idx = self.idx
        self.setWindowTitle(self.dictMain['formLabelName'][idx])
        self.LBTitulo.setText(self.dictMain['formLabelName'][idx])
        self.LBGrupo.setHidden(self.dictMain['toHideGrupo'][idx])
        self.CBGrupo.setHidden(self.dictMain['toHideGrupo'][idx])
        
        
    def costumForm(self):#14
        widx = self.dictMain['fldDlgDict'][self.idx]['sizeForm'][0]
        hidx = self.dictMain['fldDlgDict'][self.idx]['sizeForm'][1]
        lstSizeCol = self.dictMain['fldDlgDict'][self.idx]['sizeCol']
        QT_tblViewUtility.resizeForm(formToResize=self, Wx=widx, Hx=hidx)
        QT_tblViewUtility.setViewCustom(tblView=self.TVMain, lstSizeCol=lstSizeCol)
        
    
    def showMsg(self, obj=None, msgAlert=None):
        time = QTimer(self)
        obj.setText(msgAlert)
        QT_widgetsCustom.successDatabase(obj= obj)
        time.start(10000)
        time.setSingleShot(True)
        time.timeout.connect(self.toNormal)
   
   
    def toNormal(self):
        _,userName,_ = self.user_info
        objName = self.LBwhois.objectName()
        css= "#"+str(objName)+"""{
                color:black;
                }"""
        self.LBwhois.setStyleSheet(css)
        self.LBwhois.setText(str(userName).capitalize())
    
    
    def setSecurity(self):
        '''
        Metodo para abilitar e desabilitar os campos de acordo com o nivel do usuario.
        '''
        self.setDictSecurity()
        _,_,level = self.user_info
        lstWdg = self.dictLocked[str(level)]
        if lstWdg is not None:
            rscForm.setReadOnlyAll(True, lstWdg)
    
    
    def setDict(self):
        '''
        Metodo para confirgurar o dicionario dictXXX 
        que vao axiliar na criacao de modelos e dialogs
        que sera compostos por:
        Args:
        Nota1 - este sao os valores usados para cria o modelo sao os valores basicos que um dicioanrio precisa ter para poder
        usar o wrapper mixedModel.
            - fldName: Nomes das colunas na base de dados
            - headerTitle:a os novos Nomes que seram mostrados no header
            - toQuote:
            
        Nota2: este sao os valores usados para cricao da relacao 
            - val2Rel: Nome do elementos que queremos relacionar normalmente e o nome id pois no mixed model levamos sempre o segundo elemento como nome
            - fldRelTblMain:  Nome da tabela aqual nos relacionamos
        
        Nota3: este sao os valores que iram axiliar na producao do combox, nem todos tem este valores pois eles sao exclusivos so para 
        as tabelas que depende do grupo
        
        Nota4: dictSimpel corresponde as tabelas (nivel, grupo)
        '''
        self.dictPesquerio =    {
                            'fldName': ["id", "id_centro", "nome", "comentario", "activo"],
                            'headerTitle': ['Cod.', 'Provincia', 'Nome', 'Comentario', 'Activo'],
                            'lstToHide':[True, False, False, True, False],
                            'fldToQuote': [False, True, True, True, True],
                            
                            'val2Rel': [None, ['id', 'Nome'], None, None, None],
                            'fldRelTblMain': [None, 'ref_geometric', None, None, None],
                            'sizeCol':[50, 250, 300, 100, 100],
                            'sizeForm':[937, 617],
                            }
        
        self.dictRegistador = { 
                            'fldName': ["id", "id_centro", "nome", "comentario", "activo"],
                            'headerTitle': ['Cod.', 'Provincia', 'Nome', 'Comentario', 'Activo'],
                            'lstToHide':[True, False, False, True, False],
                            'fldToQuote': [False, True, True, True, True],
                            
                            'val2Rel': [None, ['id', 'Nome'], None, None, None],
                            'fldRelTblMain': [None, 'ref_geometric', None, None, None],
                            'sizeCol':[50, 250, 300, 190, 190],
                            'sizeForm':[937, 617],
                            }       
        
        self.dictArtes=     {
                            'fldName': ["id", "nome", "id_uniesforco", "id_unitrabalho", "id_tippesca", "descricao", "comentario", "activo"],
                            'headerTitle':["Cod.", "Nome", "Unidade de Esforco", "Unidade de  Trabalho", "Tipo de Pesca", "Descricao", "Comentarios", "Activo"],
                            'lstToHide':[True, False, False, False, True, True, True, False],
                            'fldToQuote': [True, True, True, True, True, True, True,  False],
                            
                            'val2Rel': [None, None, ['id', 'nome'], ['id', 'nome'], ['id', 'nome'], ['id','nome'], None, None, None],
                            'fldRelTblMain': [None, None, 'ref_table', 'ref_table', 'ref_table', None, None, None, None, None],
                            'sizeCol':[80, 200, 200, 200, 200, 100, 100, 50],
                            'sizeForm':[1017, 617],
                            }
        
        self.dictDiaSemana= {
                            'fldName': ["id", "id_tipdia",  "nome",  "descricao", "comentario", "activo"],
                            'headerTitle': ["Cod.", "Tipo de Dia", "Nome", "Descricao", "Comentarios", "Activo"],
                            'lstToHide':[True, False, False, True, True, False],
                            'fldToQuote': [True, True, True, True, True,  False],
                            
                            'val2Rel': [None, ['id','nome'],None, None, None,None],
                            'fldRelTblMain': [None, 'ref_table', None, None, None, None],
                            'sizeCol':[100, 200, 300, 120, 120, 50],
                            'sizeForm':[937, 617],
                            }
        
        self.dictEspecies=  {
                            'fldName': ["id", "familia", "genus", "species", "id_habitat", "minlength", "maxlength", "intlength", "intmaxlen", "ana_comesp", "comentario", "activo", 'nome'],
                            'headerTitle': ["Cod.", "Familia", "Genus", "Especie", "Habitate", "comp.mínimo", "comp.máximo", "Int.comum", "Int.máximo", "A.Composicao", "Comentarios", "Activo", "Nome"],
                            'lstToHide':[True, False, False, False, True, True, True, True, True, True, True,False, False],
                            'fldToQuote': [True, True, True, True, True, False, False, False, False, False, True, False, False],
                            
                            'val2Rel': [None, None, None, None, ['id', 'nome'], None, None, None, None, None, None, None, None],
                            'fldRelTblMain': [None, None, None, None, 'ref_table', None, None, None, None, None, None, None, None],
                            'sizeCol':[80, 180, 180, 180, 150, 40, 40, 40, 40, 50, 100, 50, 150],
                            'sizeForm':[1098, 617],
                            }
        
        self.dictGeometric= {
                            'fldName': ["id", "id_tiplocal", "id_parent" , "nome",  "descricao", "comentario", "activo"],
                            'headerTitle': ["Cod.", "Tipo de Local", "Parente", "Nome", "Descricao", "Comentarios", "Activo"],
                            'lstToHide':[True, False, False, False, True, True, False],
                            'fldToQuote': [True, True, True, True, True, True,  False],
                            
                            'val2Rel': [None,['id', 'nome'],  ['id','nome'], None, None, None, None],
                            'fldRelTblMain': [None, 'ref_tiplocal','ref_geometric', None, None, None, None],
                            'sizeCol':[80, 200, 200, 200, 125, 125, 50],
                            'sizeForm':[937, 617],
                            }
        
        self.dictSimpel=    {
                            'fldName': ["id", "nome","descricao", "comentario", "activo"],
                            'headerTitle': ['Cod.', 'Nome', 'Descricao', 'Comentarios', 'Activo'],
                            'lstToHide':[True, False, True, True, False],
                            'fldToQuote': [True, True, True, True, False],
                            
                            'val2Rel': [None, None, None, None, None],
                            'fldRelTblMain': [None, None, None, None, None],
                            'sizeCol':[50, 450, 200, 200, 50],
                            'sizeForm':[937, 617],
                            }
        
        self.dictTipLocal= {
                            'fldName': ["id", "id_nivel",  "nome",  "descricao", "comentario", "activo"],
                            'headerTitle': ["Cod.", "Nivel", "Nome", "Descricao", "Comentarios", "Activo"],
                            'lstToHide':[True, False, False, True, True, False],
                            'fldToQuote': [True, True, True, True, True,  False],
                            
                            'val2Rel': [None, ['id','nome'],None, None, None,None],
                            'fldRelTblMain': [None, 'ref_nivel', None, None, None, None],
                            'sizeCol':[100, 250, 250, 120, 120, 50],
                            'sizeForm':[937, 617],
                            }

        self.dictTables=    {
                            'fldName': ["id", "id_grupo", "nome", "descricao", "comentario", "activo"],
                            'headerTitle': ['Cod.', "Grupo", 'Nome', 'Descricao', 'Comentarios', 'Activo'],
                            'lstToHide':[True, False, False, True, True, False],
                            'fldToQuote': [True, True, True, True, True, False],
                            
                            'val2Rel': [None, ['id', 'nome'], None, None, None, None], 
                            'fldRelTblMain':[None, 'ref_grupo', None, None, None, None],
                            'condTbl': 'ref_grupo',
                            'condCol': ['id','nome'],
                            'condName': 'activo',
                            'condVal': True,
                            'condToQuote': False,
                            'sizeCol':[80, 200, 400, 140, 140, 50],
                            'sizeForm':[937, 617],
                            }  
        
        self.dictIntClass= {
                            'fldName': ["id", "id_especie",  "intervalo", "comentario", "activo"],
                            'headerTitle': [ "Cod.", "Especie", "Intevalo", "Comentarios", "Activo"],
                            'lstToHide':[True, False, False, True, False],
                            'fldToQuote': [False, True, True, True,False ],
                            
                            'val2Rel': [None, ['id','nome'],None, None, None],
                            'fldRelTblMain': [None, 'ref_especies', None, None, None, None],
                            'sizeCol':[50, 400, 180, 200, 100],
                            'sizeForm':[937, 617],
                            }   
        
        self.dictUniPescaTipo= {
                            'fldName': ["id",  "nome", "id_arte", "id_tipbarco", "activo", "descricao"],
                            'headerTitle': ["Cod.","Nome", "Arte", "Tipo de barco", "Activo", "Descricao"],
                            'lstToHide':[True, False, False, False, False, True],
                            'fldToQuote': [True, True, True, True, False, True],
                            
                            'val2Rel': [None, None,['id','nome'], ['id','nome'],None, None],
                            'fldRelTblMain': [None, None, 'ref_artes', 'ref_table',None, None],
                            'sizeCol':[100, 250, 170, 170, 100, 50],
                            'sizeForm':[937, 617],
                            }
                            
    def setMainDict(self):
        '''
        Metodo para definir um dicionar principal que ira ajudar no manuzeamento de dados
        e que permitira configurar o form a nossa maneira, os pop outs e a vizualizacao de dados 
        '''
        self.dictMain = {
                        'fldDlgDict' : [self.dictSimpel, self.dictArtes, self.dictDiaSemana, self.dictEspecies, 
                                        self.dictGeometric, self.dictSimpel, self.dictTables, self.dictTipLocal, 
                                        self.dictPesquerio, self.dictRegistador, self.dictUniPescaTipo, self.dictIntClass],
                         
                        'formLabelName' : ['Codificadores', 'Artes', 'Dias da Semana', 'Especies', ' Geometric', 'Nivel', 'Codificador ', 
                                           'Tipo de Local', 'Pesqueiro', 'Registador', 'Tipo de Unidade Pesca', 'Intervalo de Class'],
                        
                        'toHideGrupo': [True, True, True, True, True, True, False, True, True, True, True, True],
                        
                        'dlgToPop': [dlg_simpel, dlg_artes, dlg_diasemana, dlg_especies, dlg_geometric, dlg_simpel, dlg_tabela, dlg_tiplocal, 
                                     dlg_pesqueiros, dlg_registadores, dlg_UniPescaTipo, dlg_intClass],
                        
                        'tblName': ['ref_grupo', 'ref_artes', 'ref_diasemana', 'ref_especies', 'ref_geometric', 'ref_nivel', 'ref_table', 
                                    'ref_tiplocal', 'ref_pesqueiro', 'ref_registador', 'ref_unidpescatipo', 'ref_intervalo_class'],
                            
                        'fldFiltro':["ref_grupo.nome LIKE '%{nome}%'", "ref_artes.nome LIKE '%{nome}%'", "ref_diasemana.nome LIKE '%{nome}%'", "ref_especies.species LIKE '%{nome}%'",
                                     "ref_geometric.nome LIKE '%{nome}%'", "ref_nivel.nome LIKE '%{nome}%'", "id_grupo = '{combox}' and ref_table.nome LIKE '%{nome}%'", 
                                     "ref_tiplocal.nome LIKE '%{nome}%'", "ref_pesqueiro.nome LIKE '%{nome}%'", "ref_registador.nome LIKE '%{nome}%'", "ref_unidpescatipo.nome LIKE '%{nome}%'",
                                     "ref_intervalo_class.comentarios = ref_intervalo_class.comentarios"]
                        } 


    
    def setDictSecurity(self):
        '''
        Definimos os widgets que estarao bloqueados para cada user level
        
        '''
        self.dictLocked= {
                        '0':[self.PBAdicionar, self.PBEditar],
                        '1':[self.PBAdicionar, self.PBEditar],
                        '10':None,
                        '99':None
                        }
