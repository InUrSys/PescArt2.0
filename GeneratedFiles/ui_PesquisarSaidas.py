# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_PesquisarSaidas.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1041, 550)
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.TVSaidas = QtWidgets.QTableView(Form)
        self.TVSaidas.setObjectName("TVSaidas")
        self.gridLayout_5.addWidget(self.TVSaidas, 0, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.CBProvincia = QtWidgets.QComboBox(self.groupBox)
        self.CBProvincia.setEnabled(True)
        self.CBProvincia.setObjectName("CBProvincia")
        self.gridLayout.addWidget(self.CBProvincia, 0, 1, 1, 1)
        self.CBPosto = QtWidgets.QComboBox(self.groupBox)
        self.CBPosto.setEnabled(True)
        self.CBPosto.setObjectName("CBPosto")
        self.gridLayout.addWidget(self.CBPosto, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.CBDistrito = QtWidgets.QComboBox(self.groupBox)
        self.CBDistrito.setEnabled(True)
        self.CBDistrito.setObjectName("CBDistrito")
        self.gridLayout.addWidget(self.CBDistrito, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.CBCentroPesca = QtWidgets.QComboBox(self.groupBox)
        self.CBCentroPesca.setEnabled(True)
        self.CBCentroPesca.setObjectName("CBCentroPesca")
        self.gridLayout.addWidget(self.CBCentroPesca, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 2, 1)
        self.GBData = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GBData.sizePolicy().hasHeightForWidth())
        self.GBData.setSizePolicy(sizePolicy)
        self.GBData.setCheckable(True)
        self.GBData.setObjectName("GBData")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.GBData)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.GBData)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.GBData)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.DEInicio = QtWidgets.QDateTimeEdit(self.GBData)
        self.DEInicio.setObjectName("DEInicio")
        self.gridLayout_2.addWidget(self.DEInicio, 0, 1, 1, 1)
        self.DEFim = QtWidgets.QDateTimeEdit(self.GBData)
        self.DEFim.setObjectName("DEFim")
        self.gridLayout_2.addWidget(self.DEFim, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.GBData, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.CBDiaSemana = QtWidgets.QComboBox(self.groupBox_3)
        self.CBDiaSemana.setObjectName("CBDiaSemana")
        self.gridLayout_3.addWidget(self.CBDiaSemana, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.CBRegistador = QtWidgets.QComboBox(self.groupBox_3)
        self.CBRegistador.setObjectName("CBRegistador")
        self.gridLayout_3.addWidget(self.CBRegistador, 0, 1, 1, 1)
        self.CBActividadePesqueria = QtWidgets.QComboBox(self.groupBox_3)
        self.CBActividadePesqueria.setObjectName("CBActividadePesqueria")
        self.gridLayout_3.addWidget(self.CBActividadePesqueria, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 1, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PBOK = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBOK.setIcon(icon)
        self.PBOK.setObjectName("PBOK")
        self.gridLayout_4.addWidget(self.PBOK, 0, 2, 1, 1)
        self.PBPesquisar = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/001-search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBPesquisar.setIcon(icon1)
        self.PBPesquisar.setIconSize(QtCore.QSize(20, 20))
        self.PBPesquisar.setObjectName("PBPesquisar")
        self.gridLayout_4.addWidget(self.PBPesquisar, 0, 3, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon2)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout_4.addWidget(self.PBCancelar, 0, 1, 1, 1)
        self.PBOptions = QtWidgets.QPushButton(Form)
        self.PBOptions.setObjectName("PBOptions")
        self.gridLayout_4.addWidget(self.PBOptions, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pesquisa das Saidas"))
        self.groupBox.setTitle(_translate("Form", "Local"))
        self.label_9.setText(_translate("Form", "Provincia:"))
        self.label_4.setText(_translate("Form", "Posto Administrativo:"))
        self.label_10.setText(_translate("Form", "Distrito:"))
        self.label_3.setText(_translate("Form", "Centro de Pesca:"))
        self.GBData.setTitle(_translate("Form", "Data"))
        self.label.setText(_translate("Form", "Inicio:"))
        self.label_2.setText(_translate("Form", "Fim:"))
        self.DEInicio.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.DEFim.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.groupBox_3.setTitle(_translate("Form", "Outras Opcoes"))
        self.label_6.setText(_translate("Form", "Dia da Semana:"))
        self.label_5.setText(_translate("Form", "Registador:"))
        self.label_7.setText(_translate("Form", "Actividade Pesqueira:"))
        self.PBOK.setText(_translate("Form", "Ok!"))
        self.PBPesquisar.setText(_translate("Form", "Pesquisar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))
        self.PBOptions.setText(_translate("Form", "..."))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

