# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_AmostraSexo.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmAmostSexo(object):
    def setupUi(self, frmAmostSexo):
        frmAmostSexo.setObjectName("frmAmostSexo")
        frmAmostSexo.resize(286, 163)
        self.gridLayout_2 = QtWidgets.QGridLayout(frmAmostSexo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(frmAmostSexo)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(frmAmostSexo)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.CBSexo = QtWidgets.QComboBox(frmAmostSexo)
        self.CBSexo.setObjectName("CBSexo")
        self.gridLayout_2.addWidget(self.CBSexo, 0, 1, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBSalvar = QtWidgets.QPushButton(frmAmostSexo)
        self.PBSalvar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(frmAmostSexo)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 3)
        self.label_20 = QtWidgets.QLabel(frmAmostSexo)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 2, 0, 1, 1)
        self.DSBPeso = QtWidgets.QDoubleSpinBox(frmAmostSexo)
        self.DSBPeso.setMaximum(10000.99)
        self.DSBPeso.setObjectName("DSBPeso")
        self.gridLayout_2.addWidget(self.DSBPeso, 1, 1, 1, 1)
        self.SBN_indiv = QtWidgets.QSpinBox(frmAmostSexo)
        self.SBN_indiv.setMaximum(10000)
        self.SBN_indiv.setObjectName("SBN_indiv")
        self.gridLayout_2.addWidget(self.SBN_indiv, 2, 1, 1, 1)

        self.retranslateUi(frmAmostSexo)
        QtCore.QMetaObject.connectSlotsByName(frmAmostSexo)

    def retranslateUi(self, frmAmostSexo):
        _translate = QtCore.QCoreApplication.translate
        frmAmostSexo.setWindowTitle(_translate("frmAmostSexo", "Amostra do Sexo"))
        self.label_3.setText(_translate("frmAmostSexo", "Sexo"))
        self.label_4.setText(_translate("frmAmostSexo", "Peso Amost ."))
        self.label_20.setText(_translate("frmAmostSexo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nº de Indiv.</p></body></html>"))

import icons_rc
