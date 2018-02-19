# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_Relatorio_SaidasPorProvincia.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(355, 270)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.LENome = QtWidgets.QLineEdit(Form)
        self.LENome.setObjectName("LENome")
        self.gridLayout_2.addWidget(self.LENome, 2, 1, 1, 1)
        self.PTEDescricao = QtWidgets.QPlainTextEdit(Form)
        self.PTEDescricao.setObjectName("PTEDescricao")
        self.gridLayout_2.addWidget(self.PTEDescricao, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBGerar = QtWidgets.QPushButton(Form)
        self.PBGerar.setObjectName("PBGerar")
        self.gridLayout.addWidget(self.PBGerar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(Form)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 2)
        self.LEFormato = QtWidgets.QLineEdit(Form)
        self.LEFormato.setObjectName("LEFormato")
        self.gridLayout_2.addWidget(self.LEFormato, 0, 1, 1, 1)
        self.CBProvincia = QtWidgets.QComboBox(Form)
        self.CBProvincia.setObjectName("CBProvincia")
        self.gridLayout_2.addWidget(self.CBProvincia, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Saidas Por Provincia"))
        self.label_3.setText(_translate("Form", "Descricao:"))
        self.label_2.setText(_translate("Form", "Nome:"))
        self.label.setText(_translate("Form", "Formato:"))
        self.PBGerar.setText(_translate("Form", "Gerar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))
        self.label_4.setText(_translate("Form", "Provincia:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

