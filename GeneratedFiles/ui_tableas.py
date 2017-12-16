# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_tableas.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(618, 662)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.LEComentarios = QtWidgets.QLineEdit(Form)
        self.LEComentarios.setObjectName("LEComentarios")
        self.gridLayout.addWidget(self.LEComentarios, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.PBEditar = QtWidgets.QPushButton(self.splitter)
        self.PBEditar.setObjectName("PBEditar")
        self.PBGuardar = QtWidgets.QPushButton(self.splitter)
        self.PBGuardar.setObjectName("PBGuardar")
        self.PBAdicionar = QtWidgets.QPushButton(self.splitter)
        self.PBAdicionar.setObjectName("PBAdicionar")
        self.PBCancelar = QtWidgets.QPushButton(self.splitter)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.splitter, 7, 0, 1, 2)
        self.CHBActivo = QtWidgets.QCheckBox(Form)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout.addWidget(self.CHBActivo, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.LENome = QtWidgets.QLineEdit(Form)
        self.LENome.setObjectName("LENome")
        self.gridLayout.addWidget(self.LENome, 2, 1, 1, 1)
        self.LECodigo = QtWidgets.QLineEdit(Form)
        self.LECodigo.setObjectName("LECodigo")
        self.gridLayout.addWidget(self.LECodigo, 1, 1, 1, 1)
        self.LEDescricao = QtWidgets.QLineEdit(Form)
        self.LEDescricao.setObjectName("LEDescricao")
        self.gridLayout.addWidget(self.LEDescricao, 3, 1, 1, 1)
        self.TVCodificadores = QtWidgets.QTableView(Form)
        self.TVCodificadores.setObjectName("TVCodificadores")
        self.gridLayout.addWidget(self.TVCodificadores, 6, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.CBGrupos = QtWidgets.QComboBox(Form)
        self.CBGrupos.setObjectName("CBGrupos")
        self.gridLayout.addWidget(self.CBGrupos, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tabelas de Refencias"))
        self.label_5.setText(_translate("Form", "Comentarios:"))
        self.PBEditar.setText(_translate("Form", "Editar"))
        self.PBGuardar.setText(_translate("Form", "Guardar"))
        self.PBAdicionar.setText(_translate("Form", "Adicionar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))
        self.CHBActivo.setText(_translate("Form", "Activo"))
        self.label.setText(_translate("Form", "Codigo:"))
        self.label_3.setText(_translate("Form", "Nome:"))
        self.label_4.setText(_translate("Form", "Descricao:"))
        self.label_2.setText(_translate("Form", "Grupo:"))

