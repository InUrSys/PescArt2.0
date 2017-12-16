# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_compAmostra.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmDistComprimento(object):
    def setupUi(self, frmDistComprimento):
        frmDistComprimento.setObjectName("frmDistComprimento")
        frmDistComprimento.resize(376, 576)
        self.gridLayout_2 = QtWidgets.QGridLayout(frmDistComprimento)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBCancelar = QtWidgets.QPushButton(frmDistComprimento)
        self.PBCancelar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 1, 1, 1, 1)
        self.PBSalvar = QtWidgets.QPushButton(frmDistComprimento)
        self.PBSalvar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBSalvar.setIcon(icon1)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout.addWidget(self.PBSalvar, 1, 0, 1, 1)
        self.TWComprimentos = QtWidgets.QTableWidget(frmDistComprimento)
        self.TWComprimentos.setGridStyle(QtCore.Qt.SolidLine)
        self.TWComprimentos.setObjectName("TWComprimentos")
        self.TWComprimentos.setColumnCount(2)
        self.TWComprimentos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TWComprimentos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWComprimentos.setHorizontalHeaderItem(1, item)
        self.TWComprimentos.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.TWComprimentos, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.retranslateUi(frmDistComprimento)
        QtCore.QMetaObject.connectSlotsByName(frmDistComprimento)

    def retranslateUi(self, frmDistComprimento):
        _translate = QtCore.QCoreApplication.translate
        frmDistComprimento.setWindowTitle(_translate("frmDistComprimento", "Composicao"))
        item = self.TWComprimentos.horizontalHeaderItem(0)
        item.setText(_translate("frmDistComprimento", "Class do Comprimento"))
        item = self.TWComprimentos.horizontalHeaderItem(1)
        item.setText(_translate("frmDistComprimento", "Nº de indivíduos"))

import icons_rc
