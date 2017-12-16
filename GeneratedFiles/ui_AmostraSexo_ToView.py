# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_AmostraSexo_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(247, 231)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionarSexo = QtWidgets.QPushButton(Dialog)
        self.PBAdicionarSexo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionarSexo.setIcon(icon)
        self.PBAdicionarSexo.setObjectName("PBAdicionarSexo")
        self.gridLayout.addWidget(self.PBAdicionarSexo, 1, 0, 1, 1)
        self.PBEditarSexo = QtWidgets.QPushButton(Dialog)
        self.PBEditarSexo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditarSexo.setIcon(icon1)
        self.PBEditarSexo.setObjectName("PBEditarSexo")
        self.gridLayout.addWidget(self.PBEditarSexo, 1, 1, 1, 1)
        self.TVAmostSexo = QtWidgets.QTableView(Dialog)
        self.TVAmostSexo.setObjectName("TVAmostSexo")
        self.gridLayout.addWidget(self.TVAmostSexo, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Amostra do Sexo"))

import icons_rc
