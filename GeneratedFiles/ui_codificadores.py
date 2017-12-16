# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_codificadores.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(848, 452)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.TVCodificadores = QtWidgets.QTableView(Form)
        self.TVCodificadores.setObjectName("TVCodificadores")
        self.gridLayout.addWidget(self.TVCodificadores, 0, 0, 1, 2)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.PBEditar = QtWidgets.QPushButton(self.splitter)
        self.PBEditar.setObjectName("PBEditar")
        self.PBAdicionar = QtWidgets.QPushButton(self.splitter)
        self.PBAdicionar.setObjectName("PBAdicionar")
        self.PBCancelar = QtWidgets.QPushButton(self.splitter)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Codificador"))
        self.PBEditar.setText(_translate("Form", "Editar"))
        self.PBAdicionar.setText(_translate("Form", "Adicionar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))

