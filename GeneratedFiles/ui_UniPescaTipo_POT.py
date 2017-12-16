# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_UniPescaTipo_POT.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(377, 289)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.CBTipBarco = QtWidgets.QComboBox(Dialog)
        self.CBTipBarco.setObjectName("CBTipBarco")
        self.gridLayout.addWidget(self.CBTipBarco, 5, 3, 1, 2)
        self.LENome = QtWidgets.QLineEdit(Dialog)
        self.LENome.setMaxLength(50)
        self.LENome.setClearButtonEnabled(False)
        self.LENome.setObjectName("LENome")
        self.gridLayout.addWidget(self.LENome, 3, 3, 1, 2)
        self.LECodigo = QtWidgets.QLineEdit(Dialog)
        self.LECodigo.setMaxLength(10)
        self.LECodigo.setObjectName("LECodigo")
        self.gridLayout.addWidget(self.LECodigo, 1, 3, 1, 2)
        self.PTEDescricao = QtWidgets.QPlainTextEdit(Dialog)
        self.PTEDescricao.setObjectName("PTEDescricao")
        self.gridLayout.addWidget(self.PTEDescricao, 6, 3, 1, 2)
        self.CHBActivo = QtWidgets.QCheckBox(Dialog)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout.addWidget(self.CHBActivo, 7, 3, 1, 2)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 2)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.PBGuardar = QtWidgets.QPushButton(self.splitter)
        self.PBGuardar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBGuardar.setIcon(icon)
        self.PBGuardar.setObjectName("PBGuardar")
        self.PBCancelar = QtWidgets.QPushButton(self.splitter)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.splitter, 8, 1, 1, 4)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.CBArtes = QtWidgets.QComboBox(Dialog)
        self.CBArtes.setObjectName("CBArtes")
        self.gridLayout.addWidget(self.CBArtes, 4, 3, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tipo de barco"))
        self.label_8.setText(_translate("Dialog", "Nome:"))
        self.LENome.setPlaceholderText(_translate("Dialog", "Ex:Arasto"))
        self.LECodigo.setPlaceholderText(_translate("Dialog", "Ex:AAAAAAAAAA"))
        self.PTEDescricao.setPlaceholderText(_translate("Dialog", "Ex:O que se faz..."))
        self.CHBActivo.setText(_translate("Dialog", "Activo"))
        self.label_10.setText(_translate("Dialog", "Descricao:"))
        self.label.setText(_translate("Dialog", "Codigo:"))
        self.label_5.setText(_translate("Dialog", "Tipo de Barco:"))
        self.label_6.setText(_translate("Dialog", "Arte:"))

import icons_rc
