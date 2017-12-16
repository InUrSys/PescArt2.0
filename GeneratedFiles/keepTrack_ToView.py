# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/keepTrack_ToView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(972, 153)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.DEData = QtWidgets.QDateEdit(Form)
        self.DEData.setEnabled(False)
        self.DEData.setObjectName("DEData")
        self.gridLayout.addWidget(self.DEData, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.LECentro = QtWidgets.QLineEdit(Form)
        self.LECentro.setReadOnly(True)
        self.LECentro.setObjectName("LECentro")
        self.gridLayout.addWidget(self.LECentro, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.LERegistador = QtWidgets.QLineEdit(Form)
        self.LERegistador.setReadOnly(True)
        self.LERegistador.setObjectName("LERegistador")
        self.gridLayout.addWidget(self.LERegistador, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.LEArte = QtWidgets.QLineEdit(Form)
        self.LEArte.setReadOnly(True)
        self.LEArte.setObjectName("LEArte")
        self.gridLayout.addWidget(self.LEArte, 0, 7, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.LEEmbarcacao = QtWidgets.QLineEdit(Form)
        self.LEEmbarcacao.setReadOnly(True)
        self.LEEmbarcacao.setObjectName("LEEmbarcacao")
        self.gridLayout_2.addWidget(self.LEEmbarcacao, 0, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 2, 1, 1)
        self.LETipPescaUnidade = QtWidgets.QLineEdit(Form)
        self.LETipPescaUnidade.setReadOnly(True)
        self.LETipPescaUnidade.setObjectName("LETipPescaUnidade")
        self.gridLayout_2.addWidget(self.LETipPescaUnidade, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 4, 1, 1)
        self.LECentroOrigem = QtWidgets.QLineEdit(Form)
        self.LECentroOrigem.setReadOnly(True)
        self.LECentroOrigem.setObjectName("LECentroOrigem")
        self.gridLayout_2.addWidget(self.LECentroOrigem, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 2, 2)
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 3, 2, 1)
        self.LECatComercial = QtWidgets.QLineEdit(Form)
        self.LECatComercial.setReadOnly(True)
        self.LECatComercial.setObjectName("LECatComercial")
        self.gridLayout_3.addWidget(self.LECatComercial, 0, 2, 2, 1)
        self.LEMetodoSelec = QtWidgets.QLineEdit(Form)
        self.LEMetodoSelec.setReadOnly(True)
        self.LEMetodoSelec.setObjectName("LEMetodoSelec")
        self.gridLayout_3.addWidget(self.LEMetodoSelec, 0, 4, 2, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Keep Track"))
        self.label.setText(_translate("Form", "Data do Registo:"))
        self.DEData.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label_2.setText(_translate("Form", "Centro:"))
        self.label_3.setText(_translate("Form", "Registador:"))
        self.label_4.setText(_translate("Form", "Arte:"))
        self.label_10.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Centro de </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Origem da Arte:</p></body></html>"))
        self.label_16.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tipo de</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Uni. Pesca:</p></body></html>"))
        self.label_7.setText(_translate("Form", "Embarcação"))
        self.label_13.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Categoria</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Comercial</p></body></html>"))
        self.label_14.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Metodo de Selecao:</p></body></html>"))

