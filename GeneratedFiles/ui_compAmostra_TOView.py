# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_compAmostra_TOView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(141, 231)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionarComprimentos = QtWidgets.QPushButton(Dialog)
        self.PBAdicionarComprimentos.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionarComprimentos.setIcon(icon)
        self.PBAdicionarComprimentos.setObjectName("PBAdicionarComprimentos")
        self.gridLayout.addWidget(self.PBAdicionarComprimentos, 1, 0, 1, 1)
        self.PBEditarComprimentos = QtWidgets.QPushButton(Dialog)
        self.PBEditarComprimentos.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditarComprimentos.setIcon(icon1)
        self.PBEditarComprimentos.setObjectName("PBEditarComprimentos")
        self.gridLayout.addWidget(self.PBEditarComprimentos, 1, 1, 1, 1)
        self.TVComprimentos = QtWidgets.QTableView(Dialog)
        self.TVComprimentos.setObjectName("TVComprimentos")
        self.gridLayout.addWidget(self.TVComprimentos, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Composicao"))

import icons_rc
