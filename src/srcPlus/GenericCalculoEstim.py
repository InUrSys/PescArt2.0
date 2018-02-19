'''
Created on 24/11/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QStandardItemModel, QStandardItem, QComboBox,\
    QModelIndex
import mixedModel
import QT_tblViewUtility
import CustomWidgets
import FuncSQL
import searchSimple
import pprint
class GenericCalculoEstim(QDialog):
    
    def CBTextHint(self, Combox=None):
        mdel = QStandardItemModel(Combox.model())
        firstIndex = mdel.index(0, Combox.modelColumn(), Combox.rootModelIndex())
        firstItem = QStandardItem(mdel.itemFromIndex(firstIndex))
        firstItem.setSelectable(False)
    
    def setCB(self):
        lstquer = ["select null as id, '-ANO-' as nome UNION all (select distinct data_ano, cast (data_ano as text) as d_ano from view_ano_mes order by data_ano)",
                   "select null as id, '-ANO-' as nome UNION all (select distinct data_ano, cast (data_ano as text) as d_ano from view_ano_mes order by data_ano)",
                   "select null as id, '-Agrupamento-' as nome UNION all (select mes_num, nome from prc_agrupamentos order by mes_num)",
                   "select null as id, '-Tipo de Dia-' as nome union all select id, nome from ref_table where id_grupo = 'TPD'",
                   "select null as id, '-Periodo do Dia-' as nome union all SELECT id, nome FROM public.prc_periodo_dia;"]
            
        lstWdg = [self.CBAno_inicio, self.CBAno_Fim, self.CBAgrupamento, self.CBTipDia, self.CBPeriodoDia] 
        for idx, val in enumerate (lstWdg):
            model = mixedModel.setQueryModel(query = lstquer[idx])
            val.setModel(model)
            val.setModelColumn(1)    
    
    def openToSearch(self):
        dictlstwdg= {
                    'TBEspecies':[self.CBEspecie, "select nome from ref_especies ", "select id from ref_especies where nome = '{nome}'"],
                    'TBSexo': [self.CBSexo, "select nome from ref_table where id_grupo = 'SEX'", "select id from ref_table where id_grupo = 'SEX' and nome = '{nome}'"]
                    }
        val = dictlstwdg.get(self.sender().objectName())
        if val is not None:
            bOK, rsModel = FuncSQL.multLineSelect(scpt= val[1])
            model = CustomWidgets.modelWithCheck_search(lstResult=rsModel )
            if val[0].count() > 0:
                lstIn = self.getALLItemFromCB(cb=val[0])
                popSearch = searchSimple.simpleSearch(lastSelected= lstIn ,model=model)
            else:
                popSearch = searchSimple.simpleSearch(model=model)
            popSearch.exec_()
            if popSearch.close():
                bOK, lstIn =  popSearch.bOK
                if bOK:
                    lstID = []
                    val[0].clear()
                    val[0].addItems(lstIn)
                    for nome in lstIn:
                        bok, Id = FuncSQL.anySelectScript(scpt= val[2].format(nome = nome))
                        if bok:
                            lstID.append(Id)
                        
                
    def getALLItemFromCB(self, cb=None):
        rows = cb.count()
        lstOut = []
        for i in range(rows):
            val = cb.itemText(i)
            lstOut.append(val)
        return lstOut
    
    
    def setAgruToDefault(self):
        self.CBAgrupamento.setCurrentIndex(0)
    
    
    def setTView(self):
        for idx, val in enumerate(self.dictTblView ['lstquer']):
            View= self.dictTblView ['lstView'][idx]
            Size= self.dictTblView ['size'][idx]
            Hide= self.dictTblView ['toHide'][idx]
            model = mixedModel.setQueryModel(query= val) 
            QT_tblViewUtility.setViewCustom(tblView= View, lstSizeCol=Size)
            QT_tblViewUtility.setModelInView(tblView= View, ViewModel = model, toHide=Hide) 
            
        
    def setCBMes(self, val=-99):
        quer = "select null, '-MES-' UNION all select  cast (data_mes as text), mes_nome from view_ano_mes where data_ano = {inicioAno}".format(inicioAno= val)
        model = mixedModel.setQueryModel(query = quer)
        dictlstWdg= {self.CBAno_inicio.objectName(): self.CBMes_inicio, 
                     self.CBAno_Fim.objectName(): self.CBMes_Fim
                    }
        val = dictlstWdg.get(self.sender().objectName())
        if val is not None:
            val.setModel(model)
            val.setModelColumn(1)
                    
        
    def getVal_Combox(self):
        val = mixedModel.getDataCombox(widg=self.sender())
        self.setCBMes(val= val)
           
    
    def getAllToCalculo(self):
        lstAno = self.getAno() #Ano inicio e Fim
        lstMes_Agru_tipDia = self.getMes_Agru_tipDia() #Mes Inicio, Fim, Agrupamento, Tipo de Dia
        lstPeriodo = self.getPeriodo() #Periodo
        lstEspe_Sexo = self.getEspe_Sexo() # Lista Especies, Lista Sexo
        lstArte_Catego = self.getArtes_Categ()
        

        pprint.pprint(lstAno)
        pprint.pprint(lstMes_Agru_tipDia)
        pprint.pprint(lstPeriodo)
        pprint.pprint(lstEspe_Sexo)
        pprint.pprint(lstArte_Catego)
        
        
    def getAno(self):
        lstWdg = [self.CBAno_inicio, self.CBAno_Fim]
        lstOut = []
        for val in (lstWdg):
            if val.currentIndex() != 0:
                ano = val.currentText()
                lstOut.append(ano)
        return lstOut
    
    
    def getMes_Agru_tipDia(self):
        lstWdg = [self.CBMes_inicio, self.CBMes_Fim, self.CBAgrupamento, self.CBTipDia]
        lstOut = []
        for idx, val in enumerate (lstWdg):
            if val.currentIndex() != 0:
                txtOut = mixedModel.getDataCombox(widg= val)
                tpOut = [txtOut,val.currentText()]
                lstOut.append(tpOut)
        return lstOut
    
    
    def getPeriodo(self):
        wdg = self.CBPeriodoDia
        quer = "SELECT id, nome, inicio, fim FROM public.prc_periodo_dia where nome like '{nome}';"
        lstOut =None
        if wdg.currentIndex() != 0:
            nome = wdg.currentText()
            bOK,lstIn = FuncSQL.anySelectScript(scpt=quer.format(nome = nome))
            if bOK:
                lstOut = lstIn
        return lstOut
            
            
    def getEspe_Sexo(self):
        dDict = {
                'widget':[self.CBEspecie, self.CBSexo],
                'query':["SELECT id, nome FROM public.ref_especies where nome like '{nome}';", 
                         "SELECT id, nome FROM public.ref_table where id_grupo like 'SEX' and nome like '{nome}';"]
                }
        lstQuer = dDict['query']
        lstWdg = dDict['widget']
        lstOut = [[],[]]
        for idx, val in enumerate (lstWdg):
            bOK=False
            if val == self.CBEspecie:
                if self.RBTodos.isChecked():
                    quer = "SELECT id, nome FROM public.ref_especies;"
                    bOK, lstIn = FuncSQL.multLineSelect(scpt= quer)
                else:
                    rows = val.count()
                    if rows > 0:
                        for i in range(rows):
                            txtIn = val.itemText(i)
                            bOK, lstIn = FuncSQL.anySelectScript(scpt= lstQuer[idx].format(nome=txtIn))
            else:
                rows = val.count()
                if rows > 0:
                    for i in range(rows):
                        txtIn = val.itemText(i)
                        bOK, lstIn = FuncSQL.anySelectScript(scpt= lstQuer[idx].format(nome=txtIn))
            if bOK:
                lstOut[idx].append(lstIn)
        return lstOut
                    
            
    def getArtes_Categ(self):
        lstClicked = [self.arteClicked, self.categoriaClicked]
        lstOut=[]
        for val in lstClicked:
            if val is not None:
                row = val.row()
                model = val.model()
                valOut = [model.record(row).value(0), model.record(row).value(1)]
                lstOut.append(valOut)
        return lstOut
                
            
            
                
        
        
        
        
     
    