'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_ViagemPesca_ToView import Ui_Form
import mixedModel as mModel
import rscForm
from GenericToViewQDialog import GenericToView
from PyQt5.Qt import QLCDNumber
class toView_ViagemPesca(GenericToView, Ui_Form):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None):
        super(toView_ViagemPesca, self).__init__(parent)
        self.setupUi(self)
        
        self.cMapper = mModel.withWidgets()
        self.filtro ="id_activ_tip_unidade = {id}".format(id = str(Id))
        self.tblName = TblName
        self.setDict()
        self._setModelInView()
        self.PBAdicionarViagens.clicked.connect(self._insertClicked)
        self.PBEditarViagens.clicked.connect(self._EditarClicked)
        self.PBNext.clicked.connect(self.mapperNext)
        self.PBBack.clicked.connect(self.mapperPrev)
        self.betterViewData()
        
        
    def _setModelInView(self):
        lstVal2Rel= self.dictFields['fldRelName']
        lstRelTblName= self.dictFields['fldRelTblMain']
        lstNewNames= self.dictFields['HeaderNames']
        bOK, self.model = mModel.setViewModel(tblName=self.tblName, filtro=self.filtro, lstVal2Rel=lstVal2Rel, lstRelTblName=lstRelTblName, lstNewNames=lstNewNames)
        if bOK:
            self.config()
        self.betterViewData()
        
        
    def config(self):
        fldToMap = self.dictFields['fldToMap']
        self.cMapper.setMapper(model= self.model, fldToMap=fldToMap)
        val = self.cMapper.getValueFromMapper()
        _, row = val
        self.setLCD(val=row)
        try:
            self.updateItemClicked(newVal=val,idx=2)
        except AttributeError:
            try:
                self.parent().parent().updateItemClicked(newVal=val,idx=2)
            except AttributeError:
                try:
                    self.parent().updateItemClicked(newVal=val, idx=2)
                except:
                    pass
            
             

    def clearWidgets_Viagens(self):
        lstWdgt= self.dictFields['fldToMap']
        for val in lstWdgt:
            rscForm.setToDefault(val)
        self.betterViewData()
    
                
    def setNextView_Viagens(self, val=None):
        _, row = val
        self.parent().parent().updateItemClicked(newVal=val)
        self.parent().parent().updateModelOnNextView()
        self.setLCD(val=row)
        self.betterViewData()
        
        
    def setLCD(self, val=None):
        self.lcdNumber.display(str(val))
        
        
    def mapperNext(self):
        self.cMapper.mapperToNext()
        val = self.cMapper.getValueFromMapper()
        self.setNextView_Viagens(val=val)
        
    
    
    def mapperPrev(self):
        self.cMapper.mapperToPerv()
        val = self.cMapper.getValueFromMapper()
        self.setNextView_Viagens(val=val)
        
    
    
    def _insertClicked(self):
        bOK = self.parent().parent().openToInser()
        if bOK:
            bOK = self.model.select()
            if bOK:
                self.cMapper.mapperToNext()
                val = self.cMapper.getValueFromMapper()
                self.setNextView_Viagens(val=val)
        self.betterViewData()
            
    
    def _EditarClicked(self):
        lstVal= self.getValFromWidgets()
        bOK = self.parent().parent().openDlg(idx=1, ClickedlstVal=lstVal)
        if bOK:
            bOK = self.model.select()
            if bOK:
                self.cMapper.mapperToNext()
                val = self.cMapper.getValueFromMapper()
                self.setNextView_Viagens(val=val)
        self.betterViewData()
    
    
    def getValFromWidgets(self):
        lstWdg = self.dictFields['fldToMap']
        lstOut = rscForm.getTextAll(lstWidg=lstWdg)
        return lstOut
    
    def betterViewData(self):
        inicio = self.DEDataInicio.text()
        fim = self.DEDataFim.text()
        if inicio != '':
            new_inicio = inicio.split(sep='T' , maxsplit=4)
            self.DEDataInicio.setText(new_inicio[0])
        if fim != '':
            new_fim = fim.split(sep='T' , maxsplit=4)
            self.DEDataFim.setText(new_fim[0])
            
            
    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_activ_tip_unidade", "id_unipesca", "id_pesqueiros",
                                    "id_uniamostra", "id_tip_uni_pesca","n_sequnidade", "n_pescadores", "comp_rede",
                                    "comp_cabo", "tam_malha", "n_lances_amostrados", "n_lances_totais",
                                    "cap_total", "data_inicio", "data_fim", "hora_inicio",
                                    "hora_fim"],
                        
                        'fldToMap':[self.LEN_Sequencial, self.LEN_Sequencial_Arte, self.CBUniPesca, self.CBPesqueiros, self.CBUniAmostra,
                                    self.LETipUniPesca, self.SBNSeqUnidade, self.SBN_Pescadores, self.DSBComp_Rede, self.DSBComp_Cabo, self.DSBTam_Malha,
                                    self.SBN_Lanc_Amsotras, self.BN_Lanc_Total, self.DSBCapTotal, self.DEDataInicio, self.DEDataFim,
                                    self.TEHoraInico, self.TEHoraInico ],
                        
                        'HeaderNames':["ID", "ID DA ARTE", "UNI.PESCA", "PESQUEIROS",
                                    "UNI.AMOSTRA","TIPO DE UNIDADE DE PESCA","SEQ.UNIDADE", "Nº PESCADORES", "COMP.REDE"
                                    "COMP.CABO", "TAM.MALHA", "Nº LANCES AMOST.", "Nº LANCES TOTAL",
                                    "CAP.TOTAL", "INICIO", "FIM", "H.INICIO", "H.FIM"],
                                
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
                                  False]
                       
                      }