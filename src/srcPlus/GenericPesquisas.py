'''
Created on 13/12/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QModelIndex, QStandardItemModel, QStandardItem,\
    QGroupBox
import mixedModel
import QT_tblViewUtility
import rscForm
class GenericPesquisas(QDialog):
    
    
    
    def configCombox(self):
        '''
        Metodo para configurar o Modelo e Text Hint no Combox.
        '''
        lstWdgt = self.dictCB['widget']
        lstQuer = self.dictCB['quer']
        for idx, val in enumerate (lstWdgt):
            model = mixedModel.setQueryModel(lstQuer[idx])
            val.setModel(model)
            val.setModelColumn(1)
            self.CBTextHint(Combox=val)
    
    
    def CBTextHint(self, Combox=None):
        mdel = QStandardItemModel(Combox.model())
        firstIndex = mdel.index(0, Combox.modelColumn(), Combox.rootModelIndex())
        firstItem = QStandardItem(mdel.itemFromIndex(firstIndex))
        firstItem.setSelectable(False)
        
    
    def configComboxLocal(self):
        '''
        Configurar o combox e o evento
        '''
        lstWdgt = [self.CBProvincia, self.CBDistrito, self.CBPosto, self.CBCentroPesca]
        for wdg in lstWdgt:
            wdgName = wdg.objectName()
            query= self.dictLocal[wdgName]['query']
            model= mixedModel.setQueryModel(query= query)
            wdg.setModel(model)
            wdg.setModelColumn(1)
            self.CBTextHint(Combox=wdg)
            wdg.currentTextChanged.connect(self.updateNextCombo)
        
        
    def updateNextCombo(self):
        '''
        Atualiza o modelo do Next widget 
        '''
        wdgt= self.sender().objectName() 
        setNext= self.dictLocal[wdgt]['nextLVL']
        if setNext is not None:
            query= self.dictLocal[setNext]['query'].format(val = mixedModel.getDataCombox(widg= self.sender()))
            nextWdg = self.dictLocal[setNext]['wdgt']
            nextWdgModel= nextWdg.model()
            nextWdgModel.setQuery(query)
            nextWdg.setCurrentIndex(0)
            self.CBTextHint(Combox=self.dictLocal[setNext]['wdgt'])
            
    def configRegistador(self):
        if self.CBProvincia.currentIndex() == 0:
            quer= "select null as id, '-Registador-' as nome union all select id, nome from ref_registador"
        else:
            id_prov = mixedModel.getDataCombox(widg= self.CBProvincia)
            quer = "select null as id, '-Registador-' as nome union all select id, nome from ref_registador where id_centro = '{prov}'".format(prov = id_prov)
        model = mixedModel.setQueryModel(query =quer)
        self.CBRegistador.setModel(model)
        self.CBRegistador.setModelColumn(1)
        
        
    def buldingTheQuery(self):
        startQuery = """SELECT tbl1.id, date(data_amostragem) as "Data da Amostra", tbl2.nome as "Centro", tbl3.nome as "Registador",
                        hora_inicioamo, hor_fimamo, tbl4.nome as "Dia da Semana", tbl5.nome as "Forca do Vento", tbl6.nome as "Nivel da Mare", 
                        tbl7.nome as "Direcao do Vento", hora_vento, tbl8.nome as "Tipo de Mare", altura_preamar, hora_preamar, altura_baimar, 
                        hora_baixamar, tbl9.nome as "Fase da Lua", tbl10.nome as "Nebulosidade", hora_nebulosidade, actividade_pesq, 
                        total_artes_amos, total_artes_act, total_artes_n_activas, total_artes_prov_outo_cent, observacoes
                        FROM public.t_saidas as tbl1
                        left join ref_geometric as tbl2
                        on tbl1.id_centro = tbl2.id and tbl2.id_tiplocal = 'CTP'
                        left join ref_registador as tbl3
                        on tbl1.id_registrador = tbl3.id
                        left join ref_diasemana as tbl4
                        on tbl1.id_diasemana = tbl4.id  
                        left join ref_table as tbl5
                        on tbl1.id_forcavento = tbl5.id and tbl5.id_grupo = 'FCV'
                        left join ref_table as tbl6
                        on tbl1.id_estadomare = tbl6.id and tbl6.id_grupo = 'NVM'
                        left join ref_table as tbl7 
                        on tbl1.id_direccao = tbl7.id and tbl7.id_grupo = 'DDV'
                        left join ref_table as tbl8
                        on tbl1.id_tipomare = tbl8.id and tbl8.id_grupo = 'TPM'
                        left join ref_table as tbl9
                        on tbl1.id_faselua = tbl9.id and tbl9.id_grupo = 'FLD'
                        left join ref_table as tbl10
                        on tbl1.id_nebulosidade = tbl10.id and tbl10.id_grupo = 'NBL' """#BigQuery and start Where
        #
        #
        if self.CBProvincia.currentIndex() != 0:
            startQuery += " where "
            if self.CBDistrito.currentIndex() != 0:
                if self.CBPosto.currentIndex() != 0:
                    if self.CBCentroPesca.currentIndex() != 0:
                        ctp = mixedModel.getDataCombox(widg= self.CBCentroPesca)
                        startQuery +=   "tbl1.id_centro in (select tbl1.id from ref_geometric as tbl1 where tbl1.id = '{ctp}')".format(ctp = ctp)
                    else:
                        psd = mixedModel.getDataCombox(widg= self.CBPosto)
                        startQuery +=   """ tbl1.id_centro in (select tbl1.id from ref_geometric as tbl1 
                                            inner join ref_geometric as tbl2
                                            on tbl1.id_parent = tbl2.id
                                            where tbl2.id like '{psd}') """.format(psd = psd)
                else:
                    dst = mixedModel.getDataCombox(widg= self.CBDistrito)
                    startQuery +=       """ tbl1.id_centro in (select tbl1.id from ref_geometric as tbl1 
                                            inner join ref_geometric as tbl2
                                            on tbl1.id_parent = tbl2.id
                                            inner join ref_geometric as tbl3 
                                            on tbl2.id_parent = tbl3.id
                                            where tbl3.id like '{dst}') """.format(dst = dst)
            else:
                prv = mixedModel.getDataCombox(widg= self.CBProvincia)
                startQuery +=           """ tbl1.id_centro in (select tbl1.id from ref_geometric as tbl1 
                                            inner join ref_geometric as tbl2
                                            on tbl1.id_parent = tbl2.id
                                            inner join ref_geometric as tbl3 
                                            on tbl2.id_parent = tbl3.id
                                            inner join ref_geometric as tbl4
                                            on tbl3.id_parent = tbl4.id
                                            where tbl4.id like '{prv}') """.format(prv = prv)
        #
        #
        if self.GBData.isChecked():
            if self.CBProvincia.currentIndex(): #!= 0 or self.CBRegistador.currentIndex() != 0 or self.CBDiaSemana.currentIndex() != 0 or self.CBActividadePesqueria.currentIndex() != 0:
                startQuery += ' and '  
            else:
                startQuery += " where "
            inicio = rscForm.getText(widg = self.DEInicio)
            fim =  rscForm.getText(widg = self.DEFim)
            startQuery += "data_amostragem  between '{inicio}' and '{fim}' ".format(inicio=inicio, fim=fim)
        #
        #
        if self.CBRegistador.currentIndex() != 0:
            if self.CBProvincia.currentIndex() != 0 or self.GBData.isChecked():#or self.CBDiaSemana.currentIndex() != 0 or self.CBActividadePesqueria.currentIndex() != 0:
                startQuery += ' and '
            else:
                startQuery += " where "
            rgt = mixedModel.getDataCombox(widg= self.CBRegistador)
            startQuery += "tbl3.id = '{rgt}' ".format(rgt = rgt)
        #
        #
        if self.CBDiaSemana.currentIndex() != 0:
            if self.CBProvincia.currentIndex() != 0 or self.GBData.isChecked() or self.CBRegistador.currentIndex() != 0:# or self.CBActividadePesqueria.currentIndex() != 0:
                startQuery += ' and '
            else:
                startQuery += " where "
            dsm = mixedModel.getDataCombox(widg= self.CBDiaSemana)
            startQuery += "tbl4.id = '{dsm}' ".format(dsm = dsm)
        #
        #
        if self.CBActividadePesqueria.currentIndex() != 0:
            if self.CBProvincia.currentIndex() != 0 or self.GBData.isChecked() or self.CBRegistador.currentIndex() != 0 or self.CBDiaSemana.currentIndex() != 0:
                startQuery += ' and '
            else:
                startQuery += " where "
            quer = mixedModel.getDataCombox(widg = self.CBActividadePesqueria)
            startQuery += quer
        #
        #
        endQuery = " order by tbl1.data_amostragem ;"#ORder by Data 
        startQuery += endQuery
        lstName = self.dictSaidas['newNames']
        model = mixedModel.setQueryModel(query= startQuery, lstNewNames= lstName)
        toHide = self.dictSaidas['toHide']
        lstSizeCol = self.dictSaidas['sizeCol']
        QT_tblViewUtility.setModelInView(tblView= self.TVSaidas, ViewModel= model, toHide = toHide)
        QT_tblViewUtility.setViewCustom(tblView=self.TVSaidas, lstSizeCol=lstSizeCol)
    
    
    def selectedRow(self, mIdx):
        lstOut=[]
        lenDict = len(self.dictSaidas['fldName'])
        model = mIdx.model()
        clickedRow = mIdx.row()
        for idx in range(lenDict):
            val = model.record(clickedRow).value(idx)
            lstOut.append(val)
        self.lstVal= lstOut
        self.bOK = True
        
        