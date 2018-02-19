# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_artes_POT.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(363, 409)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.CBuniTrablho = QtWidgets.QComboBox(Dialog)
        self.CBuniTrablho.setObjectName("CBuniTrablho")
        self.gridLayout.addWidget(self.CBuniTrablho, 4, 3, 1, 2)
        self.CBUniEsforco = QtWidgets.QComboBox(Dialog)
        self.CBUniEsforco.setObjectName("CBUniEsforco")
        self.gridLayout.addWidget(self.CBUniEsforco, 5, 3, 1, 2)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 2)
        self.CBTipPesca = QtWidgets.QComboBox(Dialog)
        self.CBTipPesca.setObjectName("CBTipPesca")
        self.gridLayout.addWidget(self.CBTipPesca, 6, 3, 1, 2)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 1, 1, 1)
        self.CHBActivo = QtWidgets.QCheckBox(Dialog)
        self.CHBActivo.setObjectName("CHBActivo")
        self.gridLayout.addWidget(self.CHBActivo, 9, 3, 1, 2)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(Dialog)
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
        self.gridLayout.addWidget(self.splitter, 10, 1, 1, 4)
        self.LECodigo = QtWidgets.QLineEdit(Dialog)
        self.LECodigo.setMaxLength(3)
        self.LECodigo.setObjectName("LECodigo")
        self.gridLayout.addWidget(self.LECodigo, 1, 3, 1, 2)
        self.LENome = QtWidgets.QLineEdit(Dialog)
        self.LENome.setMaxLength(15)
        self.LENome.setClearButtonEnabled(False)
        self.LENome.setObjectName("LENome")
        self.gridLayout.addWidget(self.LENome, 3, 3, 1, 2)
        self.PTEDescricao = QtWidgets.QPlainTextEdit(Dialog)
        self.PTEDescricao.setObjectName("PTEDescricao")
        self.gridLayout.addWidget(self.PTEDescricao, 7, 3, 1, 2)
        self.PTEComentarios = QtWidgets.QPlainTextEdit(Dialog)
        self.PTEComentarios.setObjectName("PTEComentarios")
        self.gridLayout.addWidget(self.PTEComentarios, 8, 3, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Artes de Pesca"))
        self.label_6.setText(_translate("Dialog", "Unidade de Trabalho:"))
        self.label_8.setText(_translate("Dialog", "Nome:"))
        self.label_5.setText(_translate("Dialog", "Unidade de Esforco:"))
        self.label_7.setText(_translate("Dialog", "Tipo de Pesca:"))
        self.label_9.setText(_translate("Dialog", "Comentarios:"))
        self.CHBActivo.setText(_translate("Dialog", "Activo"))
        self.label_10.setText(_translate("Dialog", "Descricao:"))
        self.label.setText(_translate("Dialog", "Codigo:"))
        self.LECodigo.setPlaceholderText(_translate("Dialog", "Ex:ABC"))
        self.LENome.setPlaceholderText(_translate("Dialog", "Ex:Arasto"))
        self.PTEDescricao.setPlaceholderText(_translate("Dialog", "Ex:O que se faz..."))
        self.PTEComentarios.setPlaceholderText(_translate("Dialog", "Ex:Algo a mais..."))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

