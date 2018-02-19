'''
Created on 22/01/2018

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog
from ui_Keep_Track_Artes_Pesca_ToView import Ui_Form 
import FuncSQL
import rscForm
import mixedModel


class toView_Keep_track_ArtesPesca(QDialog, Ui_Form):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None):
        super(toView_Keep_track_ArtesPesca, self).__init__(parent)
        self.setupUi(self)
        
        self.dbcon = dbcon
        self.mIDx = Id
        self.setModel4Mapper()
        
        self.PBDown.clicked.connect(self.NextData)
        self.PBUp.clicked.connect(self.prevData)
    
    def getTheData(self):
        quer='''select saida.id from t_activ_tip_unidade as arte
                    inner join t_saidas as saida on arte.id_saida = saida.id
                    left join ref_geometric as centro2 on arte.id_centro = centro2.id
                    left join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                    left join ref_geometric as centro on saida.id_centro = centro.id
                    left join ref_registador as registador on saida.id_registrador = registador.id
                    where arte.id = {id}'''.format(id= self.mIDx.model().record(self.mIDx.row()).value(0))
        bOK, lstOut = FuncSQL.anySelectScript(scpt=quer)
        if bOK == False:
            lstOut = None
        return bOK, lstOut
    
    
    def setModel4Mapper(self):
        fldToMap = [None, self.DEData, self.LECentro, self.LERegistador, self.LECentroOrigem, self.LEArte, self.SBAmostradas]
        bOK, lstOut = self.getTheData()
        if bOK:
            val= lstOut
            saidaID = val[0]
            quer='''select 
                    arte.id, DATE(saida.data_amostragem), centro.nome, registador.nome,
                    centro2.nome, artenome.nome, arte.n_amostradas
                    from t_activ_tip_unidade as arte
                    inner join t_saidas as saida on arte.id_saida = saida.id
                    left join ref_geometric as centro2 on arte.id_centro = centro2.id
                    left join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                    left join ref_geometric as centro on saida.id_centro = centro.id
                    left join ref_registador as registador on saida.id_registrador = registador.id
                    where saida.id = {id}'''.format(id= saidaID)
            model = mixedModel.setQueryModel(query=quer)
            mixedModel.withWidgets.setMapper(self, model= model, fldToMap=fldToMap)
            mixedModel.withWidgets.setMapperToIdx(self, idx= self.mIDx.row())
    
    
    def NextData(self):
        mixedModel.withWidgets.mapperToNext(self)
        self.setNextModel()
        
        
    def prevData(self):
        mixedModel.withWidgets.mapperToPerv(self)
        self.setNextModel()
        
        
    def setNextModel(self):
        curID, row = mixedModel.withWidgets.getValueFromMapper(self)
        self.parent().parent().DictGridLay['ItemClicked'][0] = (curID, row)
        self.parent().parent().updateModelOnNextView()
        
    def getData(self):
        curID, row = mixedModel.withWidgets.getValueFromMapper(self)
        return (curID, row)
    
        
