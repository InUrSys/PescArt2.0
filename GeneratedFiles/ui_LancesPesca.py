# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_LancesPesca.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmLancesPesca(object):
    def setupUi(self, frmLancesPesca):
        frmLancesPesca.setObjectName("frmLancesPesca")
        frmLancesPesca.resize(209, 192)
        self.gridLayout_2 = QtWidgets.QGridLayout(frmLancesPesca)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBSalvar = QtWidgets.QPushButton(frmLancesPesca)
        self.PBSalvar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(frmLancesPesca)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(frmLancesPesca)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.TEInicio = QtWidgets.QTimeEdit(frmLancesPesca)
        self.TEInicio.setObjectName("TEInicio")
        self.gridLayout_2.addWidget(self.TEInicio, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(frmLancesPesca)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(frmLancesPesca)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.DSBCapTotal = QtWidgets.QDoubleSpinBox(frmLancesPesca)
        self.DSBCapTotal.setMaximum(10000.99)
        self.DSBCapTotal.setObjectName("DSBCapTotal")
        self.gridLayout_2.addWidget(self.DSBCapTotal, 1, 1, 1, 2)
        self.TEFim = QtWidgets.QTimeEdit(frmLancesPesca)
        self.TEFim.setObjectName("TEFim")
        self.gridLayout_2.addWidget(self.TEFim, 3, 1, 1, 2)
        self.SBNSeqLance = QtWidgets.QSpinBox(frmLancesPesca)
        self.SBNSeqLance.setObjectName("SBNSeqLance")
        self.gridLayout_2.addWidget(self.SBNSeqLance, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(frmLancesPesca)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(frmLancesPesca)
        QtCore.QMetaObject.connectSlotsByName(frmLancesPesca)

    def retranslateUi(self, frmLancesPesca):
        _translate = QtCore.QCoreApplication.translate
        frmLancesPesca.setWindowTitle(_translate("frmLancesPesca", "Lances de Pesca"))
        self.label_3.setText(_translate("frmLancesPesca", "Captura Total:"))
        self.TEInicio.setSpecialValueText(_translate("frmLancesPesca", "--:--"))
        self.label_4.setText(_translate("frmLancesPesca", "Inicio:"))
        self.label_7.setText(_translate("frmLancesPesca", "Fim:"))
        self.TEFim.setSpecialValueText(_translate("frmLancesPesca", "--:--"))
        self.label.setText(_translate("frmLancesPesca", "Nº do Lance:"))

import icons_rc
