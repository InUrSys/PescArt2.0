# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_Ficha_Recolha_Part_III.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(1012, 601)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 150, 341, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.GLEspecies = QtWidgets.QGridLayout(self.layoutWidget)
        self.GLEspecies.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.GLEspecies.setContentsMargins(0, 0, 0, 0)
        self.GLEspecies.setObjectName("GLEspecies")
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(360, 150, 441, 201))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.GLAmostEspe = QtWidgets.QGridLayout(self.layoutWidget1)
        self.GLAmostEspe.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.GLAmostEspe.setContentsMargins(0, 0, 0, 0)
        self.GLAmostEspe.setObjectName("GLAmostEspe")
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 370, 341, 191))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.GLSexo = QtWidgets.QGridLayout(self.layoutWidget2)
        self.GLSexo.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.GLSexo.setContentsMargins(0, 0, 0, 0)
        self.GLSexo.setObjectName("GLSexo")
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(810, 150, 191, 411))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.GLComprimentos = QtWidgets.QGridLayout(self.layoutWidget3)
        self.GLComprimentos.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.GLComprimentos.setContentsMargins(0, 0, 0, 0)
        self.GLComprimentos.setObjectName("GLComprimentos")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(360, 370, 441, 191))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.GLAmostSexo = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.GLAmostSexo.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.GLAmostSexo.setContentsMargins(0, 0, 0, 0)
        self.GLAmostSexo.setObjectName("GLAmostSexo")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(8, 3, 999, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(7, 560, 1001, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(998, 11, 16, 557))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(0, 10, 16, 557))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.layoutWidget_3 = QtWidgets.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 20, 991, 121))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.GLKeppTrack = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.GLKeppTrack.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.GLKeppTrack.setContentsMargins(0, 0, 0, 0)
        self.GLKeppTrack.setObjectName("GLKeppTrack")
        self.LBwhois = QtWidgets.QLabel(Form)
        self.LBwhois.setGeometry(QtCore.QRect(6, 571, 1001, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LBwhois.setFont(font)
        self.LBwhois.setFrameShape(QtWidgets.QFrame.Box)
        self.LBwhois.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LBwhois.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LBwhois.setObjectName("LBwhois")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(8, 139, 998, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_9 = QtWidgets.QFrame(Form)
        self.line_9.setGeometry(QtCore.QRect(796, 146, 20, 421))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(7, 353, 799, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ficha de Recolha"))
        self.LBwhois.setText(_translate("Form", "UserName: Chernomirdin Da Costa Macuvele"))

import icons_rc
import images_rc
