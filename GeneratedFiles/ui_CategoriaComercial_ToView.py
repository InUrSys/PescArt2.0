# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_CategoriaComercial_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(365, 197)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionarCatComerical = QtWidgets.QPushButton(Dialog)
        self.PBAdicionarCatComerical.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionarCatComerical.setIcon(icon)
        self.PBAdicionarCatComerical.setObjectName("PBAdicionarCatComerical")
        self.gridLayout.addWidget(self.PBAdicionarCatComerical, 1, 0, 1, 1)
        self.PBEditarCatComercial = QtWidgets.QPushButton(Dialog)
        self.PBEditarCatComercial.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditarCatComercial.setIcon(icon1)
        self.PBEditarCatComercial.setObjectName("PBEditarCatComercial")
        self.gridLayout.addWidget(self.PBEditarCatComercial, 1, 1, 1, 1)
        self.TVCatComercial = QtWidgets.QTableView(Dialog)
        self.TVCatComercial.setObjectName("TVCatComercial")
        self.gridLayout.addWidget(self.TVCatComercial, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Categoria Comercial"))

import icons_rc
