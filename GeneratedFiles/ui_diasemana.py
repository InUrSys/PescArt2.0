# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_diasemana.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(618, 662)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777210))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.LEComentarios = QtWidgets.QLineEdit(Form)
        self.LEComentarios.setObjectName("LEComentarios")
        self.gridLayout.addWidget(self.LEComentarios, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.LENome = QtWidgets.QLineEdit(Form)
        self.LENome.setObjectName("LENome")
        self.gridLayout.addWidget(self.LENome, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.CBTipDia = QtWidgets.QComboBox(Form)
        self.CBTipDia.setObjectName("CBTipDia")
        self.gridLayout.addWidget(self.CBTipDia, 1, 2, 1, 1)
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
        self.gridLayout.addWidget(self.splitter, 8, 0, 1, 3)
        self.CHBActivo = QtWidgets.QCheckBox(Form)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout.addWidget(self.CHBActivo, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.LEDescricao = QtWidgets.QLineEdit(Form)
        self.LEDescricao.setObjectName("LEDescricao")
        self.gridLayout.addWidget(self.LEDescricao, 4, 2, 1, 1)
        self.TVDiaSemana = QtWidgets.QTableView(Form)
        self.TVDiaSemana.setObjectName("TVDiaSemana")
        self.gridLayout.addWidget(self.TVDiaSemana, 7, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.LECodigo = QtWidgets.QLineEdit(Form)
        self.LECodigo.setObjectName("LECodigo")
        self.gridLayout.addWidget(self.LECodigo, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dias de Semana"))
        self.label_5.setText(_translate("Form", "Comentarios:"))
        self.label_4.setText(_translate("Form", "Descricao:"))
        self.PBEditar.setText(_translate("Form", "Editar"))
        self.PBGuardar.setText(_translate("Form", "Guardar"))
        self.PBAdicionar.setText(_translate("Form", "Adicionar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))
        self.CHBActivo.setText(_translate("Form", "Activo"))
        self.label.setText(_translate("Form", "Codigo:"))
        self.label_2.setText(_translate("Form", "Tipo de Dia:"))
        self.label_3.setText(_translate("Form", "Nome:"))

