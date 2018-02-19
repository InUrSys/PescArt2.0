# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_GenerateReports.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(506, 412)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 2, 3)
        self.PBUp = QtWidgets.QPushButton(Form)
        self.PBUp.setObjectName("PBUp")
        self.gridLayout_2.addWidget(self.PBUp, 3, 4, 1, 2)
        self.LECod = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LECod.sizePolicy().hasHeightForWidth())
        self.LECod.setSizePolicy(sizePolicy)
        self.LECod.setObjectName("LECod")
        self.gridLayout_2.addWidget(self.LECod, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.TVReports = QtWidgets.QTableView(Form)
        self.TVReports.setObjectName("TVReports")
        self.gridLayout_2.addWidget(self.TVReports, 5, 0, 1, 6)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.PTEDescricao = QtWidgets.QPlainTextEdit(Form)
        self.PTEDescricao.setObjectName("PTEDescricao")
        self.gridLayout_2.addWidget(self.PTEDescricao, 2, 1, 1, 5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PBGerar = QtWidgets.QPushButton(Form)
        self.PBGerar.setObjectName("PBGerar")
        self.gridLayout.addWidget(self.PBGerar, 0, 0, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCancelar.sizePolicy().hasHeightForWidth())
        self.PBCancelar.setSizePolicy(sizePolicy)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 6, 0, 1, 6)
        self.LENome = QtWidgets.QLineEdit(Form)
        self.LENome.setObjectName("LENome")
        self.gridLayout_2.addWidget(self.LENome, 1, 1, 1, 5)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.PBDown = QtWidgets.QPushButton(Form)
        self.PBDown.setObjectName("PBDown")
        self.gridLayout_2.addWidget(self.PBDown, 4, 4, 1, 2)
        self.CBFormato = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CBFormato.sizePolicy().hasHeightForWidth())
        self.CBFormato.setSizePolicy(sizePolicy)
        self.CBFormato.setObjectName("CBFormato")
        self.gridLayout_2.addWidget(self.CBFormato, 0, 3, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Processamento de Relatorios"))
        self.label_4.setText(_translate("Form", "Lista dos Templates de Relatorio Existentes"))
        self.PBUp.setText(_translate("Form", "Up"))
        self.label_3.setText(_translate("Form", "Descricao:"))
        self.label_5.setText(_translate("Form", "Formato:"))
        self.PBGerar.setText(_translate("Form", "Gerar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))
        self.label_2.setText(_translate("Form", "Nome:"))
        self.label.setText(_translate("Form", "Cod.:"))
        self.PBDown.setText(_translate("Form", "Down"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

