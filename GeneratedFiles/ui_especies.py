# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_especies.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(919, 643)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.DSBMinimo = QtWidgets.QDoubleSpinBox(Form)
        self.DSBMinimo.setObjectName("DSBMinimo")
        self.gridLayout.addWidget(self.DSBMinimo, 3, 2, 1, 1)
        self.LEEspecies = QtWidgets.QLineEdit(Form)
        self.LEEspecies.setObjectName("LEEspecies")
        self.gridLayout.addWidget(self.LEEspecies, 1, 1, 1, 2)
        self.DSBComum = QtWidgets.QDoubleSpinBox(Form)
        self.DSBComum.setObjectName("DSBComum")
        self.gridLayout.addWidget(self.DSBComum, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.LECodigo = QtWidgets.QLineEdit(Form)
        self.LECodigo.setObjectName("LECodigo")
        self.gridLayout.addWidget(self.LECodigo, 0, 1, 1, 2)
        self.CBHabitat = QtWidgets.QComboBox(Form)
        self.CBHabitat.setObjectName("CBHabitat")
        self.gridLayout.addWidget(self.CBHabitat, 2, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.CHBAnalize = QtWidgets.QCheckBox(Form)
        self.CHBAnalize.setObjectName("CHBAnalize")
        self.gridLayout.addWidget(self.CHBAnalize, 5, 1, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.DSBMaximo_2 = QtWidgets.QDoubleSpinBox(Form)
        self.DSBMaximo_2.setObjectName("DSBMaximo_2")
        self.gridLayout_2.addWidget(self.DSBMaximo_2, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.LEGenus = QtWidgets.QLineEdit(Form)
        self.LEGenus.setObjectName("LEGenus")
        self.gridLayout_2.addWidget(self.LEGenus, 1, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 3)
        self.DSBMaixmo = QtWidgets.QDoubleSpinBox(Form)
        self.DSBMaixmo.setObjectName("DSBMaixmo")
        self.gridLayout_2.addWidget(self.DSBMaixmo, 3, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 1, 1, 1)
        self.LEFamila = QtWidgets.QLineEdit(Form)
        self.LEFamila.setObjectName("LEFamila")
        self.gridLayout_2.addWidget(self.LEFamila, 0, 1, 1, 2)
        self.CHBActivo = QtWidgets.QCheckBox(Form)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout_2.addWidget(self.CHBActivo, 5, 1, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.LEComentarios = QtWidgets.QLineEdit(Form)
        self.LEComentarios.setObjectName("LEComentarios")
        self.gridLayout_3.addWidget(self.LEComentarios, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 2)
        self.TVEspecies = QtWidgets.QTableView(Form)
        self.TVEspecies.setObjectName("TVEspecies")
        self.gridLayout_4.addWidget(self.TVEspecies, 3, 0, 1, 2)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.PBCancelar = QtWidgets.QPushButton(self.splitter)
        self.PBCancelar.setObjectName("PBCancelar")
        self.PBEditar = QtWidgets.QPushButton(self.splitter)
        self.PBEditar.setObjectName("PBEditar")
        self.PBAdicionar = QtWidgets.QPushButton(self.splitter)
        self.PBAdicionar.setObjectName("PBAdicionar")
        self.PBGuardar = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBGuardar.sizePolicy().hasHeightForWidth())
        self.PBGuardar.setSizePolicy(sizePolicy)
        self.PBGuardar.setObjectName("PBGuardar")
        self.gridLayout_4.addWidget(self.splitter, 4, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Especies"))
        self.label_2.setText(_translate("Form", "codigo:"))
        self.label_11.setText(_translate("Form", "Intervalo de classes "))
        self.label_5.setText(_translate("Form", "Especies:"))
        self.label_9.setText(_translate("Form", "Minimo:"))
        self.label_13.setText(_translate("Form", "Comum:"))
        self.label_8.setText(_translate("Form", "Comprimentos"))
        self.label_6.setText(_translate("Form", "Habitat:"))
        self.CHBAnalize.setText(_translate("Form", "Analizar Composicao Especifica"))
        self.label.setText(_translate("Form", "Familia:"))
        self.label_3.setText(_translate("Form", "Genus:"))
        self.label_10.setText(_translate("Form", "maximo:"))
        self.label_12.setText(_translate("Form", "maximo:"))
        self.CHBActivo.setText(_translate("Form", "Activo"))
        self.label_4.setText(_translate("Form", "Comentarios:"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))
        self.PBEditar.setText(_translate("Form", "Editar"))
        self.PBAdicionar.setText(_translate("Form", "Adicionar"))
        self.PBGuardar.setText(_translate("Form", "Guardar"))
