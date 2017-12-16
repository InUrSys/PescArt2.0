# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_AmostraEspecie.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmEspeciesAmostradas(object):
    def setupUi(self, frmEspeciesAmostradas):
        frmEspeciesAmostradas.setObjectName("frmEspeciesAmostradas")
        frmEspeciesAmostradas.resize(269, 162)
        self.gridLayout_2 = QtWidgets.QGridLayout(frmEspeciesAmostradas)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(frmEspeciesAmostradas)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(frmEspeciesAmostradas)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.DSBPesoAmost = QtWidgets.QDoubleSpinBox(frmEspeciesAmostradas)
        self.DSBPesoAmost.setMaximum(10000.99)
        self.DSBPesoAmost.setObjectName("DSBPesoAmost")
        self.gridLayout_2.addWidget(self.DSBPesoAmost, 1, 2, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBSalvar = QtWidgets.QPushButton(frmEspeciesAmostradas)
        self.PBSalvar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(frmEspeciesAmostradas)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 4)
        self.CBEspecies = MyComboBox(frmEspeciesAmostradas)
        self.CBEspecies.setObjectName("CBEspecies")
        self.gridLayout_2.addWidget(self.CBEspecies, 0, 1, 1, 3)
        self.SBN_Indiv = QtWidgets.QSpinBox(frmEspeciesAmostradas)
        self.SBN_Indiv.setMaximum(10000)
        self.SBN_Indiv.setObjectName("SBN_Indiv")
        self.gridLayout_2.addWidget(self.SBN_Indiv, 2, 2, 1, 2)
        self.label_10 = QtWidgets.QLabel(frmEspeciesAmostradas)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.retranslateUi(frmEspeciesAmostradas)
        QtCore.QMetaObject.connectSlotsByName(frmEspeciesAmostradas)

    def retranslateUi(self, frmEspeciesAmostradas):
        _translate = QtCore.QCoreApplication.translate
        frmEspeciesAmostradas.setWindowTitle(_translate("frmEspeciesAmostradas", "Amostra Da Especie"))
        self.label_11.setText(_translate("frmEspeciesAmostradas", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nº de Individos</p></body></html>"))
        self.label_3.setText(_translate("frmEspeciesAmostradas", "Especies"))
        self.label_10.setText(_translate("frmEspeciesAmostradas", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Peso</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Amostraddo</p></body></html>"))

from CustomWidgets import MyComboBox
import icons_rc
