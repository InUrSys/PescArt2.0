'''
Created on 11/12/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QModelIndex, QComboBox
import rscForm
import mixedModel
from GenericReferenciasQDialog import GenericReferencias_
import FuncSQL
import QT_msg
import Rules
class sub_GenericReferencias_Geometric(GenericReferencias_):
    
    
    def setIDFromCB(self):
        self.dictCBX={
                'quer':["SELECT id, nome from ref_geometric where id_tiplocal = 'PIS';",
                        "select null as id, '-Provincia-' as nome",
                        "select null as id, '-Distrito-' as nome",
                        "select null as id, '-Posto Administrativo-' as nome",
                        "select null as id, '-Centros Existentes-' as nome"],
                'widget':[self.CBPais ,self.CBProvincia, self.CBDistrito, self.CBPostoAdmin, self.CBCentroPesca]
                }
        #rscForm.setReadOnlyAll(state= True, lstWidg= dictCB['widget'])
        tipLocal = mixedModel.getDataCombox(widg = self.CBTipLocal)
        self.LBid.setText(tipLocal)
        if tipLocal == 'PRV':
            self.dictCBX['quer'][0] = "select null as id, '-Provincia-' as nome union all SELECT id, nome from ref_geometric where id_tiplocal = 'PRV' and id_parent = 'PISMZ'";
        elif tipLocal == 'DST':
            self.dictCBX['quer'][1] = "select null as id, '-Provincia-' as nome union all SELECT id, nome from ref_geometric where id_tiplocal = 'PRV' and id_parent = 'PISMZ'";
            self._configCombox()
            self.CBProvincia.currentIndexChanged.connect(self.setLocal_part1)
        elif tipLocal == 'PSD':
            self.dictCBX['quer'][1] = "select null as id, '-Provincia-' as nome union all select id, nome from ref_geometric where id_tiplocal = 'PRV' and id_parent = 'PISMZ'";
            self._configCombox()
            self.CBProvincia.currentIndexChanged.connect(self.setLocal_part1)
        elif tipLocal == 'CTP':
            self.dictCBX['quer'][1] = "select null as id, '-Provincia-' as nome union all select id, nome from ref_geometric where id_tiplocal = 'PRV' and id_parent = 'PISMZ'";
            self._configCombox()
            self.CBProvincia.currentIndexChanged.connect(self.setLocal_part1)
        else:
            pass
        #Set to default as like null or somethinf 
    
    def setLocal_part1(self):
        tipLocal = mixedModel.getDataCombox(widg = self.CBTipLocal)
        if tipLocal == 'DST':
            prov = mixedModel.getDataCombox(widg = self.CBProvincia)
            self.dictCBX['quer'][2] = "select null as id, '-Distrito-' as nome union all SELECT id, nome from ref_geometric where id_tiplocal = 'DST' and id_parent = '{prov}'".format(prov = prov);
            self._configCombox(index=2)
        elif tipLocal == 'PSD':
            prov = mixedModel.getDataCombox(widg = self.CBProvincia)
            self.dictCBX['quer'][2] = "select null as id, '-Distrito-' as nome union all SELECT id, nome from ref_geometric where id_tiplocal = 'DST' and id_parent = '{prov}'".format(prov = prov);
            self._configCombox(index=2)
            self.CBDistrito.currentIndexChanged.connect(self.setLocal_part2)
        elif tipLocal == 'CTP':
            prov = mixedModel.getDataCombox(widg = self.CBProvincia)
            self.dictCBX['quer'][2] = "select null as id, '-Distrito-' as nome union all SELECT id, nome from ref_geometric where id_tiplocal = 'DST' and id_parent = '{prov}'".format(prov = prov);
            self._configCombox(index=2)
            self.CBDistrito.currentIndexChanged.connect(self.setLocal_part2)
    
    def setLocal_part2(self):
        tipLocal = mixedModel.getDataCombox(widg = self.CBTipLocal)
        if tipLocal == 'PSD':
            dist = mixedModel.getDataCombox(widg = self.CBDistrito)
            self.dictCBX['quer'][3] = "select null as id, '-Posto administrativo-' as nome union all select id, nome from ref_geometric where id_tiplocal = 'PSD' and id_parent = '{dist}'".format(dist = dist);
            self._configCombox(index=3)
            
        if tipLocal == 'CTP':
            dist = mixedModel.getDataCombox(widg = self.CBDistrito)
            self.dictCBX['quer'][3] = "select null as id, '-Posto administrativo-' as nome union all select id, nome from ref_geometric where id_tiplocal = 'PSD' and id_parent = '{dist}'".format(dist = dist);
            self._configCombox(index=3)
            self.CBPostoAdmin.currentIndexChanged.connect(self.setLocal_part3)
            
    def setLocal_part3(self):
        tipLocal = mixedModel.getDataCombox(widg = self.CBTipLocal)
        if tipLocal == 'CTP':     
            posto = mixedModel.getDataCombox(widg = self.CBPostoAdmin)
            self.dictCBX['quer'][4] = "select null as id, '-Centros Existentes-' as nome union all select id, nome from ref_geometric where id_tiplocal = 'CTP' and id_parent = '{posto}'".format(posto = posto);
            self._configCombox(index=4)
            
        
    'Centro de Pesca', 
    def toEdit(self):
        if isinstance(self.mIdx, QModelIndex):
            row = self.mIdx.row()
            model = self.mIdx.model()
            column = model.columnCount()
            lstWdg = self.dictFields['lstWidget']
            for idx in range(column):
                val = model.record(row).value(idx)
                if idx == 2: 
                    tpl= model.record(row).value(1)
                    self.setLocalizacao(nome= val, tipoLocal= tpl)
                else:
                    rscForm.setTxtToWidget(widget=lstWdg[idx], val=val)
            self.splitInID()
        self.LECodigo.setMaxLength(6)
        
    
    def _configCombox(self, index=0):
        '''
        Metodo para configurar o Modelo e Text Hint no Combox.
        '''
        lstWdgt = self.dictCBX['widget']
        lstQuer = self.dictCBX['quer']
        limit = len(lstWdgt)
        for idx in range(index, limit):
            val = lstWdgt[idx]
            model = mixedModel.setQueryModel(lstQuer[idx])
            val.setModel(model)
            val.setModelColumn(1)
            self.CBTextHint(Combox=val)
        
        
    def setLocalizacao(self, nome=None, tipoLocal=None):
        '''
        Metodo para Settar localizacao nos comboxs 
        da provincia ate o centro de pesca.
        '''
        if tipoLocal== 'Centro de Pesca':
            bOK, lstIn = self.getLocalizacao_Posto(nomePosto = nome)
        elif tipoLocal== 'Posto Administrativo':
            bOK, lstIn = self.getLocalizacao_Distrio(nomeDistrito = nome)
        elif tipoLocal == 'Distrito':
            bOK, lstIn = self.getLocalizacao_Provincia(nomeProvincia = nome)
        else:
            bOK = False
        if bOK:
            lstWdiget = [self.CBProvincia, self.CBDistrito, self.CBPostoAdmin, self.CBCentroPesca]
            for idx, val in enumerate(lstWdiget):
                rscForm.setTxtToWidget(widget=val, val=lstIn[idx])
                
                

    def getLocalizacao_Posto(self, nomePosto=None):
        '''
        Metodo para Extrair a localizacao atraves do Nome Do local do local e 
        Retornado uma lista que vai ser usada para settar a localicao Artraves da provincia 
        ate o local de pesca.
        '''
        scrpt = ''' SELECT prov.nome, dist.nome, posto.nome, '-Centros Existentes-'
                    FROM public.ref_geometric as posto 
                    inner join ref_geometric as dist on posto.id_parent = dist.id
                    inner join ref_geometric as prov on dist.id_parent = prov.id
                    where posto.id_tiplocal= 'PSD' and posto.nome = '{nomePosto}' '''.format(nomePosto= nomePosto)
        bOK, lstOut = FuncSQL.anySelectScript(scpt=scrpt)
        return bOK, lstOut
    
    def getLocalizacao_Distrio(self, nomeDistrito=None):
        '''
        Metodo para Extrair a localizacao atraves do Nome Do local do local e 
        Retornado uma lista que vai ser usada para settar a localicao Artraves da provincia 
        ate o local de pesca.
        '''
        scrpt = ''' SELECT prov.nome, dist.nome, '-Posto Administrativo-', '-Centros Existentes-'
                    FROM public.ref_geometric as dist 
                    inner join ref_geometric as prov on dist.id_parent = prov.id
                    where dist.id_tiplocal= 'DST' and dist.nome = '{nomeDistrito}' '''.format(nomeDistrito= nomeDistrito)
        bOK, lstOut = FuncSQL.anySelectScript(scpt=scrpt)
        return bOK, lstOut
    
    def getLocalizacao_Provincia(self, nomeProvincia=None):
        '''
        Metodo para Extrair a localizacao atraves do Nome Do local do local e 
        Retornado uma lista que vai ser usada para settar a localicao Artraves da provincia 
        ate o local de pesca.
        '''
        scrpt = ''' SELECT prov.nome, '-Distrito-', '-Posto Administrativo-', '-Centros Existentes-'
                    FROM public.ref_geometric as prov 
                    where prov.id_tiplocal= 'PRV' and prov.nome = '{nomeProv}' '''.format(nomeProv= nomeProvincia)
        bOK, lstOut = FuncSQL.anySelectScript(scpt=scrpt)
        return bOK, lstOut
        
      
    def pre_operacao(self):
        try:
            tblName= self.tblName
            lstName= self.dictFields['lstName']
            lstQuot= self.dictFields['lstToQuote']
            if self.mIdx is not None:
                cond = self.dictFields['lstName'][0]
                getId= lambda mIdx: mIdx.model().record(mIdx.row()).value(0)
                conVal = getId(self.mIdx)
                condQuot = self.dictFields['lstToQuote'][0]
            else:
                cond = None
                conVal = None
                condQuot = None
            bOK, lstVal = self.getValues()
        except:
            bOK = False
        if bOK:
            if lstVal[1] == 'CTP':
                lstVal[2] = mixedModel.getDataCombox(widg= self.CBPostoAdmin)
            elif lstVal[1] == 'PSD':
                lstVal[2] = mixedModel.getDataCombox(widg= self.CBDistrito)
            elif lstVal[1] == 'DST':
                lstVal[2] = mixedModel.getDataCombox(widg= self.CBProvincia)
            else:
                bOK = False
                QT_msg.aviso(txt= 'Aviso voce nao pode introduzir uma Nova <b>Provincia</b> ou <b>Pais</b>')
        if bOK:
            self._operacao(tblName= tblName, lstNames= lstName, lstVals= lstVal, lstQuot =lstQuot, cond=cond, conVal=conVal, condQuot=condQuot)
        else:
            lstNotNull=self.dictFields['lstDefault']
            for idx, val in enumerate(self.dictFields['lstWidget']):
                if lstNotNull[idx] is False and idx!=2:
                    self._warning(widgt=val)
            QT_msg.aviso(txt="PorFavor reveja os dados que esta para ser inseridos e certifique-se que os campos Amarelos estao todos preenchidos e nao Estao repetidos")
    
    