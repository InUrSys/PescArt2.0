# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_user_conf.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 434)
        Form.setStyleSheet("#Form\n"
"{\n"
"background-color: #f0f0f0;\n"
"}\n"
"\n"
".QLineEdit {background-color: rgb(255, 255, 255); \n"
"border-radius: 7px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"}")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LEId = QtWidgets.QLineEdit(Form)
        self.LEId.setObjectName("LEId")
        self.gridLayout.addWidget(self.LEId, 0, 1, 1, 1)
        self.CBLevel = QtWidgets.QComboBox(Form)
        self.CBLevel.setObjectName("CBLevel")
        self.gridLayout.addWidget(self.CBLevel, 3, 1, 2, 1)
        self.LViewUser = QtWidgets.QListView(Form)
        self.LViewUser.setObjectName("LViewUser")
        self.gridLayout.addWidget(self.LViewUser, 0, 2, 7, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.PTEInformacao = QtWidgets.QPlainTextEdit(Form)
        self.PTEInformacao.setObjectName("PTEInformacao")
        self.gridLayout.addWidget(self.PTEInformacao, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.LENome = QtWidgets.QLineEdit(Form)
        self.LENome.setObjectName("LENome")
        self.gridLayout.addWidget(self.LENome, 1, 1, 1, 1)
        self.LEPsw = QtWidgets.QLineEdit(Form)
        self.LEPsw.setObjectName("LEPsw")
        self.gridLayout.addWidget(self.LEPsw, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 2, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PBSalvar = QtWidgets.QPushButton(Form)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout_2.addWidget(self.PBSalvar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(Form)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout_2.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 7, 0, 1, 3)
        self.CHBActivo = QtWidgets.QCheckBox(Form)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout.addWidget(self.CHBActivo, 6, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adcionar/Editar Usuarios"))
        self.label_5.setText(_translate("Form", "Informacao:"))
        self.label.setText(_translate("Form", "ID:"))
        self.label_3.setText(_translate("Form", "Nome:"))
        self.label_6.setText(_translate("Form", "credencial:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.PBSalvar.setText(_translate("Form", "Salvar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))
        self.CHBActivo.setText(_translate("Form", "Activo"))

import icons_rc
import images_rc
