# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_AmostEspeEspecie_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(218, 228)
        Dialog.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionarAmostEspecificaEspecie = QtWidgets.QPushButton(Dialog)
        self.PBAdicionarAmostEspecificaEspecie.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionarAmostEspecificaEspecie.setIcon(icon)
        self.PBAdicionarAmostEspecificaEspecie.setObjectName("PBAdicionarAmostEspecificaEspecie")
        self.gridLayout.addWidget(self.PBAdicionarAmostEspecificaEspecie, 1, 0, 1, 1)
        self.PBEditarEspecieEspecifica = QtWidgets.QPushButton(Dialog)
        self.PBEditarEspecieEspecifica.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditarEspecieEspecifica.setIcon(icon1)
        self.PBEditarEspecieEspecifica.setObjectName("PBEditarEspecieEspecifica")
        self.gridLayout.addWidget(self.PBEditarEspecieEspecifica, 1, 1, 1, 1)
        self.TVAmostEspecificaEspecie = QtWidgets.QTableView(Dialog)
        self.TVAmostEspecificaEspecie.setObjectName("TVAmostEspecificaEspecie")
        self.gridLayout.addWidget(self.TVAmostEspecificaEspecie, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Amostra Especifica Da Especie"))

import icons_rc
import images_rc
