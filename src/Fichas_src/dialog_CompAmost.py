'''
Created on 05/09/2017

@author: chernomirdinmacuvele
'''

from ui_compAmostra  import Ui_frmDistComprimento
from PyQt5.Qt import QSpinBox, QDialog, QDoubleSpinBox, QSqlQuery
import FuncSQL
import rscForm
import WhatLog
import QT_msg
class dialog_CompAmost(QDialog, Ui_frmDistComprimento):
    def __init__(self, parent=None, TblName=None, dbcon=None, Id=None, lstValToEdit=None, dictRules = None):  
        super(dialog_CompAmost, self).__init__(parent)
        self.setupUi(self)   
        
        self.rowCount= 100#Ler do ficherio de configuracao
        self.dbcon =dbcon
        self.tblName = TblName
        self.lstToEdit = lstValToEdit
        self.dictRules = dictRules
        self.Id = Id
        self.isEdit = False
        self.setLines()
        self.bOK= (False, None)
    
        self.PBSalvar.clicked.connect(self.toSave)
        self.PBCancelar.clicked.connect(self.close)
        
    
    def getAmostSexo(self):
        quer= """
                SELECT ref_table.nome, round ( cast(id_intervalo_class as numeric), 2)as int_class,
                comp_minimo, peso, n_indiv
                FROM public.t_amost_comp_sexo
                left join public.ref_table on  t_amost_comp_sexo.id_medida_comp = ref_table.id
                where t_amost_comp_sexo.id= {Id}
                """.format(Id= self.Id)
        bOK, lstOut= FuncSQL.anySelectScript(scpt=quer)
        if bOK:
            medida, intClass, compMinimo, peso, n_indiv = lstOut[0], lstOut[1], lstOut[2], lstOut[3], lstOut[4]
        else:
            medida, intClass, compMinimo, peso, n_indiv = None, None, None, None, None
        return medida, intClass, compMinimo, peso, n_indiv
    
    
    def toEdit(self):
        quer = "SELECT class_comp, n_indiv from public.t_comp_amost where id_amost_comp_sexo= {id_amost_comp_sexo} ".format(id_amost_comp_sexo=self.Id)
        bOK, lstOut= FuncSQL.multLineSelect(scpt=quer)
        if bOK:
            if lstOut != []:
                self.isEdit = True
                for val in lstOut:
                    for row in range(self.rowCount):
                        tstDBSpin = QDoubleSpinBox()
                        tstDBSpin.setValue(float(val[0]))
                        newVal = rscForm.getText(widg= tstDBSpin)
                        item_0 = rscForm.getText(widg= self.TWComprimentos.cellWidget(row, 0))
                        if item_0 == newVal:
                            wdg1= self.TWComprimentos.cellWidget(row, 1)
                            rscForm.setTxtToWidget(widget=wdg1, val=val[1])
                              

    def setLines(self):
        _, intClass, compMini, _, _ = self.getAmostSexo()
        if intClass is not None and compMini is not None:
            mini = float(compMini)
            intClass = float(intClass)
            
            self.TWComprimentos.setRowCount(self.rowCount)
            for row in range(self.rowCount):
                spinBox = QSpinBox() #Criando objecto Spin e double box
                doubleSpin = QDoubleSpinBox()
                if row == 0:
                    idx = mini
                else:
                    idx = mini + (row * intClass) #formula para determinar o valor inicial
                doubleSpin.setMinimum(idx)
                doubleSpin.setReadOnly(True)
                self.TWComprimentos.setCellWidget(row, 0, doubleSpin)#Configurando os valores nas possicoes
                self.TWComprimentos.setCellWidget(row, 1, spinBox)
            self.toEdit()   
        
    
    def getVal(self):
        lstOut=[]
        for val in range(self.rowCount):
            item_0 = rscForm.getText(widg= self.TWComprimentos.cellWidget(val, 0))
            item_1 = self.TWComprimentos.cellWidget(val, 1).text()
            if int(item_1) > 0:
                lstOut.append((item_0, item_1))
        return lstOut
    
    
    def toSave(self):
        lstIn = self.getVal()
        lstInserted= []
        for val in lstIn:
            bOK, idx =FuncSQL.getLast(tblName=self.tblName)
            newLast = int(idx)+1
            if bOK:
                classeCom, n_indiv = val
                dictVal = {'id': newLast,
                           'id_amost_comp_sexo':self.Id,
                           'class_comp':classeCom,
                           'n_indiv':n_indiv
                        }
                quer =  '''INSERT INTO public.t_comp_amost
                            (id, id_amost_comp_sexo, class_comp, n_indiv)
                            VALUES ({id}, {id_amost_comp_sexo}, '{class_comp}', {n_indiv});'''.format(**dictVal)
                WhatLog.whatHappen(info=quer)
                toSave = QSqlQuery()
                bOK = toSave.exec_(quer)
                if bOK == False:
                    lstInserted.append(dictVal)
        bOK, msgOut = self.vefSaved(lstdictIN= lstInserted)
        self.bOK = bOK, msgOut
        self.close()
    
    
    def vefSaved(self, lstdictIN=None):
        toSave = QSqlQuery()
        bOK=True
        msgOut= "Operacao Realizada Com sucesso"
        for dictIN in lstdictIN:
            quer = "SELECT id_amost_comp_sexo, class_comp, n_indiv from public.t_comp_amost where class_comp= '{class_comp}' and id_amost_comp_sexo= {id_amost_comp_sexo} ".format(**dictIN)
            WhatLog.whatHappen(info=quer)
            _, lstOut = FuncSQL.anySelectScript(scpt= quer)
            if lstOut[0] == dictIN['id_amost_comp_sexo'] and lstOut[1] == dictIN['class_comp'] and lstOut[2] == dictIN['n_indiv']:
                bOK =True
            elif lstOut[0] == dictIN['id_amost_comp_sexo'] and lstOut[1] != dictIN['class_comp'] or lstOut[2] != dictIN['n_indiv']:
                quer= ''' UPDATE public.t_comp_amost SET n_indiv= {n_indiv}
                         WHERE class_comp= '{class_comp}' and id_amost_comp_sexo= {id_amost_comp_sexo};'''.format(**dictIN)
                bOK = toSave.exec_(quer)
                WhatLog.whatHappen(info=quer)
                
            else:
                bOK =False
                vTxt= toSave.lastError().text()
                QT_msg.error(txt='Error Nao sera possivel realizar a opercao', verbTxt=vTxt)
                WhatLog.errorHappen(info=vTxt)
                msgOut=None
                break
        return bOK, msgOut

        
        
        
    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_comp_sexo", "class_comp", "n_indiv"],
                        'fldWidget':[None, None, self.DSBClass_comp, self.DSBN_indiv_Medidos],
                        'toDefault':[False, False, False, False],
                        'objName': ['id', 'id_comp_sexo', 'DSBClass_comp', 'DSBN_indiv_Medidos'],
                        'isRel':[False, False, False, False],
                        'toCheck': [False, False, True, True],
                        "toQuote":[False, False, True, True]
                         }
                
    

