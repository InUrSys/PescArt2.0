# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_simpleSearch.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 300)
        self.TView = QtWidgets.QTableView(Form)
        self.TView.setGeometry(QtCore.QRect(10, 53, 362, 201))
        self.TView.setObjectName("TView")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 260, 361, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PBexit = QtWidgets.QPushButton(self.layoutWidget)
        self.PBexit.setObjectName("PBexit")
        self.gridLayout.addWidget(self.PBexit, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.PBOK = QtWidgets.QPushButton(self.layoutWidget)
        self.PBOK.setObjectName("PBOK")
        self.gridLayout.addWidget(self.PBOK, 0, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 361, 33))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.LENome = QtWidgets.QLineEdit(self.layoutWidget1)
        self.LENome.setObjectName("LENome")
        self.gridLayout_2.addWidget(self.LENome, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Search"))
        self.PBexit.setText(_translate("Form", "Cancelar"))
        self.PBOK.setText(_translate("Form", "OK"))
        self.label.setText(_translate("Form", "Nome:"))

import icons_rc
