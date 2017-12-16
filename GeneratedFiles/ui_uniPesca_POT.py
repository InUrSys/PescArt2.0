# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PscArt2.0.X/UserInt/ui_uniPesca_POT.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 214)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 3)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 4, 0, 1, 3)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 3)
        self.TabUniPesca_LEN_Sequencial = QtWidgets.QLineEdit(Form)
        self.TabUniPesca_LEN_Sequencial.setReadOnly(True)
        self.TabUniPesca_LEN_Sequencial.setObjectName("TabUniPesca_LEN_Sequencial")
        self.gridLayout_4.addWidget(self.TabUniPesca_LEN_Sequencial, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 4, 1, 1)
        self.TabUniPesca_LENome = QtWidgets.QLineEdit(Form)
        self.TabUniPesca_LENome.setMaxLength(25)
        self.TabUniPesca_LENome.setObjectName("TabUniPesca_LENome")
        self.gridLayout_4.addWidget(self.TabUniPesca_LENome, 1, 3, 1, 2)
        self.TabUniPesca_LEMatricula = QtWidgets.QLineEdit(Form)
        self.TabUniPesca_LEMatricula.setMaxLength(15)
        self.TabUniPesca_LEMatricula.setObjectName("TabUniPesca_LEMatricula")
        self.gridLayout_4.addWidget(self.TabUniPesca_LEMatricula, 2, 3, 1, 2)
        self.TabUniPesca_CBMotor = QtWidgets.QComboBox(Form)
        self.TabUniPesca_CBMotor.setObjectName("TabUniPesca_CBMotor")
        self.gridLayout_4.addWidget(self.TabUniPesca_CBMotor, 3, 3, 1, 2)
        self.TabUniPesca_CBArtePrincinpal = QtWidgets.QComboBox(Form)
        self.TabUniPesca_CBArtePrincinpal.setObjectName("TabUniPesca_CBArtePrincinpal")
        self.gridLayout_4.addWidget(self.TabUniPesca_CBArtePrincinpal, 4, 3, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.PBGuardar = QtWidgets.QPushButton(self.splitter)
        self.PBGuardar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBGuardar.setIcon(icon)
        self.PBGuardar.setObjectName("PBGuardar")
        self.PBCancelar = QtWidgets.QPushButton(self.splitter)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Unidade de pesca"))
        self.label_9.setText(_translate("Form", "Nome"))
        self.label_11.setText(_translate("Form", "Arte Princinpal"))
        self.label_10.setText(_translate("Form", "Motor"))
        self.label_3.setText(_translate("Form", "Matricula"))
        self.TabUniPesca_LEN_Sequencial.setPlaceholderText(_translate("Form", "Ex:1"))
        self.label_8.setText(_translate("Form", "Numero Sequencial"))
        self.TabUniPesca_LENome.setPlaceholderText(_translate("Form", "Ex:Joao Mateus"))
        self.TabUniPesca_LEMatricula.setPlaceholderText(_translate("Form", "Ex:MZ XXXZ"))

import icons_rc
