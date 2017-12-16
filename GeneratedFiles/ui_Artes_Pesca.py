# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_Artes_Pesca.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmArtesPesca(object):
    def setupUi(self, frmArtesPesca):
        frmArtesPesca.setObjectName("frmArtesPesca")
        frmArtesPesca.resize(359, 308)
        self.gridLayout_2 = QtWidgets.QGridLayout(frmArtesPesca)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(frmArtesPesca)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.CBProvincia = QtWidgets.QComboBox(frmArtesPesca)
        self.CBProvincia.setObjectName("CBProvincia")
        self.gridLayout_2.addWidget(self.CBProvincia, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(frmArtesPesca)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(frmArtesPesca)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 2, 1, 1)
        self.CBDistrito = QtWidgets.QComboBox(frmArtesPesca)
        self.CBDistrito.setObjectName("CBDistrito")
        self.gridLayout_2.addWidget(self.CBDistrito, 1, 1, 1, 2)
        self.CBArtes = MyComboBox(frmArtesPesca)
        self.CBArtes.setObjectName("CBArtes")
        self.gridLayout_2.addWidget(self.CBArtes, 4, 1, 1, 2)
        self.label = QtWidgets.QLabel(frmArtesPesca)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 6, 2, 1, 1)
        self.CBCentroPesca = QtWidgets.QComboBox(frmArtesPesca)
        self.CBCentroPesca.setObjectName("CBCentroPesca")
        self.gridLayout_2.addWidget(self.CBCentroPesca, 3, 1, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBSalvar = QtWidgets.QPushButton(frmArtesPesca)
        self.PBSalvar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(frmArtesPesca)
        self.PBCancelar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 8, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(frmArtesPesca)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.CBPosto = QtWidgets.QComboBox(frmArtesPesca)
        self.CBPosto.setObjectName("CBPosto")
        self.gridLayout_2.addWidget(self.CBPosto, 2, 1, 1, 2)
        self.SBActivas = QtWidgets.QSpinBox(frmArtesPesca)
        self.SBActivas.setMaximum(1000)
        self.SBActivas.setObjectName("SBActivas")
        self.gridLayout_2.addWidget(self.SBActivas, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(frmArtesPesca)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(frmArtesPesca)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(frmArtesPesca)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.SBAmostradas = QtWidgets.QSpinBox(frmArtesPesca)
        self.SBAmostradas.setStyleSheet(".SBAmostras{\n"
"background-color:red;\n"
"color:black;\n"
"}")
        self.SBAmostradas.setMaximum(1000)
        self.SBAmostradas.setObjectName("SBAmostradas")
        self.gridLayout_2.addWidget(self.SBAmostradas, 7, 1, 1, 1)
        self.SBN_Activas = QtWidgets.QSpinBox(frmArtesPesca)
        self.SBN_Activas.setMaximum(1000)
        self.SBN_Activas.setObjectName("SBN_Activas")
        self.gridLayout_2.addWidget(self.SBN_Activas, 6, 1, 1, 1)

        self.retranslateUi(frmArtesPesca)
        QtCore.QMetaObject.connectSlotsByName(frmArtesPesca)

    def retranslateUi(self, frmArtesPesca):
        _translate = QtCore.QCoreApplication.translate
        frmArtesPesca.setWindowTitle(_translate("frmArtesPesca", "Artes de Pesca"))
        self.label_4.setText(_translate("frmArtesPesca", "Posto Administrativo"))
        self.label_2.setText(_translate("frmArtesPesca", "Activas"))
        self.label_7.setText(_translate("frmArtesPesca", "Amostradas"))
        self.label.setText(_translate("frmArtesPesca", "Centro de Pesca"))
        self.label_9.setText(_translate("frmArtesPesca", "Provincia"))
        self.label_8.setText(_translate("frmArtesPesca", "Artes Amostradas"))
        self.label_3.setText(_translate("frmArtesPesca", "Nao Activas"))
        self.label_10.setText(_translate("frmArtesPesca", "Distrito"))

from CustomWidgets import MyComboBox
import icons_rc
