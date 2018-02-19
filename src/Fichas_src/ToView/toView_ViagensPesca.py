'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_ViagemPesca_ToView import Ui_Form
import mixedModel as mModel
from GenericToViewQDialog import GenericToView
class toView_ViagemPesca(GenericToView, Ui_Form):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None):
        super(toView_ViagemPesca, self).__init__(parent)
        self.setupUi(self)
        
        self.cMapper = mModel.withWidgets()
        self.filtro ="id_activ_tip_unidade = {id}".format(id = str(Id))
        self.tblName = TblName
        self.setDict()
        
        self.setModelInView(tblView= self.TVViagens)
        self.TVViagens.clicked.connect(self.setNextView)
        self.PBAdicionar.clicked.connect(self.insertClicked)
        self.PBEditar.clicked.connect(self.updatedClicked)
    
    def setModelFromKeepTrack(self):
        self.setModelInView(tblView= self.TVViagens)
            
    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_activ_tip_unidade", "id_unipesca", "id_pesqueiros",
                                    "id_uniamostra", "id_tip_uni_pesca","n_sequnidade", "n_pescadores", "comp_rede",
                                    "comp_cabo", "tam_malha", "n_lances_amostrados", "n_lances_totais",
                                    "cap_total", "data_inicio", "data_fim", "hora_inicio",
                                    "hora_fim"],

                        'HeaderNames':["ID", "ID DA ARTE", "UNI.PESCA", "PESQUEIROS",
                                    "UNI.AMOSTRA","TIPO DE UNIDADE DE PESCA","SEQ", "Nº PESCADORES", "COMP.REDE"
                                    "COMP.CABO", "TAM.MALHA", "Nº LANCES AMOST.", "Nº LANCES TOTAL",
                                    "CAP.TOTAL", "Data do Inicio", "Data do Fim", "Hora do Inicio", "Hara do fim"],
                                
                        'fldRelTblMain': [None, None, None, "public.ref_pesqueiro",
                                          "public.ref_table", "ref_unidpescatipo",  None, None, None,
                                          None, None, None, None,
                                           None, None, None, None, None],
                       
                        'fldRelName': [None, None, None , ["id", "nome"],
                                        ["id", "nome"], ["id", "nome"],  None, None, None,
                                        None, None, None, None,
                                        None, None, None, None, None],
                          
                        'fldToHide':[True, True, False, False,
                                  False,False, False,False, False,
                                  False, False, False, False,
                                  False, False, False, False,
                                  False],
                          
                        'sizeCol':[0,0, 170, 170, 170, 170, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
                       
                      }