# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_AmostEspeEspecie.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmAmostEspeEspecieAmost(object):
    def setupUi(self, frmAmostEspeEspecieAmost):
        frmAmostEspeEspecieAmost.setObjectName("frmAmostEspeEspecieAmost")
        frmAmostEspeEspecieAmost.resize(296, 207)
        self.gridLayout_2 = QtWidgets.QGridLayout(frmAmostEspeEspecieAmost)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.DSBPeso = QtWidgets.QDoubleSpinBox(frmAmostEspeEspecieAmost)
        self.DSBPeso.setMaximum(10000.99)
        self.DSBPeso.setObjectName("DSBPeso")
        self.gridLayout_2.addWidget(self.DSBPeso, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(frmAmostEspeEspecieAmost)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.LEComentarios = QtWidgets.QLineEdit(frmAmostEspeEspecieAmost)
        self.LEComentarios.setObjectName("LEComentarios")
        self.gridLayout_2.addWidget(self.LEComentarios, 5, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(frmAmostEspeEspecieAmost)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBSalvar = QtWidgets.QPushButton(frmAmostEspeEspecieAmost)
        self.PBSalvar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(frmAmostEspeEspecieAmost)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 6, 0, 1, 3)
        self.label_12 = QtWidgets.QLabel(frmAmostEspeEspecieAmost)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)
        self.SBN_indiv_Amostrados = QtWidgets.QSpinBox(frmAmostEspeEspecieAmost)
        self.SBN_indiv_Amostrados.setMaximum(10000)
        self.SBN_indiv_Amostrados.setObjectName("SBN_indiv_Amostrados")
        self.gridLayout_2.addWidget(self.SBN_indiv_Amostrados, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(frmAmostEspeEspecieAmost)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.CBMetSelecao = QtWidgets.QComboBox(frmAmostEspeEspecieAmost)
        self.CBMetSelecao.setObjectName("CBMetSelecao")
        self.gridLayout_2.addWidget(self.CBMetSelecao, 0, 1, 1, 2)

        self.retranslateUi(frmAmostEspeEspecieAmost)
        QtCore.QMetaObject.connectSlotsByName(frmAmostEspeEspecieAmost)

    def retranslateUi(self, frmAmostEspeEspecieAmost):
        _translate = QtCore.QCoreApplication.translate
        frmAmostEspeEspecieAmost.setWindowTitle(_translate("frmAmostEspeEspecieAmost", "Amostra Especifica Da Especie"))
        self.label_6.setText(_translate("frmAmostEspeEspecieAmost", "Peso"))
        self.LEComentarios.setPlaceholderText(_translate("frmAmostEspeEspecieAmost", "Ex:Nota, Obs…"))
        self.label_4.setText(_translate("frmAmostEspeEspecieAmost", "Comentarios"))
        self.label_12.setText(_translate("frmAmostEspeEspecieAmost", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nº de Individos </p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Amostrados</p></body></html>"))
        self.label_13.setText(_translate("frmAmostEspeEspecieAmost", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Metodo de</p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Selecao</p></body></html>"))

import icons_rc
