'''
Created on 15/08/2017

@author: chernomirdinmacuvele
'''
from ui_especies_POT import Ui_Form
from GenericReferenciasQDialog import GenericReferencias
from PyQt5.Qt import QLineEdit

class dlg_especies(GenericReferencias,Ui_Form):
    def __init__(self, parent = None, dbcon=None, tblName=None, indexModel=None, idx=None, level=None):
        super(dlg_especies, self).__init__(parent=None)
        self.setupUi(self)
        
        self.tblName = tblName
        self.mIdx = indexModel
        self.setDict()
        self.configCombox()
        self.toEdit()
        self.bOK = (False, None)
        
        self.level = level
        self.justView()
        
        self.PBGuardar.clicked.connect(self.generateNome)
        self.PBCancelar.clicked.connect(self.close)
        
    def generateNome(self):
        '''
        select id, concat_ws(' ',genus, species) as EspNameUse
        from ref_especies
        where (species is not null) and (species not like 'sp.')
        union all
        select id, (genus || ' sp.') as EspNameUse
        from ref_especies
        where (genus is not null and ((species is null) or (species like 'sp.')))
        union all
        select id, (familia) as EspNameUse
        from ref_especies
        where (genus is null)
        '''
        if self.LENome.text() == '':
            if (self.LEGenus.text() != '' or self.LEGenus.text() != 'n/a') and self.LEEspecies.text() != '':
                nome = self.LEGenus.text()+' '+self.LEEspecies.text()
            elif self.LEGenus.text() != '' and (self.LEEspecies.text() == 'sp.' or self.LEEspecies.text() == '' or self.LEEspecies.text() == 'n/a'):
                nome = self.LEGenus.text()+' '+'sp.'
            else:
                nome = self.LEFamila.text()
            self.LENome.setText(str(nome))
        self.pre_operacao()
            
    
    def setDict(self):
        self.dictFields={
                        'lstName': ["id", "familia", "genus", "species", "id_habitat", "minlength", "maxlength", "intlength", "intmaxlen", "ana_comesp", "comentario", "activo","nome"],
                        'lstToQuote': [True, True, True, True, True, False, False, False, False, False, True, False, True],
                        'lstWidget': [self.LECodigo, self.LEFamila, self.LEGenus, self.LEEspecies, self.CBHabitat, self.DSBMinimo, self.DSBMaixmo,
                                      self.DSBComum, self.DSBMaximo_2, self.CHBAnalize, self.PTEComentarios, self.CHBActivo, self.LENome],
                        'lstRel': [False, False, False, False, True, False, False, False, False, False, False, False, False],
                        'lstDefault':[False, True, True, False, True, True, True, True, True, True ,True ,True, True],
                        'lstUpercase':[True, False, False, False, False, False, False, False, False,False,False ,False,False]
                        }
        
        self.dictCB= {
                    'quer':["select null as id, '-Habitate-' as nome union all select id, nome from ref_table where id_grupo = 'HBT';"],
                                            
                    'widget':[self.CBHabitat]
                           }