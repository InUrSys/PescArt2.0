# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_MainRef.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(937, 617)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/stats-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        MainForm.setStyleSheet(".QPushButton {\n"
"border-radius: 12px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: black\n"
"}\n"
"\n"
".QPushButton:pressed { \n"
"background-color: DodgerBlue; \n"
"}\n"
"\n"
".QPushButton:focus:pressed { \n"
"background-color: #3c3c3c; \n"
"}\n"
"\n"
".QPushButton:focus { \n"
"background-color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"background-color: Gray; \n"
"}\n"
"\n"
"QPushButton:checked { \n"
"background-color: DodgerBlue; \n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(MainForm)
        self.gridLayout.setObjectName("gridLayout")
        self.LBGrupo = QtWidgets.QLabel(MainForm)
        self.LBGrupo.setObjectName("LBGrupo")
        self.gridLayout.addWidget(self.LBGrupo, 0, 0, 1, 1)
        self.CBGrupo = QtWidgets.QComboBox(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CBGrupo.sizePolicy().hasHeightForWidth())
        self.CBGrupo.setSizePolicy(sizePolicy)
        self.CBGrupo.setStyleSheet(".QcomboBox {background-color: rgb(255, 255, 255); \n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: black\n"
"}")
        self.CBGrupo.setObjectName("CBGrupo")
        self.gridLayout.addWidget(self.CBGrupo, 0, 1, 1, 1)
        self.TVMain = QtWidgets.QTableView(MainForm)
        self.TVMain.setStyleSheet(".QTableView {background-color: rgb(255, 255, 255); \n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: black;}\n"
"")
        self.TVMain.setObjectName("TVMain")
        self.gridLayout.addWidget(self.TVMain, 1, 0, 1, 7)
        self.LBTitulo = QtWidgets.QLabel(MainForm)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LBTitulo.setFont(font)
        self.LBTitulo.setObjectName("LBTitulo")
        self.gridLayout.addWidget(self.LBTitulo, 0, 3, 1, 1)
        self.LEFiltro = QtWidgets.QLineEdit(MainForm)
        self.LEFiltro.setStyleSheet(".QLineEdit {background-color: rgb(255, 255, 255); \n"
"border-radius: 7px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: black\n"
"}")
        self.LEFiltro.setObjectName("LEFiltro")
        self.gridLayout.addWidget(self.LEFiltro, 0, 6, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.LBFiltro = QtWidgets.QLabel(MainForm)
        self.LBFiltro.setObjectName("LBFiltro")
        self.gridLayout.addWidget(self.LBFiltro, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(219, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.LBwhois = QtWidgets.QLabel(MainForm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LBwhois.setFont(font)
        self.LBwhois.setFrameShape(QtWidgets.QFrame.Box)
        self.LBwhois.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LBwhois.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LBwhois.setObjectName("LBwhois")
        self.gridLayout.addWidget(self.LBwhois, 2, 0, 1, 7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PBProcurar = QtWidgets.QPushButton(MainForm)
        self.PBProcurar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/001-search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBProcurar.setIcon(icon1)
        self.PBProcurar.setIconSize(QtCore.QSize(25, 25))
        self.PBProcurar.setCheckable(False)
        self.PBProcurar.setChecked(False)
        self.PBProcurar.setObjectName("PBProcurar")
        self.verticalLayout.addWidget(self.PBProcurar)
        self.PBAtualizar = QtWidgets.QPushButton(MainForm)
        self.PBAtualizar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAtualizar.setIcon(icon2)
        self.PBAtualizar.setIconSize(QtCore.QSize(25, 25))
        self.PBAtualizar.setObjectName("PBAtualizar")
        self.verticalLayout.addWidget(self.PBAtualizar)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.PBAdicionar = QtWidgets.QPushButton(MainForm)
        self.PBAdicionar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/004-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBAdicionar.setIcon(icon3)
        self.PBAdicionar.setIconSize(QtCore.QSize(25, 25))
        self.PBAdicionar.setFlat(False)
        self.PBAdicionar.setObjectName("PBAdicionar")
        self.verticalLayout.addWidget(self.PBAdicionar)
        self.PBEditar = QtWidgets.QPushButton(MainForm)
        self.PBEditar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/005-writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBEditar.setIcon(icon4)
        self.PBEditar.setIconSize(QtCore.QSize(25, 25))
        self.PBEditar.setFlat(False)
        self.PBEditar.setObjectName("PBEditar")
        self.verticalLayout.addWidget(self.PBEditar)
        self.PBCancelar = QtWidgets.QPushButton(MainForm)
        self.PBCancelar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon5)
        self.PBCancelar.setIconSize(QtCore.QSize(25, 25))
        self.PBCancelar.setFlat(False)
        self.PBCancelar.setObjectName("PBCancelar")
        self.verticalLayout.addWidget(self.PBCancelar)
        self.gridLayout.addLayout(self.verticalLayout, 1, 7, 2, 1)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Depende"))
        self.LBGrupo.setText(_translate("MainForm", "Grupo:"))
        self.LBTitulo.setText(_translate("MainForm", "Nome Da Tabela "))
        self.LBFiltro.setText(_translate("MainForm", "Filtro:"))
        self.LBwhois.setText(_translate("MainForm", "UserName: Chernomirdin Da Costa Macuvele"))
        self.PBAdicionar.setWhatsThis(_translate("MainForm", "Adicionar"))
        self.PBEditar.setWhatsThis(_translate("MainForm", "Editar"))
        self.PBCancelar.setWhatsThis(_translate("MainForm", "Apagar"))

import icons_rc
import images_rc
