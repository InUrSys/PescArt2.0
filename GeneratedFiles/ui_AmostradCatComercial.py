# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_AmostradCatComercial.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmAmostCatComercial(object):
    def setupUi(self, frmAmostCatComercial):
        frmAmostCatComercial.setObjectName("frmAmostCatComercial")
        frmAmostCatComercial.resize(292, 199)
        self.gridLayout = QtWidgets.QGridLayout(frmAmostCatComercial)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(frmAmostCatComercial)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.PBSalvar = QtWidgets.QPushButton(frmAmostCatComercial)
        self.PBSalvar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 6, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(frmAmostCatComercial)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 6, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(frmAmostCatComercial)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(frmAmostCatComercial)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.LEComentarios = QtWidgets.QLineEdit(frmAmostCatComercial)
        self.LEComentarios.setObjectName("LEComentarios")
        self.gridLayout.addWidget(self.LEComentarios, 5, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(frmAmostCatComercial)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.CBMetSelecao = QtWidgets.QComboBox(frmAmostCatComercial)
        self.CBMetSelecao.setObjectName("CBMetSelecao")
        self.gridLayout.addWidget(self.CBMetSelecao, 1, 1, 1, 2)
        self.DSBPeso = QtWidgets.QDoubleSpinBox(frmAmostCatComercial)
        self.DSBPeso.setMaximum(10000.99)
        self.DSBPeso.setObjectName("DSBPeso")
        self.gridLayout.addWidget(self.DSBPeso, 2, 1, 1, 1)
        self.SBN_Indiv_Amost = QtWidgets.QSpinBox(frmAmostCatComercial)
        self.SBN_Indiv_Amost.setMaximum(10000)
        self.SBN_Indiv_Amost.setObjectName("SBN_Indiv_Amost")
        self.gridLayout.addWidget(self.SBN_Indiv_Amost, 4, 1, 1, 1)

        self.retranslateUi(frmAmostCatComercial)
        QtCore.QMetaObject.connectSlotsByName(frmAmostCatComercial)

    def retranslateUi(self, frmAmostCatComercial):
        _translate = QtCore.QCoreApplication.translate
        frmAmostCatComercial.setWindowTitle(_translate("frmAmostCatComercial", "Amostra da Categoria"))
        self.label_13.setText(_translate("frmAmostCatComercial", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Metodo de</p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Selecao</p></body></html>"))
        self.label_4.setText(_translate("frmAmostCatComercial", "Comentarios"))
        self.label_7.setText(_translate("frmAmostCatComercial", "Peso Amostrado"))
        self.LEComentarios.setPlaceholderText(_translate("frmAmostCatComercial", "Ex:Nota, Obs…"))
        self.label_12.setText(_translate("frmAmostCatComercial", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nº Amostrados</p></body></html>"))

import icons_rc
