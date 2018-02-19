# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/PescArt2.0/UserInt/ui_TreeViewMoz.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(529, 558)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.TViewMoz = QtWidgets.QTreeView(Form)
        self.TViewMoz.setObjectName("TViewMoz")
        self.gridLayout.addWidget(self.TViewMoz, 0, 0, 1, 2)
        self.PBFechar = QtWidgets.QPushButton(Form)
        self.PBFechar.setObjectName("PBFechar")
        self.gridLayout.addWidget(self.PBFechar, 1, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(416, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Estrura Hierarquia de Mocambique"))
        self.PBFechar.setText(_translate("Form", "Fechar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

