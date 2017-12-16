'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_AmostCompSexo import Ui_frmAmostCompSexo
import decimal
import GenericAmostrasQDialog
import mixedModel
import FuncSQL
import QT_msg
from PyQt5.Qt import QComboBox

class dialog_AmostCompSexo(GenericAmostrasQDialog.CustomForm_Amostras, Ui_frmAmostCompSexo):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None, lstValToEdit=None ,dictRules = None):
        super(dialog_AmostCompSexo, self).__init__(parent)
        self.setupUi(self)
        
        self.N_Sequencial_Parent = str(Id)
        self.tblName = TblName
        self.lstToEdit = lstValToEdit
        self.dictRules = dictRules
        self.setDict()
        self.bOK= (False, None)
        self.lastChecked = None
        self.configWidgetTriggeredEvent()
        self.configRules()
        self.configKeepTrack(id_parente=Id)
        self.configCombox()
        self.setValuesToEdit()
        self.CBEspecies.currentIndexChanged.connect(self.setIntClass)
        self.setEspecie()
        self.CBIntervaloClass.currentTextChanged.connect(self.compMinSetup)
        self.compMinSetup()
        self.PBSalvar.clicked.connect(self._operacao)
        self.PBCancelar.clicked.connect(self.close)
    
    def setEspecie(self):
        quer = '''select tbl4.nome from t_comp_sexo tbl1 
                inner join t_amost_comp_especifica as tbl2 on tbl1.id_amost_comp_especifica = tbl2.id
                inner join t_comp_especifica as tbl3 on tbl2.id_comp_especifica = tbl3.id
                inner join ref_especies as tbl4 on tbl3.id_especie = tbl4.id
                where tbl1.id = {id} '''.format(id=self.N_Sequencial_Parent)
        bOK, especie = FuncSQL.anySelectScript(scpt=quer)
        if bOK:
            self.CBEspecies.setCurrentText(especie[0])
        
    def setIntClass(self):
        dataOut = mixedModel.getDataCombox(widg=self.CBEspecies)
        if dataOut is not None: 
            quer = "SELECT intervalo  FROM public.ref_intervalo_class where id_especie = '{id}' and activo = True".format(id = dataOut)
            bOK, mOut = FuncSQL.multLineSelect(scpt=quer)
            if bOK:
                for val in mOut:
                    self.CBIntervaloClass.addItem(str(val[0]))
                
        
    def compMinSetup(self):
        val = 0
        if self.CBIntervaloClass.currentText() == '':
            QT_msg.aviso(txt='A Especie nao tem Intervalo de Class defenida, sera artbuido o intervalo de <b>0.5</b> a <b>1.0</b> por padrao')
            lst = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
            for i in(lst):
                self.CBIntervaloClass.addItem(str(i))
                self.CBIntervaloClass.setCurrentText('0.5')
        else:
            intClass = decimal.Decimal(self.CBIntervaloClass.currentText())
            newVal = (val+intClass)
            self.DBSCompMinimo.setSingleStep(newVal)
    
    
    def _operacao(self):
        '''
        salvar
        '''
        bOK= self.formValid()
        if bOK:
            lstName= self.dictFields['fldName']
            lstQuot= self.dictFields['toQuote']
            lstVal=  self.getValues()
            lstVal[6]= self.CBIntervaloClass.currentText()
            if self.lstToEdit is None:
                bOK, msgOut= FuncSQL.insertVal(tblName= self.tblName, lstNames=lstName, lstVal= lstVal, lstQuot= lstQuot)
            else:
                cond= 'id'
                conVal= self.lstToEdit[0]
                condQuot= False
                lstVal[0]= self.lstToEdit[0]
                bOK, msgOut= FuncSQL.updateVal(tblName= self.tblName, lstNames=lstName, lstVals= lstVal, lstQuot= lstQuot, cond= cond, conVal= conVal, condQuot= condQuot)
            if bOK:
                self.bOK= (bOK, msgOut)
                self.close()
            else:
                self.bOK= (bOK, None)
    
    
    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_comp_sexo", "id_metodo_select", "id_medida_comp", "id_aproxima",
                                      "id_intervalo_class", "comp_minimo", "peso", "n_indiv", "comentario", "id_especie"],
                          
                        'fldWidget': [None, None, self.CBMetodoSelec, self.CBMedidaComp, self.CBAproximacao,
                                      self.CBIntervaloClass, self.DBSCompMinimo, self.DSBPeso, self.SB_N_indiv_amostrados, self.LEComentarios, self.CBEspecies ],
                    
                        'objName': ['id', 'id_amost_amost_espe', 'CBMetodoSelec', 'CBMedidaComp', 'CBAproximacao',
                                    'CBIntervaloClass', 'DBSCompMinimo', 'DSBPeso', 'SB_N_indiv_amostrados', 'LEComentarios', 'CBEspecies'],
                        
                        'isRel':[False, False, True, True, True, False, False, False, False, False, True],
                        
                        'toDefault':[False, False, False, False, False, False, False, False, False, True, False],
                        
                        'toCheck': [False, False, True, True, True, True, True, True, True, True, False],
                        
                        "toQuote":[False, False, True, True, True, True, True, True, False, True, True]
                         }
        
        self.dictCB= {
                        'quer':["select null as id, '-Metodo de Selecao-' as nome union all select id, nome from ref_table where id_grupo = 'MTS' and activo =true;",
                                "select null as id, '-Medida de Comprimento-' as nome union all select id, nome from ref_table where id_grupo = 'MDC' and activo =true;",
                                "select null as id, '-Aproximacao-' as nome union all select id, nome from ref_table where id_grupo = 'APM' and activo =true;",
                                "select null as id, '-Especies-' as nome union all select id, nome from ref_especies where activo =true;"],
                        
                        'widget':[self.CBMetodoSelec, self.CBMedidaComp, self.CBAproximacao, self.CBEspecies]
                      }
        
        
