'''
Created on 08/02/2018

@author: chernomirdinmacuvele
'''
from ui_TreeViewMoz import Ui_Form
from PyQt5.Qt import QDialog, QTreeView
import FuncSQL
import GenericTreeView as TreeView

class frmEstroturaHierarquia(Ui_Form, QDialog):
    def __init__(self, parent=None, dbcon=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.setTreeView()
        
        self.PBFechar.clicked.connect(self.close)
        
    def setTreeView(self):
        
        quer=   """
                SELECT tbl2.nome as "Pais", tbl3.nome as "Provincia" , tbl4.nome as "Distritos", tbl5.nome as "Posto Admin",tbl6.nome as "Centro de Pesca"
                FROM public.ref_geometric as tbl1
                inner join ref_geometric as tbl2 
                on tbl1.id = tbl2.id and tbl2.id_tiplocal = 'PIS'
                inner join ref_geometric as tbl3
                on tbl2.id = tbl3.id_parent and tbl3.id_tiplocal = 'PRV'
                inner join ref_geometric as tbl4
                on tbl3.id = tbl4.id_parent and tbl4.id_tiplocal = 'DST'
                inner join ref_geometric as tbl5
                on tbl4.id = tbl5.id_parent and tbl5.id_tiplocal = 'PSD'
                inner join ref_geometric as tbl6
                on tbl5.id = tbl6.id_parent and tbl6.id_tiplocal = 'CTP'
                order by tbl2.id asc, tbl3.nome desc    
                """
        bOK,mTrix = FuncSQL.multLineSelect(scpt=quer)
        
        if bOK:
            lstProv = []
            lstDist = []
            lstPost = []
            lstCentro = []
            Nomepais = mTrix[0][0]
             
            for nome in mTrix:
                if (nome[0],nome[1]) not in lstProv:
                    lstProv.append((nome[0], nome[1]))
                if (nome[1],nome[2]) not in lstDist:
                    lstDist.append((nome[1],nome[2]))
                if (nome[2],nome[3]) not in lstPost:
                    lstPost.append((nome[2],nome[3]))
                if (nome[3],nome[4]) not in lstCentro:
                    lstCentro.append((nome[3],nome[4]))
                    
            pais_Node = TreeView.Pais_Nodo(Nomepais)
            for key, value in lstProv:
                provincia_Node = TreeView.Provincia_Nodo(value, pais_Node)
                
                for key_1, value_1 in lstDist:
                    if key_1 == value:
                        distrito_Node = TreeView.Distrito_Nodo(value_1, provincia_Node)
                        
                        for key_2, value_2 in lstPost:
                            if key_2 == value_1:
                                posto_Node = TreeView.Posto_Nodo(value_2, distrito_Node)
                                
                                for key_3, value_3 in lstCentro:
                                    if key_3 == value_2:
                                        centro_Node = TreeView.Centro_Nodo(value_3, posto_Node)
            
         
        model = TreeView.TreeModel(pais_Node)
        self.TViewMoz.setModel(model)
        print('Here')