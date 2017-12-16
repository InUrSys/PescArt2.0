# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_Saidas_Obs.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmFactores(object):
    def setupUi(self, frmFactores):
        frmFactores.setObjectName("frmFactores")
        frmFactores.resize(800, 117)
        self.gridLayout_2 = QtWidgets.QGridLayout(frmFactores)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(frmFactores)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(frmFactores)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.CBFactores = QtWidgets.QComboBox(frmFactores)
        self.CBFactores.setObjectName("CBFactores")
        self.gridLayout_2.addWidget(self.CBFactores, 0, 1, 1, 1)
        self.LEComentarios = QtWidgets.QLineEdit(frmFactores)
        self.LEComentarios.setObjectName("LEComentarios")
        self.gridLayout_2.addWidget(self.LEComentarios, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBSalvar = QtWidgets.QPushButton(frmFactores)
        self.PBSalvar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(frmFactores)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.retranslateUi(frmFactores)
        QtCore.QMetaObject.connectSlotsByName(frmFactores)

    def retranslateUi(self, frmFactores):
        _translate = QtCore.QCoreApplication.translate
        frmFactores.setWindowTitle(_translate("frmFactores", "Factores Externos"))
        self.label_7.setText(_translate("frmFactores", "Factores"))
        self.label_8.setText(_translate("frmFactores", "Comentarios"))
        self.LEComentarios.setPlaceholderText(_translate("frmFactores", "Ex:Nota, Obs…"))

import icons_rc
