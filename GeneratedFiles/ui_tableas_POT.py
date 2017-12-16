# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_tableas_POT.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(394, 441)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.LECodigo = QtWidgets.QLineEdit(Form)
        self.LECodigo.setMaxLength(6)
        self.LECodigo.setObjectName("LECodigo")
        self.gridLayout.addWidget(self.LECodigo, 1, 2, 1, 1)
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
        self.gridLayout.addWidget(self.splitter, 6, 0, 1, 4)
        self.LBid = QtWidgets.QLabel(Form)
        self.LBid.setObjectName("LBid")
        self.gridLayout.addWidget(self.LBid, 1, 1, 1, 1)
        self.CBGrupos = QtWidgets.QComboBox(Form)
        self.CBGrupos.setEnabled(False)
        self.CBGrupos.setObjectName("CBGrupos")
        self.gridLayout.addWidget(self.CBGrupos, 0, 1, 1, 3)
        self.LENome = QtWidgets.QLineEdit(Form)
        self.LENome.setMaxLength(50)
        self.LENome.setObjectName("LENome")
        self.gridLayout.addWidget(self.LENome, 2, 1, 1, 3)
        self.PTEDescricao = QtWidgets.QPlainTextEdit(Form)
        self.PTEDescricao.setObjectName("PTEDescricao")
        self.gridLayout.addWidget(self.PTEDescricao, 3, 1, 1, 3)
        self.PTEComentarios = QtWidgets.QPlainTextEdit(Form)
        self.PTEComentarios.setObjectName("PTEComentarios")
        self.gridLayout.addWidget(self.PTEComentarios, 4, 1, 1, 3)
        self.CHBActivo = QtWidgets.QCheckBox(Form)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout.addWidget(self.CHBActivo, 5, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tabelas de Refencias"))
        self.label_2.setText(_translate("Form", "Grupo:"))
        self.label_5.setText(_translate("Form", "Comentarios:"))
        self.label.setText(_translate("Form", "Codigo:"))
        self.label_3.setText(_translate("Form", "Nome:"))
        self.label_4.setText(_translate("Form", "Descricao:"))
        self.LECodigo.setPlaceholderText(_translate("Form", "Ex:AAA"))
        self.LBid.setText(_translate("Form", "999"))
        self.LENome.setPlaceholderText(_translate("Form", "Ex:Habitat"))
        self.PTEDescricao.setPlaceholderText(_translate("Form", "Ex:O que faz…"))
        self.PTEComentarios.setPlaceholderText(_translate("Form", "Ex:Nota, Obs…"))
        self.CHBActivo.setText(_translate("Form", "Activo"))

import icons_rc
