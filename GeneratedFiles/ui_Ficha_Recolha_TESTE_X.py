# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_Ficha_Recolha_TESTE_X.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1187, 663)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Main{background-image: url(:/newPrefix/Background/918640-white-wallpaper.jpg);}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.PBCancelar = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/003-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBCancelar.setIcon(icon1)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 1, 3, 1, 1)
        self.PBGuardar = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/002-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBGuardar.setIcon(icon2)
        self.PBGuardar.setObjectName("PBGuardar")
        self.gridLayout.addWidget(self.PBGuardar, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Tab_Saidas = QtWidgets.QWidget()
        self.Tab_Saidas.setObjectName("Tab_Saidas")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Tab_Saidas)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.splitter_3 = QtWidgets.QSplitter(self.Tab_Saidas)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.GBSaida = QtWidgets.QGroupBox(self.splitter_3)
        self.GBSaida.setTitle("")
        self.GBSaida.setObjectName("GBSaida")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.GBSaida)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TabSaidas_CBCentroPesca = QtWidgets.QComboBox(self.GBSaida)
        self.TabSaidas_CBCentroPesca.setObjectName("TabSaidas_CBCentroPesca")
        self.gridLayout_2.addWidget(self.TabSaidas_CBCentroPesca, 10, 0, 1, 2)
        self.TabSaidas_DEDataAmost = QtWidgets.QDateEdit(self.GBSaida)
        self.TabSaidas_DEDataAmost.setObjectName("TabSaidas_DEDataAmost")
        self.gridLayout_2.addWidget(self.TabSaidas_DEDataAmost, 12, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.GBSaida)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 13, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.GBSaida)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 13, 1, 1, 1)
        self.TabSaidas_TEInicioAmost = QtWidgets.QTimeEdit(self.GBSaida)
        self.TabSaidas_TEInicioAmost.setObjectName("TabSaidas_TEInicioAmost")
        self.gridLayout_2.addWidget(self.TabSaidas_TEInicioAmost, 14, 0, 1, 1)
        self.TabSaidas_TEFimAmost = QtWidgets.QTimeEdit(self.GBSaida)
        self.TabSaidas_TEFimAmost.setObjectName("TabSaidas_TEFimAmost")
        self.gridLayout_2.addWidget(self.TabSaidas_TEFimAmost, 14, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.GBSaida)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 15, 0, 1, 1)
        self.TabSaidas_CBRegistadores = QtWidgets.QComboBox(self.GBSaida)
        self.TabSaidas_CBRegistadores.setObjectName("TabSaidas_CBRegistadores")
        self.gridLayout_2.addWidget(self.TabSaidas_CBRegistadores, 16, 0, 1, 2)
        self.label_31 = QtWidgets.QLabel(self.GBSaida)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 17, 0, 1, 2)
        self.TabSaidas_CBDiaSemana = QtWidgets.QComboBox(self.GBSaida)
        self.TabSaidas_CBDiaSemana.setObjectName("TabSaidas_CBDiaSemana")
        self.gridLayout_2.addWidget(self.TabSaidas_CBDiaSemana, 18, 0, 1, 2)
        self.TabSaidas_CBProvincia = QtWidgets.QComboBox(self.GBSaida)
        self.TabSaidas_CBProvincia.setObjectName("TabSaidas_CBProvincia")
        self.gridLayout_2.addWidget(self.TabSaidas_CBProvincia, 4, 0, 1, 2)
        self.TabSaidas_CBDistrito = QtWidgets.QComboBox(self.GBSaida)
        self.TabSaidas_CBDistrito.setObjectName("TabSaidas_CBDistrito")
        self.gridLayout_2.addWidget(self.TabSaidas_CBDistrito, 6, 0, 1, 2)
        self.TabSaidas_CBMunicipio = QtWidgets.QComboBox(self.GBSaida)
        self.TabSaidas_CBMunicipio.setObjectName("TabSaidas_CBMunicipio")
        self.gridLayout_2.addWidget(self.TabSaidas_CBMunicipio, 8, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.GBSaida)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 9, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.GBSaida)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 2)
        self.LEN_Sequencial = QtWidgets.QLineEdit(self.GBSaida)
        self.LEN_Sequencial.setEnabled(False)
        self.LEN_Sequencial.setObjectName("LEN_Sequencial")
        self.gridLayout_2.addWidget(self.LEN_Sequencial, 2, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.GBSaida)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.GBSaida)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.GBSaida)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.GBSaida)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 11, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.GBSaida)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 2)
        self.TabSaidas_CBDistrito.raise_()
        self.TabSaidas_CBCentroPesca.raise_()
        self.TabSaidas_DEDataAmost.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.TabSaidas_TEInicioAmost.raise_()
        self.TabSaidas_TEFimAmost.raise_()
        self.label_8.raise_()
        self.TabSaidas_CBRegistadores.raise_()
        self.label_31.raise_()
        self.TabSaidas_CBDiaSemana.raise_()
        self.TabSaidas_CBProvincia.raise_()
        self.TabSaidas_CBMunicipio.raise_()
        self.label.raise_()
        self.label_12.raise_()
        self.LEN_Sequencial.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.GBDadosHidro = QtWidgets.QGroupBox(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GBDadosHidro.sizePolicy().hasHeightForWidth())
        self.GBDadosHidro.setSizePolicy(sizePolicy)
        self.GBDadosHidro.setTitle("")
        self.GBDadosHidro.setObjectName("GBDadosHidro")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.GBDadosHidro)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_10 = QtWidgets.QLabel(self.GBDadosHidro)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_12.addWidget(self.label_10, 0, 0, 1, 2)
        self.label_35 = QtWidgets.QLabel(self.GBDadosHidro)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_12.addWidget(self.label_35, 3, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.GBDadosHidro)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_12.addWidget(self.label_11, 1, 0, 1, 2)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_28 = QtWidgets.QLabel(self.GBDadosHidro)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_10.addWidget(self.label_28, 0, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.GBDadosHidro)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_10.addWidget(self.label_30, 1, 0, 1, 1)
        self.TabSaidas_DSBPreaiaMar = QtWidgets.QDoubleSpinBox(self.GBDadosHidro)
        self.TabSaidas_DSBPreaiaMar.setObjectName("TabSaidas_DSBPreaiaMar")
        self.gridLayout_10.addWidget(self.TabSaidas_DSBPreaiaMar, 1, 1, 1, 1)
        self.TabSaidas_TEPreiamarHora = QtWidgets.QTimeEdit(self.GBDadosHidro)
        self.TabSaidas_TEPreiamarHora.setObjectName("TabSaidas_TEPreiamarHora")
        self.gridLayout_10.addWidget(self.TabSaidas_TEPreiamarHora, 1, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.GBDadosHidro)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_10.addWidget(self.label_29, 2, 0, 1, 1)
        self.TabSaidas_DSBBaixaMar = QtWidgets.QDoubleSpinBox(self.GBDadosHidro)
        self.TabSaidas_DSBBaixaMar.setObjectName("TabSaidas_DSBBaixaMar")
        self.gridLayout_10.addWidget(self.TabSaidas_DSBBaixaMar, 2, 1, 1, 1)
        self.TabSaidas_TEBaixamarHora = QtWidgets.QTimeEdit(self.GBDadosHidro)
        self.TabSaidas_TEBaixamarHora.setObjectName("TabSaidas_TEBaixamarHora")
        self.gridLayout_10.addWidget(self.TabSaidas_TEBaixamarHora, 2, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.GBDadosHidro)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_10.addWidget(self.label_32, 0, 0, 1, 2)
        self.gridLayout_12.addLayout(self.gridLayout_10, 5, 0, 1, 2)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_33 = QtWidgets.QLabel(self.GBDadosHidro)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_7.addWidget(self.label_33, 0, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.GBDadosHidro)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_7.addWidget(self.label_34, 0, 1, 1, 1)
        self.TabSaidas_CBTipoMare = QtWidgets.QComboBox(self.GBDadosHidro)
        self.TabSaidas_CBTipoMare.setObjectName("TabSaidas_CBTipoMare")
        self.gridLayout_7.addWidget(self.TabSaidas_CBTipoMare, 1, 0, 1, 1)
        self.TabSaidas_CBNivelMare = QtWidgets.QComboBox(self.GBDadosHidro)
        self.TabSaidas_CBNivelMare.setObjectName("TabSaidas_CBNivelMare")
        self.gridLayout_7.addWidget(self.TabSaidas_CBNivelMare, 1, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_7, 4, 0, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.GBDadosHidro)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 3, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.GBDadosHidro)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 0, 2, 1, 2)
        self.TabSaidas_CBForca = QtWidgets.QComboBox(self.GBDadosHidro)
        self.TabSaidas_CBForca.setObjectName("TabSaidas_CBForca")
        self.gridLayout_3.addWidget(self.TabSaidas_CBForca, 1, 0, 1, 2)
        self.TabSaidas_TEHoraVent = QtWidgets.QTimeEdit(self.GBDadosHidro)
        self.TabSaidas_TEHoraVent.setObjectName("TabSaidas_TEHoraVent")
        self.gridLayout_3.addWidget(self.TabSaidas_TEHoraVent, 3, 3, 1, 1)
        self.TabSaidas_CBDireccao = QtWidgets.QComboBox(self.GBDadosHidro)
        self.TabSaidas_CBDireccao.setObjectName("TabSaidas_CBDireccao")
        self.gridLayout_3.addWidget(self.TabSaidas_CBDireccao, 1, 2, 1, 2)
        self.label_25 = QtWidgets.QLabel(self.GBDadosHidro)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_3, 2, 0, 1, 2)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_38 = QtWidgets.QLabel(self.GBDadosHidro)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_11.addWidget(self.label_38, 0, 1, 1, 1)
        self.TabSaidas_CBNebulosidade = QtWidgets.QComboBox(self.GBDadosHidro)
        self.TabSaidas_CBNebulosidade.setObjectName("TabSaidas_CBNebulosidade")
        self.gridLayout_11.addWidget(self.TabSaidas_CBNebulosidade, 1, 1, 1, 1)
        self.TabSaidas_TENebulosidadeHora = QtWidgets.QTimeEdit(self.GBDadosHidro)
        self.TabSaidas_TENebulosidadeHora.setObjectName("TabSaidas_TENebulosidadeHora")
        self.gridLayout_11.addWidget(self.TabSaidas_TENebulosidadeHora, 2, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.GBDadosHidro)
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_11.addWidget(self.label_37, 2, 2, 1, 1)
        self.TabSaidas_CBFaselua = QtWidgets.QComboBox(self.GBDadosHidro)
        self.TabSaidas_CBFaselua.setObjectName("TabSaidas_CBFaselua")
        self.gridLayout_11.addWidget(self.TabSaidas_CBFaselua, 1, 2, 1, 2)
        self.label_36 = QtWidgets.QLabel(self.GBDadosHidro)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_11.addWidget(self.label_36, 0, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem2, 2, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 6, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_49 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout_6.addWidget(self.label_49, 0, 0, 1, 1)
        self.TabSaidas_PTEObservacao = QtWidgets.QPlainTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.TabSaidas_PTEObservacao.setFont(font)
        self.TabSaidas_PTEObservacao.setObjectName("TabSaidas_PTEObservacao")
        self.gridLayout_6.addWidget(self.TabSaidas_PTEObservacao, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.splitter_3)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_43 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_5.addWidget(self.label_43, 0, 0, 1, 2)
        self.GBActiPesqueira = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.GBActiPesqueira.setFont(font)
        self.GBActiPesqueira.setCheckable(True)
        self.GBActiPesqueira.setObjectName("GBActiPesqueira")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.GBActiPesqueira)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.TabSaidas_SBAmostras = QtWidgets.QSpinBox(self.GBActiPesqueira)
        self.TabSaidas_SBAmostras.setObjectName("TabSaidas_SBAmostras")
        self.gridLayout_13.addWidget(self.TabSaidas_SBAmostras, 3, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.GBActiPesqueira)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_13.addWidget(self.label_39, 3, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.GBActiPesqueira)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_13.addWidget(self.label_42, 6, 0, 1, 1)
        self.TabSaidas_SBActivas = QtWidgets.QSpinBox(self.GBActiPesqueira)
        self.TabSaidas_SBActivas.setObjectName("TabSaidas_SBActivas")
        self.gridLayout_13.addWidget(self.TabSaidas_SBActivas, 1, 1, 1, 1)
        self.TabSaidas_SBOutrosCentros = QtWidgets.QSpinBox(self.GBActiPesqueira)
        self.TabSaidas_SBOutrosCentros.setObjectName("TabSaidas_SBOutrosCentros")
        self.gridLayout_13.addWidget(self.TabSaidas_SBOutrosCentros, 6, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.GBActiPesqueira)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_13.addWidget(self.label_40, 1, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.GBActiPesqueira)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_13.addWidget(self.label_41, 2, 0, 1, 1)
        self.TabSaidas_SBNaoActivas = QtWidgets.QSpinBox(self.GBActiPesqueira)
        self.TabSaidas_SBNaoActivas.setObjectName("TabSaidas_SBNaoActivas")
        self.gridLayout_13.addWidget(self.TabSaidas_SBNaoActivas, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.GBActiPesqueira, 1, 0, 1, 1)
        self.GBArtes = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GBArtes.sizePolicy().hasHeightForWidth())
        self.GBArtes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GBArtes.setFont(font)
        self.GBArtes.setAlignment(QtCore.Qt.AlignCenter)
        self.GBArtes.setFlat(True)
        self.GBArtes.setObjectName("GBArtes")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.GBArtes)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.PBArtes = QtWidgets.QPushButton(self.GBArtes)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBArtes.setIcon(icon3)
        self.PBArtes.setObjectName("PBArtes")
        self.gridLayout_14.addWidget(self.PBArtes, 1, 0, 1, 1)
        self.TabSaidas_TVArtesAmost = QtWidgets.QTableView(self.GBArtes)
        self.TabSaidas_TVArtesAmost.setObjectName("TabSaidas_TVArtesAmost")
        self.gridLayout_14.addWidget(self.TabSaidas_TVArtesAmost, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.GBArtes, 3, 0, 1, 2)
        self.GBSaidasObs = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.GBSaidasObs.setFont(font)
        self.GBSaidasObs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GBSaidasObs.setFlat(False)
        self.GBSaidasObs.setCheckable(False)
        self.GBSaidasObs.setChecked(False)
        self.GBSaidasObs.setObjectName("GBSaidasObs")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.GBSaidasObs)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.TabSaidas_TVSaidasObservacoes = QtWidgets.QTableView(self.GBSaidasObs)
        self.TabSaidas_TVSaidasObservacoes.setObjectName("TabSaidas_TVSaidasObservacoes")
        self.gridLayout_16.addWidget(self.TabSaidas_TVSaidasObservacoes, 1, 0, 1, 1)
        self.PBSaidasObs = QtWidgets.QPushButton(self.GBSaidasObs)
        self.PBSaidasObs.setIcon(icon3)
        self.PBSaidasObs.setObjectName("PBSaidasObs")
        self.gridLayout_16.addWidget(self.PBSaidasObs, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.GBSaidasObs, 1, 1, 1, 1)
        self.gridLayout_8.addWidget(self.splitter_3, 0, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/006-wall-calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Tab_Saidas, icon4, "")
        self.tab_Amostras = QtWidgets.QWidget()
        self.tab_Amostras.setObjectName("tab_Amostras")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_Amostras)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.GLAmostras = QtWidgets.QGridLayout()
        self.GLAmostras.setObjectName("GLAmostras")
        self.gridLayout_15.addLayout(self.GLAmostras, 0, 0, 1, 1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Amostras, icon5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 4)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ficha de Recolha"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))
        self.PBGuardar.setText(_translate("Form", "Guardar"))
        self.label_2.setText(_translate("Form", "Inicio"))
        self.label_3.setText(_translate("Form", "Fim"))
        self.label_8.setText(_translate("Form", "Registador"))
        self.label_31.setText(_translate("Form", "Dia da Semana"))
        self.label.setText(_translate("Form", "Centro de Pesca"))
        self.label_12.setText(_translate("Form", "Numero Sequencial"))
        self.label_6.setText(_translate("Form", "Provincia"))
        self.label_5.setText(_translate("Form", "Distrito"))
        self.label_4.setText(_translate("Form", "Municipio"))
        self.label_7.setText(_translate("Form", "Data"))
        self.label_9.setText(_translate("Form", "Saidas"))
        self.label_10.setText(_translate("Form", "Dados Hidrometeorologicos"))
        self.label_35.setText(_translate("Form", "MARE"))
        self.label_11.setText(_translate("Form", "VENTO"))
        self.label_28.setText(_translate("Form", "Hora"))
        self.label_30.setText(_translate("Form", "Preia-mar "))
        self.label_29.setText(_translate("Form", "Baixa-mar "))
        self.label_32.setText(_translate("Form", "Altura"))
        self.label_33.setText(_translate("Form", "Tipo"))
        self.label_34.setText(_translate("Form", "Nivel"))
        self.label_13.setText(_translate("Form", "Hora:       "))
        self.label_26.setText(_translate("Form", "Direccao"))
        self.label_25.setText(_translate("Form", "Forca"))
        self.label_38.setText(_translate("Form", "NEBULOSIDADE"))
        self.label_37.setText(_translate("Form", "Hora:        "))
        self.label_36.setText(_translate("Form", "FASE DA LUA"))
        self.label_49.setText(_translate("Form", "Observacao"))
        self.label_43.setText(_translate("Form", "Actividade Pesqueira"))
        self.GBActiPesqueira.setTitle(_translate("Form", "Houve activdades pesqueiras?"))
        self.label_39.setText(_translate("Form", "Amostradas"))
        self.label_42.setText(_translate("Form", "Outros Centros"))
        self.label_40.setText(_translate("Form", "Activas"))
        self.label_41.setText(_translate("Form", "Nao Activas"))
        self.GBArtes.setTitle(_translate("Form", "Artes"))
        self.PBArtes.setText(_translate("Form", "Adicionar Artes"))
        self.GBSaidasObs.setTitle(_translate("Form", "Saidas Observacoes"))
        self.PBSaidasObs.setText(_translate("Form", "Adiconar Observacoes as Saidas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Saidas), _translate("Form", "1 - Saidas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Amostras), _translate("Form", "2 - Amostras"))

import icons_rc
import images_rc
