# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_ViagemPesca_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(977, 175)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAdicionar = QtWidgets.QPushButton(Form)
        self.PBAdicionar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionar.setIcon(icon)
        self.PBAdicionar.setObjectName("PBAdicionar")
        self.gridLayout.addWidget(self.PBAdicionar, 2, 0, 1, 1)
        self.PBEditar = QtWidgets.QPushButton(Form)
        self.PBEditar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditar.setIcon(icon1)
        self.PBEditar.setObjectName("PBEditar")
        self.gridLayout.addWidget(self.PBEditar, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 2)
        self.TVViagens = QtWidgets.QTableView(Form)
        self.TVViagens.setObjectName("TVViagens")
        self.gridLayout.addWidget(self.TVViagens, 0, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "VIAGEMPESCA_TOVIEW"))

import icons_rc
