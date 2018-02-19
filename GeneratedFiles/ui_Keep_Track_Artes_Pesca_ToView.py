# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_Keep_Track_Artes_Pesca_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(983, 94)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.DEData = QtWidgets.QDateEdit(Form)
        self.DEData.setEnabled(False)
        self.DEData.setObjectName("DEData")
        self.gridLayout_2.addWidget(self.DEData, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.LECentro = QtWidgets.QLineEdit(Form)
        self.LECentro.setReadOnly(True)
        self.LECentro.setObjectName("LECentro")
        self.gridLayout_2.addWidget(self.LECentro, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 4, 1, 1)
        self.LERegistador = QtWidgets.QLineEdit(Form)
        self.LERegistador.setReadOnly(True)
        self.LERegistador.setObjectName("LERegistador")
        self.gridLayout_2.addWidget(self.LERegistador, 0, 5, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.PBUp = QtWidgets.QPushButton(Form)
        self.PBUp.setObjectName("PBUp")
        self.gridLayout_3.addWidget(self.PBUp, 0, 1, 2, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LECentroOrigem = QtWidgets.QLineEdit(Form)
        self.LECentroOrigem.setReadOnly(True)
        self.LECentroOrigem.setObjectName("LECentroOrigem")
        self.gridLayout.addWidget(self.LECentroOrigem, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.LEArte = QtWidgets.QLineEdit(Form)
        self.LEArte.setReadOnly(True)
        self.LEArte.setObjectName("LEArte")
        self.gridLayout.addWidget(self.LEArte, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.SBAmostradas = QtWidgets.QSpinBox(Form)
        self.SBAmostradas.setStyleSheet(".SBAmostras{\n"
"background-color:red;\n"
"color:black;\n"
"}")
        self.SBAmostradas.setReadOnly(True)
        self.SBAmostradas.setMaximum(1000)
        self.SBAmostradas.setObjectName("SBAmostradas")
        self.gridLayout.addWidget(self.SBAmostradas, 0, 5, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 2, 1)
        self.PBDown = QtWidgets.QPushButton(Form)
        self.PBDown.setObjectName("PBDown")
        self.gridLayout_3.addWidget(self.PBDown, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Artes de Pesca"))
        self.label.setText(_translate("Form", "Data do Registo:"))
        self.DEData.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label_2.setText(_translate("Form", "Centro:"))
        self.label_3.setText(_translate("Form", "Registador:"))
        self.PBUp.setText(_translate("Form", "⬆︎"))
        self.label_7.setText(_translate("Form", "Amostradas"))
        self.label_10.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Centro de </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Origem da Arte:</p></body></html>"))
        self.label_17.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tipo de</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Uni. Pesca:</p></body></html>"))
        self.PBDown.setText(_translate("Form", "⬇︎"))

import icons_rc
