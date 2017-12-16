# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_pesqueiros_POT.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(307, 251)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.CHBActivo = QtWidgets.QCheckBox(Form)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout.addWidget(self.CHBActivo, 4, 0, 1, 4)
        self.PBGuardar = QtWidgets.QPushButton(Form)
        self.PBGuardar.setObjectName("PBGuardar")
        self.gridLayout.addWidget(self.PBGuardar, 5, 0, 2, 2)
        self.LENome = QtWidgets.QLineEdit(Form)
        self.LENome.setObjectName("LENome")
        self.gridLayout.addWidget(self.LENome, 2, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.PTEComentarios = QtWidgets.QPlainTextEdit(Form)
        self.PTEComentarios.setObjectName("PTEComentarios")
        self.gridLayout.addWidget(self.PTEComentarios, 3, 1, 1, 3)
        self.PBCancelar = QtWidgets.QPushButton(Form)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 5, 2, 2, 2)
        self.LECodigo = QtWidgets.QLineEdit(Form)
        self.LECodigo.setReadOnly(True)
        self.LECodigo.setObjectName("LECodigo")
        self.gridLayout.addWidget(self.LECodigo, 0, 1, 1, 3)
        self.CBProvincia = QtWidgets.QComboBox(Form)
        self.CBProvincia.setObjectName("CBProvincia")
        self.gridLayout.addWidget(self.CBProvincia, 1, 1, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pesqueiros"))
        self.label.setText(_translate("Form", "Id:"))
        self.label_2.setText(_translate("Form", "Provincia:"))
        self.label_3.setText(_translate("Form", "Nome:"))
        self.CHBActivo.setText(_translate("Form", "Activo"))
        self.PBGuardar.setText(_translate("Form", "Guardar"))
        self.label_4.setText(_translate("Form", "Comentario:"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))

