'''
Created on 06/09/2017

@author: chernomirdinmacuvele
'''
from ui_ViagemPesca import Ui_frmViagemPesca
import GenericAmostrasQDialog
import FuncSQL

import rscForm
class dialog_ViagemPesca(GenericAmostrasQDialog.CustomForm_Amostras, Ui_frmViagemPesca):
    def __init__(self, parent=None, dbcon=None, TblName=None, Id=None, lstValToEdit=None, dictRules = None):
        super(dialog_ViagemPesca, self).__init__(parent)
        self.setupUi(self)
        
        self.N_Sequencial_Parent = str(Id)
        self.tblName = TblName
        self.lstToEdit = lstValToEdit
        self.dictRules = dictRules
        self.frmName = 'frmViagemPesca'
        self.setDict()
        self.bOK= (False, None)
        self.lastChecked = None
        self.configWidgetTriggeredEvent()
        self.configRules()
        self.configKeepTrack(id_parente=Id)
        self.configCombox()
        self._setValuesToEdit()       
        self.CHBInicio.stateChanged.connect(self.dataHandler)
        self.CHBFIm.stateChanged.connect(self.dataHandler)
        self.PBSalvar.clicked.connect(self._operacao)
        self.PBCancelar.clicked.connect(self.close)
        
        
    def dataHandler(self):
        if self.sender().objectName() == 'CHBInicio':
            if self.CHBInicio.isChecked():
                self.DEDataInicio.setEnabled(True)
            else:
                self.DEDataInicio.setEnabled(False)
        else:
            if self.CHBFIm.isChecked():
                self.DEDataFim.setEnabled(True)
            else:
                self.DEDataFim.setEnabled(False)
    
    def _setValuesToEdit(self):
        '''
        ''' 
        if self.lstToEdit is not None:
            lstWidget= self.dictFields['fldWidget']
            for idx, val in enumerate(lstWidget):
                rscForm.setTxtToWidget(widget=val, val=self.lstToEdit[idx])
            if self.lstToEdit[14] == 'NULL' or self.lstToEdit[14] == '':
                self.CHBInicio.setChecked(False)
                self.DEDataInicio.setEnabled(False)
            else:
                self.CHBInicio.setChecked(True)
                self.DEDataInicio.setEnabled(True)
                
            if self.lstToEdit[15] == 'NULL' or self.lstToEdit[15] == '':
                self.CHBFIm.setChecked(False)
                self.DEDataFim.setEnabled(False)
            else:
                self.CHBFIm.setChecked(True)
                self.DEDataFim.setEnabled(True)
            
            
        
    def _operacao(self):
        '''
        salvar
        '''
        bOK= self.formValid()
        if bOK:
            lstName= self.dictFields['fldName']
            lstQuot= self.dictFields['toQuote']
            lstVal=  self.getValues()
            if self.CHBInicio.isChecked() is False:
                lstVal[14] = 'NULL'
            if self.CHBFIm.isChecked() is False:
                lstVal[15] = 'NULL'
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
    
    def setDict(self):
        self.dictFields= {
                        'fldName': ["id", "id_activ_tip_unidade", "id_unipesca", "id_pesqueiro",
                                    "id_uniamostra","id_tip_uni_pesca","n_sequnidade",  "n_pescadores", "comp_rede",
                                    "comp_cabo", "tam_malha", "n_lances_amostrados", "n_lances_totais",
                                    "cap_total", "data_inicio", "data_fim", "hora_inicio",
                                    "hora_fim"],
                                    
                        'fldWidget': [self.LEN_Sequencial, self.LEN_Sequencial_Arte, self.LEUniPesca, self.CBPesqueiros, 
                                      self.CBUniAmostra, self.CBTipUniPesca, self.SBSeqUnidade, self.SBN_Pescadores, self.DSBComp_Rede, 
                                      self.DSBComp_Cabo, self.DSBTam_Malha, self.SBN_Lanc_Amsotras, self.SBN_Lanc_Total, 
                                      self.DSBCapTotal, self.DEDataInicio, self.DEDataFim, self.TEHoraInico, 
                                      self.TEHoraFim ],
                        
                        'isRel': [False, False, False, True, 
                                   True, True,False, False, False, 
                                   False,  False,  False, False, 
                                   False, False, False, False,
                                   False],
                                    
                        'objName':["id", "id_activ_tip_unidade", "LEUniPesca", "CBPesqueiros",
                                    "CBUniAmostra", "CBTipUniPesca", "SBSeqUnidade",  "SBN_Pescadores", "DSBComp_Rede",
                                    "DSBComp_Cabo", "DSBTam_Malha", "SBN_Lanc_Amsotras", "SBN_Lanc_Total",
                                    "DSBCapTotal", "DEDataInicio", "DEDataFim", "TEHoraInico",
                                    "TEHoraFim"],
                        
                        'toDefault':[False, False, True, False, 
                                   False, False, False, False, False, 
                                   False,  False,  False, False, 
                                   False, False, False, False,
                                   False],
                        
                        'toCheck': [False, False, True, True, 
                                   True, True, True, True, True, 
                                   True,  True,  True, True, 
                                   True, True, True, True,
                                   True],
                          
                        "toQuote":[False, False, True, False, 
                                    True, True, False, False, True,
                                    True, True, False,False, 
                                    True, True, True, True,
                                    True]
                                    }

        self.dictCB= {
                        'quer':["select null as id , '-Pesqueiros-' as nome union all select id, nome from ref_pesqueiro",
                                "select null as id , '-Unidade de Amostra-' as nome union all select id, nome from ref_table where id_grupo='UAM'",
                                "select null as id, '-Tipo de unidade de Pesca-' as nome union all select  id, nome from ref_unidpescatipo;"],
                        
                        'widget':[self.CBPesqueiros, self.CBUniAmostra, self.CBTipUniPesca]
                      }
        