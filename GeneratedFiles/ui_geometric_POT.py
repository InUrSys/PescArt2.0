# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_geometric_POT.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(355, 581)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777210))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.PTEDescricao = QtWidgets.QPlainTextEdit(Form)
        self.PTEDescricao.setObjectName("PTEDescricao")
        self.gridLayout.addWidget(self.PTEDescricao, 11, 1, 1, 3)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.CBTipLocal = QtWidgets.QComboBox(Form)
        self.CBTipLocal.setObjectName("CBTipLocal")
        self.gridLayout.addWidget(self.CBTipLocal, 3, 1, 1, 3)
        self.CBPostoAdmin = QtWidgets.QComboBox(Form)
        self.CBPostoAdmin.setObjectName("CBPostoAdmin")
        self.gridLayout.addWidget(self.CBPostoAdmin, 8, 1, 1, 3)
        self.CBDistrito = QtWidgets.QComboBox(Form)
        self.CBDistrito.setObjectName("CBDistrito")
        self.gridLayout.addWidget(self.CBDistrito, 6, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.CBPais = QtWidgets.QComboBox(Form)
        self.CBPais.setObjectName("CBPais")
        self.gridLayout.addWidget(self.CBPais, 4, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.CBProvincia = QtWidgets.QComboBox(Form)
        self.CBProvincia.setObjectName("CBProvincia")
        self.gridLayout.addWidget(self.CBProvincia, 5, 1, 1, 3)
        self.PTEComentarios = QtWidgets.QPlainTextEdit(Form)
        self.PTEComentarios.setObjectName("PTEComentarios")
        self.gridLayout.addWidget(self.PTEComentarios, 12, 1, 1, 3)
        self.splitter = QtWidgets.QSplitter(Form)
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
        self.gridLayout.addWidget(self.splitter, 14, 0, 1, 4)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.CHBActivo = QtWidgets.QCheckBox(Form)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout.addWidget(self.CHBActivo, 13, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 12, 0, 1, 1)
        self.LECodigo = QtWidgets.QLineEdit(Form)
        self.LECodigo.setMaxLength(9)
        self.LECodigo.setObjectName("LECodigo")
        self.gridLayout.addWidget(self.LECodigo, 0, 2, 1, 1)
        self.LENome = QtWidgets.QLineEdit(Form)
        self.LENome.setMaxLength(50)
        self.LENome.setObjectName("LENome")
        self.gridLayout.addWidget(self.LENome, 10, 1, 1, 3)
        self.LBid = QtWidgets.QLabel(Form)
        self.LBid.setObjectName("LBid")
        self.gridLayout.addWidget(self.LBid, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.CBCentroPesca = QtWidgets.QComboBox(Form)
        self.CBCentroPesca.setObjectName("CBCentroPesca")
        self.gridLayout.addWidget(self.CBCentroPesca, 9, 1, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Geometric"))
        self.label_9.setText(_translate("Form", "Provincia:"))
        self.label_4.setText(_translate("Form", "Descricao:"))
        self.label.setText(_translate("Form", "Codigo:"))
        self.PTEDescricao.setPlaceholderText(_translate("Form", "Ex:O que faz…"))
        self.label_7.setText(_translate("Form", "Posto. Admin:"))
        self.label_2.setText(_translate("Form", "Tipo Local:"))
        self.PTEComentarios.setPlaceholderText(_translate("Form", "Ex:Nota, Obs…"))
        self.label_10.setText(_translate("Form", "Pais:"))
        self.CHBActivo.setText(_translate("Form", "Activo"))
        self.label_8.setText(_translate("Form", "Distrito:"))
        self.label_3.setText(_translate("Form", "Nome:"))
        self.label_5.setText(_translate("Form", "Comentarios:"))
        self.LECodigo.setPlaceholderText(_translate("Form", "Ex:AAAAAA"))
        self.LENome.setPlaceholderText(_translate("Form", "Ex:Nome do Tipo de Localizacao"))
        self.LBid.setText(_translate("Form", "AAA"))
        self.label_11.setText(_translate("Form", "Centro. Pesca:"))

import icons_rc
