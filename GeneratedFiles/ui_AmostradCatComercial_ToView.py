# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_AmostradCatComercial_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(233, 230)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionarAmostCat = QtWidgets.QPushButton(Dialog)
        self.PBAdicionarAmostCat.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionarAmostCat.setIcon(icon)
        self.PBAdicionarAmostCat.setObjectName("PBAdicionarAmostCat")
        self.gridLayout.addWidget(self.PBAdicionarAmostCat, 1, 0, 1, 1)
        self.PBEditarAmostCat = QtWidgets.QPushButton(Dialog)
        self.PBEditarAmostCat.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditarAmostCat.setIcon(icon1)
        self.PBEditarAmostCat.setObjectName("PBEditarAmostCat")
        self.gridLayout.addWidget(self.PBEditarAmostCat, 1, 1, 1, 1)
        self.TVAmostCategoria = QtWidgets.QTableView(Dialog)
        self.TVAmostCategoria.setObjectName("TVAmostCategoria")
        self.gridLayout.addWidget(self.TVAmostCategoria, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Amostra da Categoria"))

import icons_rc
