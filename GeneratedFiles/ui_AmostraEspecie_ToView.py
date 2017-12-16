# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_AmostraEspecie_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 228)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionarEspecies = QtWidgets.QPushButton(Dialog)
        self.PBAdicionarEspecies.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionarEspecies.setIcon(icon)
        self.PBAdicionarEspecies.setObjectName("PBAdicionarEspecies")
        self.gridLayout.addWidget(self.PBAdicionarEspecies, 1, 0, 1, 1)
        self.PBEditarEspecies = QtWidgets.QPushButton(Dialog)
        self.PBEditarEspecies.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditarEspecies.setIcon(icon1)
        self.PBEditarEspecies.setObjectName("PBEditarEspecies")
        self.gridLayout.addWidget(self.PBEditarEspecies, 1, 1, 1, 1)
        self.TVAmostEspecie = QtWidgets.QTableView(Dialog)
        self.TVAmostEspecie.setObjectName("TVAmostEspecie")
        self.gridLayout.addWidget(self.TVAmostEspecie, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Amostra Da Especie"))

import icons_rc
