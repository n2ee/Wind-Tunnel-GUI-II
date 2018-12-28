# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCalibrate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogCalibrate(object):
    def setupUi(self, DialogCalibrate):
        DialogCalibrate.setObjectName("DialogCalibrate")
        DialogCalibrate.resize(414, 114)
        self.lblRawAirspeed = QtWidgets.QLabel(DialogCalibrate)
        self.lblRawAirspeed.setGeometry(QtCore.QRect(10, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblRawAirspeed.setFont(font)
        self.lblRawAirspeed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblRawAirspeed.setObjectName("lblRawAirspeed")
        self.txtRawAirspeed = QtWidgets.QLabel(DialogCalibrate)
        self.txtRawAirspeed.setGeometry(QtCore.QRect(150, 20, 56, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtRawAirspeed.setFont(font)
        self.txtRawAirspeed.setObjectName("txtRawAirspeed")
        self.btnAirspeedTare = QtWidgets.QPushButton(DialogCalibrate)
        self.btnAirspeedTare.setGeometry(QtCore.QRect(30, 50, 161, 32))
        self.btnAirspeedTare.setObjectName("btnAirspeedTare")
        self.btnDone = QtWidgets.QPushButton(DialogCalibrate)
        self.btnDone.setGeometry(QtCore.QRect(280, 50, 110, 32))
        self.btnDone.setDefault(True)
        self.btnDone.setObjectName("btnDone")

        self.retranslateUi(DialogCalibrate)
        self.btnDone.clicked.connect(DialogCalibrate.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogCalibrate)

    def retranslateUi(self, DialogCalibrate):
        _translate = QtCore.QCoreApplication.translate
        DialogCalibrate.setWindowTitle(_translate("DialogCalibrate", "Dialog"))
        self.lblRawAirspeed.setText(_translate("DialogCalibrate", "Raw Airspeed:"))
        self.txtRawAirspeed.setText(_translate("DialogCalibrate", "N/A"))
        self.btnAirspeedTare.setText(_translate("DialogCalibrate", "Set Airspeed Tare"))
        self.btnDone.setText(_translate("DialogCalibrate", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogCalibrate = QtWidgets.QDialog()
    ui = Ui_DialogCalibrate()
    ui.setupUi(DialogCalibrate)
    DialogCalibrate.show()
    sys.exit(app.exec_())

