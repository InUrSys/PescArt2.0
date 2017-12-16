# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_Ficha_Recolha_Tab_Amostras.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmFichaRecolhaAmostras(object):
    def setupUi(self, frmFichaRecolhaAmostras):
        frmFichaRecolhaAmostras.setObjectName("frmFichaRecolhaAmostras")
        frmFichaRecolhaAmostras.resize(1060, 701)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmFichaRecolhaAmostras.sizePolicy().hasHeightForWidth())
        frmFichaRecolhaAmostras.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmFichaRecolhaAmostras.setWindowIcon(icon)
        frmFichaRecolhaAmostras.setStyleSheet("#tabAmostra {\n"
"background-image:url(:/newPrefix/Background/Almora.jpg);\n"
"}\n"
"QTabBar::tab {color: Black;}\n"
"\n"
"#frmFichaRecolhaAmostras {\n"
"Background-color: #7FFFD4;\n"
"border-image:url(:/newPrefix/Background/Almora.jpg)\n"
"}")
        self.gridLayout_6 = QtWidgets.QGridLayout(frmFichaRecolhaAmostras)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabAmostra = QtWidgets.QTabWidget(frmFichaRecolhaAmostras)
        self.tabAmostra.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabAmostra.setObjectName("tabAmostra")
        self.tabViagem = QtWidgets.QWidget()
        self.tabViagem.setObjectName("tabViagem")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabViagem)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.GLtabViagem = QtWidgets.QGridLayout()
        self.GLtabViagem.setObjectName("GLtabViagem")
        self.gridLayout_2.addLayout(self.GLtabViagem, 0, 0, 1, 1)
        self.tabAmostra.addTab(self.tabViagem, "")
        self.tbAmostras = QtWidgets.QWidget()
        self.tbAmostras.setObjectName("tbAmostras")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tbAmostras)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.GLtabAmostEspecies = QtWidgets.QGridLayout()
        self.GLtabAmostEspecies.setObjectName("GLtabAmostEspecies")
        self.gridLayout_4.addLayout(self.GLtabAmostEspecies, 0, 0, 1, 1)
        self.tabAmostra.addTab(self.tbAmostras, "")
        self.gridLayout_6.addWidget(self.tabAmostra, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 0, 2, 1)
        self.PBVoltar = QtWidgets.QPushButton(frmFichaRecolhaAmostras)
        self.PBVoltar.setObjectName("PBVoltar")
        self.gridLayout_5.addWidget(self.PBVoltar, 0, 1, 2, 1)
        self.PBSair = QtWidgets.QPushButton(frmFichaRecolhaAmostras)
        self.PBSair.setObjectName("PBSair")
        self.gridLayout_5.addWidget(self.PBSair, 0, 2, 2, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.retranslateUi(frmFichaRecolhaAmostras)
        self.tabAmostra.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmFichaRecolhaAmostras)

    def retranslateUi(self, frmFichaRecolhaAmostras):
        _translate = QtCore.QCoreApplication.translate
        frmFichaRecolhaAmostras.setWindowTitle(_translate("frmFichaRecolhaAmostras", "Ficha de Recolha"))
        self.tabAmostra.setTabText(self.tabAmostra.indexOf(self.tabViagem), _translate("frmFichaRecolhaAmostras", "Viagem"))
        self.tabAmostra.setTabText(self.tabAmostra.indexOf(self.tbAmostras), _translate("frmFichaRecolhaAmostras", "Amos. Especie"))
        self.PBVoltar.setText(_translate("frmFichaRecolhaAmostras", "Voltar"))
        self.PBSair.setText(_translate("frmFichaRecolhaAmostras", "Sair"))

import icons_rc
import images_rc
