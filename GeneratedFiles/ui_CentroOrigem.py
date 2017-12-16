# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_CentroOrigem.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(256, 310)
        self.gridLayout = QtWidgets.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.CBProvincia = QtWidgets.QComboBox(dialog)
        self.CBProvincia.setObjectName("CBProvincia")
        self.gridLayout.addWidget(self.CBProvincia, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.CBDistrito = QtWidgets.QComboBox(dialog)
        self.CBDistrito.setObjectName("CBDistrito")
        self.gridLayout.addWidget(self.CBDistrito, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.CBMunicipio = QtWidgets.QComboBox(dialog)
        self.CBMunicipio.setObjectName("CBMunicipio")
        self.gridLayout.addWidget(self.CBMunicipio, 5, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 1)

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Centro De Origem"))
        self.label_6.setText(_translate("dialog", "Provincia"))
        self.label_5.setText(_translate("dialog", "Distrito"))
        self.label_4.setText(_translate("dialog", "Municipio"))

