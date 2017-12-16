# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_LancesPesca_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(307, 201)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionarLances = QtWidgets.QPushButton(Dialog)
        self.PBAdicionarLances.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionarLances.setIcon(icon)
        self.PBAdicionarLances.setObjectName("PBAdicionarLances")
        self.gridLayout.addWidget(self.PBAdicionarLances, 1, 0, 1, 1)
        self.PBEditarLAnces = QtWidgets.QPushButton(Dialog)
        self.PBEditarLAnces.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditarLAnces.setIcon(icon1)
        self.PBEditarLAnces.setObjectName("PBEditarLAnces")
        self.gridLayout.addWidget(self.PBEditarLAnces, 1, 1, 1, 1)
        self.TVLances = QtWidgets.QTableView(Dialog)
        self.TVLances.setObjectName("TVLances")
        self.gridLayout.addWidget(self.TVLances, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lances de Pesca"))

import icons_rc
