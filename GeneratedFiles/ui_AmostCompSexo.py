# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_AmostCompSexo.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmAmostCompSexo(object):
    def setupUi(self, frmAmostCompSexo):
        frmAmostCompSexo.setObjectName("frmAmostCompSexo")
        frmAmostCompSexo.resize(349, 357)
        self.gridLayout_2 = QtWidgets.QGridLayout(frmAmostCompSexo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(frmAmostCompSexo)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.CBAproximacao = QtWidgets.QComboBox(frmAmostCompSexo)
        self.CBAproximacao.setObjectName("CBAproximacao")
        self.gridLayout_2.addWidget(self.CBAproximacao, 4, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(frmAmostCompSexo)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 12, 0, 1, 1)
        self.CBMetodoSelec = QtWidgets.QComboBox(frmAmostCompSexo)
        self.CBMetodoSelec.setObjectName("CBMetodoSelec")
        self.gridLayout_2.addWidget(self.CBMetodoSelec, 1, 1, 1, 2)
        self.CBMedidaComp = QtWidgets.QComboBox(frmAmostCompSexo)
        self.CBMedidaComp.setObjectName("CBMedidaComp")
        self.gridLayout_2.addWidget(self.CBMedidaComp, 3, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(frmAmostCompSexo)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(frmAmostCompSexo)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 8, 2, 1, 1)
        self.DSBPeso = QtWidgets.QDoubleSpinBox(frmAmostCompSexo)
        self.DSBPeso.setMaximum(10000.99)
        self.DSBPeso.setObjectName("DSBPeso")
        self.gridLayout_2.addWidget(self.DSBPeso, 8, 1, 1, 1)
        self.CBEspecies = QtWidgets.QComboBox(frmAmostCompSexo)
        self.CBEspecies.setEnabled(False)
        self.CBEspecies.setObjectName("CBEspecies")
        self.gridLayout_2.addWidget(self.CBEspecies, 2, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(frmAmostCompSexo)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.LEComentarios = QtWidgets.QLineEdit(frmAmostCompSexo)
        self.LEComentarios.setObjectName("LEComentarios")
        self.gridLayout_2.addWidget(self.LEComentarios, 13, 1, 1, 2)
        self.CBIntervaloClass = QtWidgets.QComboBox(frmAmostCompSexo)
        self.CBIntervaloClass.setObjectName("CBIntervaloClass")
        self.gridLayout_2.addWidget(self.CBIntervaloClass, 5, 1, 1, 2)
        self.label_23 = QtWidgets.QLabel(frmAmostCompSexo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 8, 0, 1, 1)
        self.SB_N_indiv_amostrados = QtWidgets.QSpinBox(frmAmostCompSexo)
        self.SB_N_indiv_amostrados.setMaximum(10000)
        self.SB_N_indiv_amostrados.setObjectName("SB_N_indiv_amostrados")
        self.gridLayout_2.addWidget(self.SB_N_indiv_amostrados, 12, 1, 1, 1)
        self.DBSCompMinimo = QtWidgets.QDoubleSpinBox(frmAmostCompSexo)
        self.DBSCompMinimo.setMaximum(10000.99)
        self.DBSCompMinimo.setObjectName("DBSCompMinimo")
        self.gridLayout_2.addWidget(self.DBSCompMinimo, 7, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(frmAmostCompSexo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(frmAmostCompSexo)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBSalvar = QtWidgets.QPushButton(frmAmostCompSexo)
        self.PBSalvar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(frmAmostCompSexo)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 14, 0, 1, 3)
        self.label = QtWidgets.QLabel(frmAmostCompSexo)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 13, 0, 1, 1)

        self.retranslateUi(frmAmostCompSexo)
        QtCore.QMetaObject.connectSlotsByName(frmAmostCompSexo)

    def retranslateUi(self, frmAmostCompSexo):
        _translate = QtCore.QCoreApplication.translate
        frmAmostCompSexo.setWindowTitle(_translate("frmAmostCompSexo", "Amostra Comp. Sexo"))
        self.label_6.setText(_translate("frmAmostCompSexo", "Aproximacao"))
        self.label_10.setText(_translate("frmAmostCompSexo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nº de Indiv</p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Amostrados</p></body></html>"))
        self.label_7.setText(_translate("frmAmostCompSexo", "Intervalo de Casse"))
        self.label_3.setText(_translate("frmAmostCompSexo", "Metodo de Selecao"))
        self.label_8.setText(_translate("frmAmostCompSexo", "Especie"))
        self.label_23.setText(_translate("frmAmostCompSexo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">Peso</span></p></body></html>"))
        self.label_22.setText(_translate("frmAmostCompSexo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">Comprimento</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">Minimo</span></p></body></html>"))
        self.label_4.setText(_translate("frmAmostCompSexo", "Medida de Comp."))
        self.label.setText(_translate("frmAmostCompSexo", "Comentarios"))

import icons_rc
