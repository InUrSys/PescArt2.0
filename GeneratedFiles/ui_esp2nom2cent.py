# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_esp2nom2cent.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(832, 642)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.TVesp2nom2cen = QtWidgets.QTableView(Form)
        self.TVesp2nom2cen.setEnabled(True)
        self.TVesp2nom2cen.setObjectName("TVesp2nom2cen")
        self.gridLayout.addWidget(self.TVesp2nom2cen, 5, 0, 1, 8)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.CBEspecies = QtWidgets.QComboBox(Form)
        self.CBEspecies.setObjectName("CBEspecies")
        self.gridLayout_2.addWidget(self.CBEspecies, 1, 1, 1, 1)
        self.CBNomeLocal = QtWidgets.QComboBox(Form)
        self.CBNomeLocal.setObjectName("CBNomeLocal")
        self.gridLayout_2.addWidget(self.CBNomeLocal, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.DEFim = QtWidgets.QDateEdit(Form)
        self.DEFim.setObjectName("DEFim")
        self.gridLayout_2.addWidget(self.DEFim, 2, 6, 1, 1)
        self.DEInicio = QtWidgets.QDateEdit(Form)
        self.DEInicio.setObjectName("DEInicio")
        self.gridLayout_2.addWidget(self.DEInicio, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 5, 1, 1)
        self.CBCentro = QtWidgets.QComboBox(Form)
        self.CBCentro.setObjectName("CBCentro")
        self.gridLayout_2.addWidget(self.CBCentro, 1, 6, 1, 1)
        self.LECodigo = QtWidgets.QLineEdit(Form)
        self.LECodigo.setObjectName("LECodigo")
        self.gridLayout_2.addWidget(self.LECodigo, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 3, 1, 1)
        self.CHBActivo = QtWidgets.QCheckBox(Form)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout_2.addWidget(self.CHBActivo, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 6, 1, 1)
        self.LEDescricao = QtWidgets.QLineEdit(Form)
        self.LEDescricao.setObjectName("LEDescricao")
        self.gridLayout_2.addWidget(self.LEDescricao, 3, 1, 1, 6)
        self.LEComentarios = QtWidgets.QLineEdit(Form)
        self.LEComentarios.setObjectName("LEComentarios")
        self.gridLayout_2.addWidget(self.LEComentarios, 4, 1, 1, 6)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PBEditar = QtWidgets.QPushButton(Form)
        self.PBEditar.setObjectName("PBEditar")
        self.horizontalLayout.addWidget(self.PBEditar)
        self.PBAdicionar = QtWidgets.QPushButton(Form)
        self.PBAdicionar.setObjectName("PBAdicionar")
        self.horizontalLayout.addWidget(self.PBAdicionar)
        self.PBGuardar = QtWidgets.QPushButton(Form)
        self.PBGuardar.setObjectName("PBGuardar")
        self.horizontalLayout.addWidget(self.PBGuardar)
        self.PBCancelar = QtWidgets.QPushButton(Form)
        self.PBCancelar.setObjectName("PBCancelar")
        self.horizontalLayout.addWidget(self.PBCancelar)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Comentarios"))
        self.label_2.setText(_translate("Form", "Inicio"))
        self.label_4.setText(_translate("Form", "Especie"))
        self.label_8.setText(_translate("Form", "Nome Local"))
        self.label_5.setText(_translate("Form", "Descricao"))
        self.label_7.setText(_translate("Form", "Centro"))
        self.label_3.setText(_translate("Form", "Fim"))
        self.label.setText(_translate("Form", "Codigo"))
        self.CHBActivo.setText(_translate("Form", "Activo"))
        self.PBEditar.setText(_translate("Form", "Editar"))
        self.PBAdicionar.setText(_translate("Form", "Adicionar"))
        self.PBGuardar.setText(_translate("Form", "Guradar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))

