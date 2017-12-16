
'''
Created on 08/11/2017
@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog
from keepTrack_ToView import Ui_Form
import FuncSQL
import rscForm
class KeepTrack(QDialog, Ui_Form):
    def __init__(self, parent= None, dbcon=None, idx=None):
        super(KeepTrack, self).__init__(parent)
        self.setupUi(self)
        
        self.dbcon = dbcon
        self.idx = idx
        self.setKTtoView()
        
    def getTheData(self):
        if self.idx is not None:
            quer='''select 
                    DATE(saida.data_amostragem), centro.nome, registador.nome,
                    centro2.nome, artenome.nome,
                    viagem.id_unipesca, tipunipesca.nome, 
                    categoria.nome,
                    metodo0.nome
                    from t_amost_desem_cat_comercial as amostcat
                    inner join t_desem_cat_comercial as catcomercial on amostcat.id_desem_cat_comercial = catcomercial.id
                    left join ref_table as metodo0 on amostcat.id_metodo_select = metodo0.id
                    inner join t_lance_pesca as lance on  catcomercial.id_lance_pesca = lance.id
                    left join ref_table as categoria on catcomercial.id_categoria = categoria.id
                    inner join t_viagem_pesca as viagem on lance.id_viagem_pesca = viagem.id
                    left join ref_unidpescatipo as tipunipesca on viagem.id_tip_uni_pesca = tipunipesca.id
                    inner join t_activ_tip_unidade as arte on viagem.id_activ_tip_unidade = arte.id
                    inner join t_saidas as saida on arte.id_saida = saida.id
                    left join ref_geometric as centro2 on arte.id_centro = centro2.id
                    left join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                    left join ref_geometric as centro on saida.id_centro = centro.id
                    left join ref_registador as registador on saida.id_registrador = registador.id
                    where amostcat.id = {id}'''.format(id= self.idx)
                    
            bOK, lstOut = FuncSQL.anySelectScript(scpt=quer)
            if bOK == False:
                lstOut = None
        else:
            bOK =False
            lstOut=None
        return bOK, lstOut
    
    
    def setKTtoView(self):
        bOK, lstOut = self.getTheData()
        if bOK:
            val= lstOut
            mainDict = {
                        'data':(self.DEData, val[0]),
                        'centro':(self.LECentro, val[1]),
                        'registador':(self.LERegistador, val[2]),
                        'centroArte':(self.LECentroOrigem, val[3]),
                        'arte':(self.LEArte, val[4]),
                        'embarcao':(self.LEEmbarcacao, val[5]),
                        'tip_uni_pesca':(self.LETipPescaUnidade, val[6]),
                        'categoria':(self.LECatComercial, val[7]),
                        'metodo':(self.LEMetodoSelec, val[8]),
                        }
            
            for wdg, itsVal in mainDict.values():
                rscForm.setTxtToWidget(widget=wdg, val=itsVal)
            
           
                
    