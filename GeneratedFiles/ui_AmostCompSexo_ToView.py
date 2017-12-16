# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_AmostCompSexo_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 241)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionarCompSexo = QtWidgets.QPushButton(Dialog)
        self.PBAdicionarCompSexo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionarCompSexo.setIcon(icon)
        self.PBAdicionarCompSexo.setObjectName("PBAdicionarCompSexo")
        self.gridLayout.addWidget(self.PBAdicionarCompSexo, 1, 0, 1, 1)
        self.PBEditarCompSexo = QtWidgets.QPushButton(Dialog)
        self.PBEditarCompSexo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditarCompSexo.setIcon(icon1)
        self.PBEditarCompSexo.setObjectName("PBEditarCompSexo")
        self.gridLayout.addWidget(self.PBEditarCompSexo, 1, 1, 1, 1)
        self.TVAmostCompSexo = QtWidgets.QTableView(Dialog)
        self.TVAmostCompSexo.setObjectName("TVAmostCompSexo")
        self.gridLayout.addWidget(self.TVAmostCompSexo, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Amostra do Sexo"))

import icons_rc
