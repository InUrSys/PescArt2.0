# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_Artes_Pesca_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(413, 256)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionarArtes = QtWidgets.QPushButton(Form)
        self.PBAdicionarArtes.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionarArtes.setIcon(icon)
        self.PBAdicionarArtes.setObjectName("PBAdicionarArtes")
        self.gridLayout.addWidget(self.PBAdicionarArtes, 1, 0, 1, 1)
        self.PBEditarArtes = QtWidgets.QPushButton(Form)
        self.PBEditarArtes.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditarArtes.setIcon(icon1)
        self.PBEditarArtes.setObjectName("PBEditarArtes")
        self.gridLayout.addWidget(self.PBEditarArtes, 1, 1, 1, 1)
        self.TVArtePesca = QtWidgets.QTableView(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TVArtePesca.setFont(font)
        self.TVArtePesca.setObjectName("TVArtePesca")
        self.gridLayout.addWidget(self.TVArtePesca, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Artes de Pesca"))

import icons_rc
