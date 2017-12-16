# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_CategoriaComercial.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmCatComercialAmostra(object):
    def setupUi(self, frmCatComercialAmostra):
        frmCatComercialAmostra.setObjectName("frmCatComercialAmostra")
        frmCatComercialAmostra.resize(290, 214)
        self.gridLayout_2 = QtWidgets.QGridLayout(frmCatComercialAmostra)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(frmCatComercialAmostra)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)
        self.DSBPeso_total_captura = QtWidgets.QDoubleSpinBox(frmCatComercialAmostra)
        self.DSBPeso_total_captura.setMaximum(10000.99)
        self.DSBPeso_total_captura.setObjectName("DSBPeso_total_captura")
        self.gridLayout_2.addWidget(self.DSBPeso_total_captura, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBSalvar = QtWidgets.QPushButton(frmCatComercialAmostra)
        self.PBSalvar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(frmCatComercialAmostra)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 8, 0, 1, 3)
        self.SBN_Seq_Categoria = QtWidgets.QSpinBox(frmCatComercialAmostra)
        self.SBN_Seq_Categoria.setMaximum(10000)
        self.SBN_Seq_Categoria.setObjectName("SBN_Seq_Categoria")
        self.gridLayout_2.addWidget(self.SBN_Seq_Categoria, 7, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(frmCatComercialAmostra)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 2, 0, 1, 1)
        self.CBCategoria = QtWidgets.QComboBox(frmCatComercialAmostra)
        self.CBCategoria.setObjectName("CBCategoria")
        self.gridLayout_2.addWidget(self.CBCategoria, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(frmCatComercialAmostra)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(frmCatComercialAmostra)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 2, 1, 1)
        self.SBPesoUnidade = QtWidgets.QSpinBox(frmCatComercialAmostra)
        self.SBPesoUnidade.setMaximum(10000)
        self.SBPesoUnidade.setObjectName("SBPesoUnidade")
        self.gridLayout_2.addWidget(self.SBPesoUnidade, 3, 1, 1, 1)

        self.retranslateUi(frmCatComercialAmostra)
        QtCore.QMetaObject.connectSlotsByName(frmCatComercialAmostra)

    def retranslateUi(self, frmCatComercialAmostra):
        _translate = QtCore.QCoreApplication.translate
        frmCatComercialAmostra.setWindowTitle(_translate("frmCatComercialAmostra", "Categoria Comercial"))
        self.label_10.setText(_translate("frmCatComercialAmostra", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nº de Sequencial</p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">de Categoria</p></body></html>"))
        self.label_22.setText(_translate("frmCatComercialAmostra", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">Peso total</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">da Captura</span></p></body></html>"))
        self.label_3.setText(_translate("frmCatComercialAmostra", "Categoria"))
        self.label_23.setText(_translate("frmCatComercialAmostra", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">Peso total</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">da Unidade</p></body></html>"))

import icons_rc
