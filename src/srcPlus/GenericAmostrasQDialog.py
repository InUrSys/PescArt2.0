'''
Created on 21/10/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QComboBox, QPlainTextEdit, QCheckBox, QGroupBox,\
    QTimer
import FuncSQL
import QT_msg
import rscForm
import mixedModel
import Rules
import QT_widgetsCustom
from PyQt5.Qt import QStandardItemModel, QStandardItem
from dateutil.tz import tzlocal

class CustomFrm(QDialog):
    '''
    Esta class tem como objectivo herdar todos metodos do QDialog e servira para
    minimizar as funcoes comuns em todas elas, sem ter que rescrever elas.
    -confRules -> para configurar as regras
    '''

    def     configRules(self):
        '''
        ''' 
        frmName = self.objectName()
        if self.dictRules.get(frmName) is not None:
            self.rules = self.dictRules.get(frmName)
        else:
            self.rules=None
            
            
    def _getKeepTrackQuery(self, frmName=None):
        '''
        ''' 
        _dictQuey={
                    "frmSaidas": None,
                    
                    
                    "frmArtesPesca":'''select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome
                                    from t_saidas as saida
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where saida.id = {id};''',
                    
                    "frmFactores": '''select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome
                                    from t_saidas as saida
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where saida.id = {id};''',
                                    
                    "frmViagemPesca": """select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome,
                                    arte.id_centro, centro2.nome, arte.id_tip_uni_pesca, artenome.nome
                                    from t_activ_tip_unidade as arte
                                    inner join t_saidas as saida on arte.id_saida = saida.id
                                    inner join ref_geometric as centro2 on arte.id_centro = centro2.id
                                    inner join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where arte.id = {id};""",
                    
                    "frmLancesPesca": """select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome,
                                    arte.id_centro, centro2.nome, arte.id_tip_uni_pesca, artenome.nome,
                                    viagem.n_lances_amostrados, viagem.n_lances_totais, viagem.cap_total
                                    from t_viagem_pesca as viagem
                                    inner join t_activ_tip_unidade as arte on viagem.id_activ_tip_unidade = arte.id
                                    inner join t_saidas as saida on arte.id_saida = saida.id
                                    inner join ref_geometric as centro2 on arte.id_centro = centro2.id
                                    inner join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where viagem.id = {id}""" ,
        
                    "frmCatComercialAmostra": """select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome,
                                    arte.id_centro, centro2.nome, arte.id_tip_uni_pesca, artenome.nome,
                                    viagem.n_lances_amostrados, viagem.n_lances_totais, viagem.cap_total,
                                    lance.cap_total_peso, lance.hora_inicio, lance.hora_fim
                                    from t_lance_pesca as lance
                                    inner join t_viagem_pesca as viagem on lance.id_viagem_pesca = viagem.id
                                    inner join t_activ_tip_unidade as arte on viagem.id_activ_tip_unidade = arte.id
                                    inner join t_saidas as saida on arte.id_saida = saida.id
                                    inner join ref_geometric as centro2 on arte.id_centro = centro2.id
                                    inner join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where lance.id = {id}""",
        
                    "frmAmostCatComercial": """select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome,
                                    arte.id_centro, centro2.nome, arte.id_tip_uni_pesca, artenome.nome,
                                    viagem.n_lances_amostrados, viagem.n_lances_totais, viagem.cap_total,
                                    lance.cap_total_peso, lance.hora_inicio, lance.hora_fim,
                                    catcomercial.id_categoria, categoria.nome
                                    from t_desem_cat_comercial as catcomercial
                                    inner join t_lance_pesca as lance on  catcomercial.id_lance_pesca = lance.id
                                    inner join ref_table as categoria on catcomercial.id_categoria = categoria.id
                                    inner join t_viagem_pesca as viagem on lance.id_viagem_pesca = viagem.id
                                    inner join t_activ_tip_unidade as arte on viagem.id_activ_tip_unidade = arte.id
                                    inner join t_saidas as saida on arte.id_saida = saida.id
                                    inner join ref_geometric as centro2 on arte.id_centro = centro2.id
                                    inner join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where catcomercial.id = {id}""" ,
    
                    "frmEspeciesAmostradas": """select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome,
                                    arte.id_centro, centro2.nome, arte.id_tip_uni_pesca, artenome.nome,
                                    viagem.n_lances_amostrados, viagem.n_lances_totais, viagem.cap_total,
                                    lance.cap_total_peso, lance.hora_inicio, lance.hora_fim,
                                    catcomercial.id_categoria, categoria.nome,
                                    amostcat.id_metodo_select, metodo0.nome, amostcat.peso
                                    from t_amost_desem_cat_comercial as amostcat
                                    inner join t_desem_cat_comercial as catcomercial on amostcat.id_desem_cat_comercial = catcomercial.id
                                    inner join ref_table as metodo0 on amostcat.id_metodo_select = metodo0.id
                                    inner join t_lance_pesca as lance on  catcomercial.id_lance_pesca = lance.id
                                    inner join ref_table as categoria on catcomercial.id_categoria = categoria.id
                                    inner join t_viagem_pesca as viagem on lance.id_viagem_pesca = viagem.id
                                    inner join t_activ_tip_unidade as arte on viagem.id_activ_tip_unidade = arte.id
                                    inner join t_saidas as saida on arte.id_saida = saida.id
                                    inner join ref_geometric as centro2 on arte.id_centro = centro2.id
                                    inner join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where amostcat.id = {id}""" ,
        
                    "frmAmostEspeEspecieAmost": """select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome,
                                    arte.id_centro, centro2.nome, arte.id_tip_uni_pesca, artenome.nome,
                                    viagem.n_lances_amostrados, viagem.n_lances_totais, viagem.cap_total,
                                    lance.cap_total_peso, lance.hora_inicio, lance.hora_fim,
                                    catcomercial.id_categoria, categoria.nome,
                                    amostcat.id_metodo_select, metodo0.nome, amostcat.peso,
                                    especifica.id_especie, especie.species
                                    from t_comp_especifica as especifica
                                    inner join t_amost_desem_cat_comercial as amostcat on especifica.id_amost_desem_cat_comercial = amostcat.id
                                    inner join ref_especies as especie on especifica.id_especie = especie.id
                                    inner join t_desem_cat_comercial as catcomercial on amostcat.id_desem_cat_comercial = catcomercial.id
                                    inner join ref_table as metodo0 on amostcat.id_metodo_select = metodo0.id
                                    inner join t_lance_pesca as lance on  catcomercial.id_lance_pesca = lance.id
                                    inner join ref_table as categoria on catcomercial.id_categoria = categoria.id
                                    inner join t_viagem_pesca as viagem on lance.id_viagem_pesca = viagem.id
                                    inner join t_activ_tip_unidade as arte on viagem.id_activ_tip_unidade = arte.id
                                    inner join t_saidas as saida on arte.id_saida = saida.id
                                    inner join ref_geometric as centro2 on arte.id_centro = centro2.id
                                    inner join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where especifica.id = {id}""" ,
                                                
                    "frmAmostSexo": """select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome,
                                    arte.id_centro, centro2.nome, arte.id_tip_uni_pesca, artenome.nome,
                                    viagem.n_lances_amostrados, viagem.n_lances_totais, viagem.cap_total,
                                    lance.cap_total_peso, lance.hora_inicio, lance.hora_fim,
                                    catcomercial.id_categoria, categoria.nome,
                                    amostcat.id_metodo_select, metodo0.nome, amostcat.peso,
                                    especifica.id_especie, especie.species,
                                    amostespecifica.id_metodo_select, metodo1.nome, amostespecifica.peso
                                    from t_amost_comp_especifica as amostespecifica
                                    inner join t_comp_especifica as especifica on amostespecifica.id_comp_especifica = especifica.id
                                    inner join ref_table as metodo1 on amostespecifica.id_metodo_select = metodo1.id
                                    inner join t_amost_desem_cat_comercial as amostcat on especifica.id_amost_desem_cat_comercial = amostcat.id
                                    inner join ref_especies as especie on especifica.id_especie = especie.id
                                    inner join t_desem_cat_comercial as catcomercial on amostcat.id_desem_cat_comercial = catcomercial.id
                                    inner join ref_table as metodo0 on amostcat.id_metodo_select = metodo0.id
                                    inner join t_lance_pesca as lance on  catcomercial.id_lance_pesca = lance.id
                                    inner join ref_table as categoria on catcomercial.id_categoria = categoria.id
                                    inner join t_viagem_pesca as viagem on lance.id_viagem_pesca = viagem.id
                                    inner join t_activ_tip_unidade as arte on viagem.id_activ_tip_unidade = arte.id
                                    inner join t_saidas as saida on arte.id_saida = saida.id
                                    inner join ref_geometric as centro2 on arte.id_centro = centro2.id
                                    inner join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where amostespecifica.id = {id}""" ,
                                    
                    "frmAmostCompSexo": """select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome,
                                    arte.id_centro, centro2.nome, arte.id_tip_uni_pesca, artenome.nome,
                                    viagem.n_lances_amostrados, viagem.n_lances_totais, viagem.cap_total,
                                    lance.cap_total_peso, lance.hora_inicio, lance.hora_fim,
                                    catcomercial.id_categoria, categoria.nome,
                                    amostcat.id_metodo_select, metodo0.nome, amostcat.peso,
                                    especifica.id_especie, especie.species,
                                    amostespecifica.id_metodo_select, metodo1.nome, amostespecifica.peso,
                                    compsexo.id_sexo, sexo.nome
                                    from t_comp_sexo as compsexo
                                    inner join t_amost_comp_especifica as amostespecifica on compsexo.id_amost_comp_especifica = amostespecifica.id
                                    inner join ref_table as sexo on compsexo.id_sexo=sexo.id
                                    inner join t_comp_especifica as especifica on amostespecifica.id_comp_especifica = especifica.id
                                    inner join ref_table as metodo1 on amostespecifica.id_metodo_select = metodo1.id
                                    inner join t_amost_desem_cat_comercial as amostcat on especifica.id_amost_desem_cat_comercial = amostcat.id
                                    inner join ref_especies as especie on especifica.id_especie = especie.id
                                    inner join t_desem_cat_comercial as catcomercial on amostcat.id_desem_cat_comercial = catcomercial.id
                                    inner join ref_table as metodo0 on amostcat.id_metodo_select = metodo0.id
                                    inner join t_lance_pesca as lance on  catcomercial.id_lance_pesca = lance.id
                                    inner join ref_table as categoria on catcomercial.id_categoria = categoria.id
                                    inner join t_viagem_pesca as viagem on lance.id_viagem_pesca = viagem.id
                                    inner join t_activ_tip_unidade as arte on viagem.id_activ_tip_unidade = arte.id
                                    inner join t_saidas as saida on arte.id_saida = saida.id
                                    inner join ref_geometric as centro2 on arte.id_centro = centro2.id
                                    inner join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where compsexo.id = {id}""" ,
        
                    "frmDistComprimento": """select 
                                    DATE(saida.data_amostragem), saida.id_centro, centro.nome, saida.id_registrador, registador.nome,
                                    arte.id_centro, centro2.nome, arte.id_tip_uni_pesca, artenome.nome,
                                    viagem.n_lances_amostrados, viagem.n_lances_totais, viagem.cap_total,
                                    lance.cap_total_peso, lance.hora_inicio, lance.hora_fim,
                                    catcomercial.id_categoria, categoria.nome,
                                    amostcat.id_metodo_select, metodo0.nome, amostcat.peso,
                                    especifica.id_especie, especie.species,
                                    amostespecifica.id_metodo_select, metodo1.nome, amostespecifica.peso,
                                    compsexo.id_sexo, sexo.nome,
                                    amostsexo.id_metodo_select, metodo2.nome, comp_minimo
                                    from t_amost_comp_sexo as amostsexo
                                    inner join t_comp_sexo as compsexo on amostsexo.id_comp_sexo = compsexo.id
                                    inner join ref_table as metodo2 on amostsexo.id_metodo_select = metodo2.id
                                    inner join t_amost_comp_especifica as amostespecifica on compsexo.id_amost_comp_especifica = amostespecifica.id
                                    inner join ref_table as sexo on compsexo.id_sexo=sexo.id
                                    inner join t_comp_especifica as especifica on amostespecifica.id_comp_especifica = especifica.id
                                    inner join ref_table as metodo1 on amostespecifica.id_metodo_select = metodo1.id
                                    inner join t_amost_desem_cat_comercial as amostcat on especifica.id_amost_desem_cat_comercial = amostcat.id
                                    inner join ref_especies as especie on especifica.id_especie = especie.id
                                    inner join t_desem_cat_comercial as catcomercial on amostcat.id_desem_cat_comercial = catcomercial.id
                                    inner join ref_table as metodo0 on amostcat.id_metodo_select = metodo0.id
                                    inner join t_lance_pesca as lance on  catcomercial.id_lance_pesca = lance.id
                                    inner join ref_table as categoria on catcomercial.id_categoria = categoria.id
                                    inner join t_viagem_pesca as viagem on lance.id_viagem_pesca = viagem.id
                                    inner join t_activ_tip_unidade as arte on viagem.id_activ_tip_unidade = arte.id
                                    inner join t_saidas as saida on arte.id_saida = saida.id
                                    inner join ref_geometric as centro2 on arte.id_centro = centro2.id
                                    inner join ref_unidpescatipo as artenome on arte.id_tip_uni_pesca = artenome.id
                                    inner join ref_geometric as centro on saida.id_centro = centro.id
                                    inner join ref_registador as registador on saida.id_registrador = registador.id
                                    where amostsexo.id = {id} """ 
                    }
        if _dictQuey.get(frmName) is not None:
            queryOut = _dictQuey.get(frmName)
            bOK = True
        else:
            bOK = False
            queryOut =None
        return (bOK, queryOut)
    
            
            
    def _getQueryValues(self, queryResult=None, frmName=None):
        '''
        ''' 
        bOK =True
        if "frmSaidas" == frmName:
            dictOut = {None}
            
        elif "frmArtesPesca" == frmName:
            dictOut = { 
            'KT_dataSaida':queryResult[0],
            'KT_id_centroOrigem':queryResult[1],
            'KT_centroOrigem':queryResult[2],
            'KT_id_registador':queryResult[3],
            'KT_registador':queryResult[4]
            }
        
        elif "frmFactores" == frmName:
            dictOut = { 
            'KT_dataSaida':queryResult[0],
            'KT_id_centroOrigem':queryResult[1],
            'KT_centroOrigem':queryResult[2],
            'KT_id_registador':queryResult[3],
            'KT_registador':queryResult[4]
            }
            
        elif "frmViagemPesca" == frmName:
            dictOut = {
            'KT_dataSaida':queryResult[0],
            'KT_id_centroOrigem':queryResult[1],
            'KT_centroOrigem':queryResult[2],
            'KT_id_registador':queryResult[3],
            'KT_registador':queryResult[4],
            'KT_id_centroOrigemArte':queryResult[5],
            'KT_centroOrigemArte':queryResult[6],
            'KT_id_artes':queryResult[7],
            'KT_arte':queryResult[8]
                    }
        
        elif "frmLancesPesca" == frmName:
            dictOut = { 
                'KT_dataSaida':queryResult[0],
                'KT_id_centroOrigem':queryResult[1],
                'KT_centroOrigem':queryResult[2],
                'KT_id_registador':queryResult[3],
                'KT_registador':queryResult[4],
                'KT_id_centroOrigemArte':queryResult[5],
                'KT_centroOrigemArte':queryResult[6],
                'KT_id_artes':queryResult[7],
                'KT_arte':queryResult[8],
                'KT_n_lancesAmost':queryResult[9],
                'KT_n_lancesTotal':queryResult[10],
                'KT_viagem_capTotal':queryResult[11]
                }
        
        elif "frmCatComercialAmostra" == frmName:
            dictOut = { 
                'KT_dataSaida':queryResult[0],
                'KT_id_centroOrigem':queryResult[1],
                'KT_centroOrigem':queryResult[2],
                'KT_id_registador':queryResult[3],
                'KT_registador':queryResult[4],
                'KT_id_centroOrigemArte':queryResult[5],
                'KT_centroOrigemArte':queryResult[6],
                'KT_id_artes':queryResult[7],
                'KT_arte':queryResult[8],
                'KT_n_lancesAmost':queryResult[9],
                'KT_n_lancesTotal':queryResult[10],
                'KT_viagem_capTotal':queryResult[11],
                'KT_lance_capTotal':queryResult[12],
                'KT_inicio':queryResult[13],
                'KT_fim':queryResult[14]
                }
        
        elif "frmAmostCatComercial" == frmName:
            dictOut = { 
                'KT_dataSaida':queryResult[0],
                'KT_id_centroOrigem':queryResult[1],
                'KT_centroOrigem':queryResult[2],
                'KT_id_registador':queryResult[3],
                'KT_registador':queryResult[4],
                'KT_id_centroOrigemArte':queryResult[5],
                'KT_centroOrigemArte':queryResult[6],
                'KT_id_artes':queryResult[7],
                'KT_arte':queryResult[8],
                'KT_n_lancesAmost':queryResult[9],
                'KT_n_lancesTotal':queryResult[10],
                'KT_viagem_capTotal':queryResult[11],
                'KT_lance_capTotal':queryResult[12],
                'KT_inicio':queryResult[13],
                'KT_fim':queryResult[14],
                'KT_id_categorai':queryResult[15],
                'KT_categoria':queryResult[16]
                }
        
        elif "frmEspeciesAmostradas" == frmName:
            dictOut = { 
                'KT_dataSaida':queryResult[0],
                'KT_id_centroOrigem':queryResult[1],
                'KT_centroOrigem':queryResult[2],
                'KT_id_registador':queryResult[3],
                'KT_registador':queryResult[4],
                'KT_id_centroOrigemArte':queryResult[5],
                'KT_centroOrigemArte':queryResult[6],
                'KT_id_artes':queryResult[7],
                'KT_arte':queryResult[8],
                'KT_n_lancesAmost':queryResult[9],
                'KT_n_lancesTotal':queryResult[10],
                'KT_viagem_capTotal':queryResult[11],
                'KT_lance_capTotal':queryResult[12],
                'KT_inicio':queryResult[13],
                'KT_fim':queryResult[14],
                'KT_id_categorai':queryResult[15],
                'KT_categoria':queryResult[16],
                'KT_amostCat_id_metodo':queryResult[17],
                'KT_amostCat_metodo':queryResult[18],
                'KT_amostCat_peso':queryResult[19]
                
                }
        
        elif "frmAmostEspeEspecieAmost" == frmName:
            dictOut = { 
                'KT_dataSaida':queryResult[0],
                'KT_id_centroOrigem':queryResult[1],
                'KT_centroOrigem':queryResult[2],
                'KT_id_registador':queryResult[3],
                'KT_registador':queryResult[4],
                'KT_id_centroOrigemArte':queryResult[5],
                'KT_centroOrigemArte':queryResult[6],
                'KT_id_artes':queryResult[7],
                'KT_arte':queryResult[8],
                'KT_n_lancesAmost':queryResult[9],
                'KT_n_lancesTotal':queryResult[10],
                'KT_viagem_capTotal':queryResult[11],
                'KT_lance_capTotal':queryResult[12],
                'KT_inicio':queryResult[13],
                'KT_fim':queryResult[14],
                'KT_id_categorai':queryResult[15],
                'KT_categoria':queryResult[16],
                'KT_amostCat_id_metodo':queryResult[17],
                'KT_amostCat_metodo':queryResult[18],
                'KT_amostCat_peso':queryResult[19],
                'KT_id_especies':queryResult[20],
                'KT_especies':queryResult[21]
                }
        
        elif "frmAmostSexo" == frmName:
            dictOut = { 
                'KT_dataSaida':queryResult[0],
                'KT_id_centroOrigem':queryResult[1],
                'KT_centroOrigem':queryResult[2],
                'KT_id_registador':queryResult[3],
                'KT_registador':queryResult[4],
                'KT_id_centroOrigemArte':queryResult[5],
                'KT_centroOrigemArte':queryResult[6],
                'KT_id_artes':queryResult[7],
                'KT_arte':queryResult[8],
                'KT_n_lancesAmost':queryResult[9],
                'KT_n_lancesTotal':queryResult[10],
                'KT_viagem_capTotal':queryResult[11],
                'KT_lance_capTotal':queryResult[12],
                'KT_inicio':queryResult[13],
                'KT_fim':queryResult[14],
                'KT_id_categorai':queryResult[15],
                'KT_categoria':queryResult[16],
                'KT_amostCat_id_metodo':queryResult[17],
                'KT_amostCat_metodo':queryResult[18],
                'KT_amostCat_peso':queryResult[19],
                'KT_id_especies':queryResult[20],
                'KT_especies':queryResult[21],
                'KT_amostEsp_id_metodo':queryResult[22],
                'KT_amostEsp_metodo':queryResult[23],
                'KT_amostEsp_peso':queryResult[24]
                }
            
        elif "frmAmostCompSexo" == frmName:
            dictOut = { 
                'KT_dataSaida':queryResult[0],
                'KT_id_centroOrigem':queryResult[1],
                'KT_centroOrigem':queryResult[2],
                'KT_id_registador':queryResult[3],
                'KT_registador':queryResult[4],
                'KT_id_centroOrigemArte':queryResult[5],
                'KT_centroOrigemArte':queryResult[6],
                'KT_id_artes':queryResult[7],
                'KT_arte':queryResult[8],
                'KT_n_lancesAmost':queryResult[9],
                'KT_n_lancesTotal':queryResult[10],
                'KT_viagem_capTotal':queryResult[11],
                'KT_lance_capTotal':queryResult[12],
                'KT_inicio':queryResult[13],
                'KT_fim':queryResult[14],
                'KT_id_categorai':queryResult[15],
                'KT_categoria':queryResult[16],
                'KT_amostCat_id_metodo':queryResult[17],
                'KT_amostCat_metodo':queryResult[18],
                'KT_amostCat_peso':queryResult[19],
                'KT_id_especies':queryResult[20],
                'KT_especies':queryResult[21],
                'KT_amostEsp_id_metodo':queryResult[22],
                'KT_amostEsp_metodo':queryResult[23],
                'KT_amostEsp_peso':queryResult[24],
                'KT_id_sexo':queryResult[25],
                'KT_sexo':queryResult[26]
                }
        
        elif "frmDistComprimento" == frmName:
            dictOut = { 
                'KT_dataSaida':queryResult[0],
                'KT_id_centroOrigem':queryResult[1],
                'KT_centroOrigem':queryResult[2],
                'KT_id_registador':queryResult[3],
                'KT_registador':queryResult[4],
                'KT_id_centroOrigemArte':queryResult[5],
                'KT_centroOrigemArte':queryResult[6],
                'KT_id_artes':queryResult[7],
                'KT_arte':queryResult[8],
                'KT_n_lancesAmost':queryResult[9],
                'KT_n_lancesTotal':queryResult[10],
                'KT_viagem_capTotal':queryResult[11],
                'KT_lance_capTotal':queryResult[12],
                'KT_inicio':queryResult[13],
                'KT_fim':queryResult[14],
                'KT_id_categorai':queryResult[15],
                'KT_categoria':queryResult[16],
                'KT_amostCat_id_metodo':queryResult[17],
                'KT_amostCat_metodo':queryResult[18],
                'KT_amostCat_peso':queryResult[19],
                'KT_id_especies':queryResult[20],
                'KT_especies':queryResult[21],
                'KT_amostEsp_id_metodo':queryResult[22],
                'KT_amostEsp_metodo':queryResult[23],
                'KT_amostEsp_peso':queryResult[24],
                'KT_id_sexo':queryResult[25],
                'KT_sexo':queryResult[26],
                'KT_amostSexo_id_metodo':queryResult[27],
                'KT_amostSexo_metodo':queryResult[28],
                'KT_amostSexo_intervalo':queryResult[29],
                'KT_amostSexo_compMinimo':queryResult[30]
                }
        else:
            bOK = False
            dictOut =None
        return (bOK, dictOut)
    
    
    def configKeepTrack(self, id_parente=-99):
        '''
        ''' 
        frmName = self.objectName()
        bOK, query = self._getKeepTrackQuery(frmName)
        if bOK:
            query =query.format(id=id_parente)
            bOK, queryResult = FuncSQL.anySelectScript(scpt=query)
            if bOK:
                self.dictKeepTrack = {}
                bOK, dictOut = self._getQueryValues(queryResult=queryResult, frmName=frmName)
                if bOK:
                    self.dictKeepTrack = dictOut
        else:
            QT_msg.aviso(txt="Aviso Error ao recaregar as regras!\nAs Regras Nao Foram Activadas Porfavor Renicie a Pagina")

    
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
        try:
            self.configComboxLocal()
        except AttributeError:
            pass
        
    
    def getValues(self):
        '''
        ''' 
        self.setDefault()
        lstWidg = self.dictFields['fldWidget']
        lstRel = self.dictFields['isRel']
        lstVal = rscForm.getTextAll(lstWidg)
        try:
            if self.N_Sequencial_Parent is not None:
                lstVal[1]= str(self.N_Sequencial_Parent)
        except AttributeError:
            pass
        for idx, val in enumerate(lstRel):
            if val:
                lstVal[idx]= str(mixedModel.getDataCombox(widg=lstWidg[idx]))
        return lstVal 
    
    
    def configWidgetTriggeredEvent(self):
        '''
        ''' 
        lstToCheck = self.dictFields['toCheck']
        lstWidget = self.dictFields['fldWidget']
        for idx, val in enumerate(lstToCheck):
            if val:
                if lstWidget[idx] is not None:
                    if (not isinstance(lstWidget[idx], QGroupBox)) and (not isinstance(lstWidget[idx], QComboBox)) and (not isinstance(lstWidget[idx], QPlainTextEdit)) and (not isinstance(lstWidget[idx], QCheckBox)):
                        lstWidget[idx].editingFinished.connect(self._triggeredEventFinish)
    
    
    def _triggeredEventFinish(self):
        '''
        '''
        wdgObj = self.sender()
        currentWdgName = self.sender().objectName()
        currentWdgVal = rscForm.getText(widg= wdgObj)
        if self.lastChecked is not None:
            lastWdgName, lastWdgVal = self.lastChecked
            if currentWdgName == lastWdgName and currentWdgVal == lastWdgVal:
                self.sender().setFocus()
                return None
            elif currentWdgName != lastWdgName:
                return None
        self._validatingWidget(wdgObj=wdgObj, wdgName=currentWdgName, wdgVal=currentWdgVal)
    
    
    def _validatingWidget(self, wdgObj=None, wdgName=None, wdgVal=None):
        '''
        '''
        lstWidget = self.dictFields['fldWidget']
        try:
            lstExcept= self.dictFields['toTurnOff']
        except KeyError:
            lstExcept= self.dictFields['toCheck']
        bOK, lstError, lstReact, _ = self._toExecRules(wdgName=wdgName)
        self.lastChecked =(wdgName,wdgVal)
        if bOK:
            self.lastChecked = None
            self.AllWdgOffExceptOne(state=False, lstWdg=lstWidget, wdgObj=wdgObj, lstExcpt=lstExcept)
            self._msgRuleForWidgets(lstError=lstError, lstReact=lstReact,  wdgObj=wdgObj)
        else:
            self.AllWdgOffExceptOne(state=True, lstWdg=lstWidget, wdgObj=wdgObj, lstExcpt=lstExcept)
            self._msgRuleForWidgets(lstError=lstError, lstReact=lstReact,  wdgObj=wdgObj)
            self.sender().setFocus()
    
    
    def AllWdgOffExceptOne(self, state=True, lstWdg=None, wdgObj=None, lstExcpt=None):
        '''
        ''' 
        for idx, wdg in enumerate (lstWdg):
            if lstExcpt[idx]:
                setState= state
                if wdgObj is not None:
                    if wdgObj is wdg:
                        setState= False
                rscForm.setReadOnly(state=setState, widg=wdg)
    
            
    def _msgRuleForWidgets(self, lstError=None, lstReact=None,  wdgObj=None):
        '''
        Metodo para colocar a msg no Status Bar e muda a cor
        Se a lista de React Estiver vazia entao o lastChecked 
        passa para None.
        
        '''
        if lstReact == [] or (lstError is None or lstReact is None):
            QT_widgetsCustom.successFocus(obj=wdgObj)
            try:
                QT_widgetsCustom.successFocus(obj=self.LBwhois)
                self.LBwhois.setText('Tudo esta Ok!')
            except AttributeError:
                self.sender().setToolTip("Tudo esta Ok!")
        else:
            try:
                for idx, react in enumerate (lstReact):
                    if lstError != []:
                        if react:
                            QT_widgetsCustom.errorFocus(obj=wdgObj)
                            try:
                                QT_widgetsCustom.errorFocus(obj=self.LBwhois)
                                self.LBwhois.setText(str(lstError[idx]))
                            except AttributeError:
                                self.sender().setToolTip(str(lstError[idx]))
                        else:
                            QT_widgetsCustom.warningFocus(obj=wdgObj)
                            try:
                                QT_widgetsCustom.warningFocus(obj=self.LBwhois)
                                self.LBwhois.setText(str(lstError[idx]))
                            except AttributeError:
                                self.sender().setToolTip(str(lstError[idx]))
            except TypeError as ty:
                QT_msg.aviso(txt=str(ty))
            except IndexError as ie:
                QT_msg.aviso(txt=str(ie))
    
    
    def _msgRuleForForm(self, lstError=None, lstReact=None, lstObjNames=None):
        '''
        Metodo para Determinar o tipo de menssagem para validacao dos forms
        onde primerio limpa todos os highlights que os widgets tiverem
        depois faz a verificacao e mostra a menssagem e highlights os Campos afectados.
        Args:
            lstError= Lista de Erros 
            lstReact= Lista de Reacao
            lstObjNames= Lista de Nome dos Objectos 
        '''
        bOK =True
        if lstObjNames is not None:
            lstObjects = self.dictFields['fldWidget']
            lstOut = self.getObjByObjName(lstObjNames= lstObjNames, lstObjects=lstObjects)
            self.highlightsWidgets(lstWidgets=lstObjects)
            if (lstError is not None or lstReact is not None):
                try:
                    for idx, react in enumerate (lstReact):
                        if lstError != []: #Se nao houver erros Na lista de Erros entao Nao faz nada 
                            if react: #se houver verificamos o tipo de reacao, se For verdade o processo e bloqueiado.
                                QT_msg.aviso(txt="Aviso o processo nao sera execudado porque: "+str(lstError[idx]))
                                bOK =False
                                self.highlightsWidgets(bOK =bOK, lstWidgets=lstOut)
                            else: #se For Falso entao o tipo de reacao e opcional o usuario pode escolher continuar ou parar por ai.
                                bOK = QT_msg.is2insert(txt="Atencao tem a certeza que pretende introduzir os Dados Com "+str(lstError[idx]))
                                self.highlightsWidgets(bOK =bOK, lstWidgets=lstOut)
                except TypeError as ty:
                    QT_msg.aviso(txt=str(ty))
                except IndexError as ie:
                    QT_msg.aviso(txt=str(ie))
        return bOK     
    
    
    def getObjByObjName(self, lstObjNames=None, lstObjects=None):
        '''
        Get Obj Name
        '''
        lstOut = []
        for idx in range (len(lstObjNames)):
            for objNames in lstObjNames[idx]:
                for obj in lstObjects:
                    if obj is not None:
                        if obj.objectName() == objNames:
                            lstOut.append(obj)
        return lstOut
                    
                    
    def highlightsWidgets(self, bOK=None, lstWidgets=None):
        '''
        Highligth obj
        '''
        if bOK is None:
            for wdg in lstWidgets:
                QT_widgetsCustom.successFocus(obj=wdg)
        elif bOK is True:
            for wdg in lstWidgets:
                QT_widgetsCustom.warningFocus(obj=wdg)
        elif bOK is False:
            for wdg in lstWidgets:
                QT_widgetsCustom.errorFocus(obj=wdg)
                
        
        
    def formValid(self):
        '''
        metodo que valida o form e Coloca 
        mostra a mensagem de Erro
        '''
        _, lstError, lstReac, lstObjNames= self._toExecRules()
        bOK = self._msgRuleForForm(lstError=lstError, lstReact=lstReac, lstObjNames=lstObjNames)
        return bOK

    
    def _toExecRules(self, wdgName=None):
        '''
        Metodo que prepara os Dados para as regras serem executadas.
        Depois de Executadas verifica se houve alguma reacao.
        '''
        lstName = self.dictFields['objName']
        lstVal = self.getValues()
        try:
            if wdgName is None:
                rules = self.rules.get('ValidateForm')
            else:
                rules = self.rules['ValidateWidget'].get(wdgName)
            _, lstError, lstReac, lstObjNames= Rules.exec_Rule(lstNames=lstName, lstVal=lstVal, dictTrack=self.dictKeepTrack, dictRule=rules)
            bOK= self._afterExecRules(lstReact=lstReac)
        except (TypeError, AttributeError):
            bOK = True
            lstError, lstReac, lstObjNames= None, None, None
        return bOK, lstError, lstReac, lstObjNames
    
    
    def _afterExecRules(self, lstReact=None):
        '''
        Metodo para verificar se das regras verificadas, se houve 
        alguma reacao para bloqueiar os Form/Widgets.
        '''
        bOK = True
        if lstReact is not None:
            for val in lstReact:
                if val:
                    bOK= False
                    break
                else:
                    bOK= True
        return bOK
            
        
    def setDefault(self):
        '''
        ''' 
        wdgt = self.dictFields['fldWidget']
        toDefault = self.dictFields['toDefault']
        for idx, val in enumerate(wdgt):
            if toDefault[idx]:
                Rules.setNull(wdgt=val)
                
                
    def setValuesToEdit(self):
        '''
        ''' 
        if self.lstToEdit is not None:
            lstWidget= self.dictFields['fldWidget']
            for idx, val in enumerate(lstWidget):
                rscForm.setTxtToWidget(widget=val, val=self.lstToEdit[idx])

    
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
         
         
    def CBTextHint(self, Combox=None):
        mdel = QStandardItemModel(Combox.model())
        firstIndex = mdel.index(0, Combox.modelColumn(), Combox.rootModelIndex())
        firstItem = QStandardItem(mdel.itemFromIndex(firstIndex))
        firstItem.setSelectable(False)
        
    
    def getLocalizacao(self, nomeCentro=None):
        '''
        Metodo para Extrair a localizacao atraves do Nome Do local do local e 
        Retornado uma lista que vai ser usada para settar a localicao Artraves da provincia 
        ate o local de pesca.
        '''
        scrpt = ''' SELECT prov.nome, dist.nome, muni.nome, centro.nome 
                    FROM public.ref_geometric as centro 
                    inner join ref_geometric as muni on centro.id_parent = muni.id
                    inner join ref_geometric as dist on muni.id_parent = dist.id
                    inner join ref_geometric as prov on dist.id_parent = prov.id
                    where centro.id_tiplocal= 'CTP' and centro.nome = '{nomeCentro}' '''.format(nomeCentro= nomeCentro)
        bOK, lstOut = FuncSQL.anySelectScript(scpt=scrpt)
        return bOK, lstOut
        
        
    def setLocalizacao(self, nome=None):
        '''
        Metodo para Settar localizacao nos comboxs 
        da provincia ate o centro de pesca.
        '''
        bOK, lstIn = self.getLocalizacao(nomeCentro= nome)
        if bOK:
            lstWdiget = [self.CBProvincia, self.CBDistrito, self.CBPosto, self.CBCentroPesca]
            for idx, val in enumerate(lstWdiget):
                rscForm.setTxtToWidget(widget=val, val=lstIn[idx])


    def showMsg(self, obj=None, msgAlert=None):
        time = QTimer(self)
        obj.setText(msgAlert)
        QT_widgetsCustom.successDatabase(obj= obj)
        time.start(10000)
        time.setSingleShot(True)
        time.timeout.connect(self.toNormal)
   
   
    def toNormal(self):
        objName = self.LBwhois.objectName()
        css= "#"+str(objName)+"""{
                color:black;
                }"""
        self.LBwhois.setStyleSheet(css)
        self.LBwhois.setText("User Name")
    
                   
class CustomForm_Amostras(CustomFrm):
    def operacao(self):
        '''
        salvar
        '''
        bOK= self.formValid()
        if bOK:
            lstName= self.dictFields['fldName']
            lstQuot= self.dictFields['toQuote']
            lstVal=  self.getValues()
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
            