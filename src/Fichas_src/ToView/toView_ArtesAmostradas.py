'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_Artes_Pesca_ToView import Ui_Form
from GenericToViewQDialog import GenericToView

class toView_ArtesAmostradas(GenericToView, Ui_Form):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None):
        super(toView_ArtesAmostradas, self).__init__(parent)
        self.setupUi(self)
        
        self.filtro=("id_saida = {id}".format(id=str(Id)))
        self.tblName = TblName
        self.con = dbcon
        
        self.setDict()
        self.setModelInView(tblView= self.TVArtePesca)
        self.TVArtePesca.clicked.connect(self.setNextView)
        self.PBAdicionarArtes.clicked.connect(self.insertClicked)
        self.PBEditarArtes.clicked.connect(self.updatedClicked)
        
        

    def setSameClicked(self):
        mIdx = self.parent().parent().mIdex
        self.setNextView(midx=mIdx)
        _, row= self.getClicked(mIdx=mIdx)
        self.TVArtePesca.selectRow(row)
    
    
    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_saida", "id_centro", "id_tip_uni_pesca", "n_activas", "n_nao_activas", "n_amostradas"],
                        'fldToHide':[True, True, False, False, False, False, False],
                        'HeaderNames':['ID', 'Saida Numero', 'Centro', "Tipo Uni. Pesca", 'Activas', 'Nao Activas', 'Amostradas'],
                        'fldRelTblMain':[None, None, "public.ref_geometric", "public.ref_unidpescatipo", None, None, None],
                        'fldRelName': [None, None, ["id", "nome"], ["id", "nome"], None, None, None],
                        'sizeCol': [0,0,110, 110, 50,50,50]
                        }