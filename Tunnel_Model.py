# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tunnel_Model.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLoadTare = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadTare.setGeometry(QtCore.QRect(90, 320, 113, 32))
        self.btnLoadTare.setProperty("toolTipDuration", 4)
        self.btnLoadTare.setObjectName("btnLoadTare")
        self.inpRunName = QtWidgets.QLineEdit(self.centralwidget)
        self.inpRunName.setGeometry(QtCore.QRect(110, 20, 261, 21))
        self.inpRunName.setObjectName("inpRunName")
        self.btnSaveResults = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveResults.setGeometry(QtCore.QRect(280, 320, 113, 32))
        self.btnSaveResults.setObjectName("btnSaveResults")
        self.lblRunName = QtWidgets.QLabel(self.centralwidget)
        self.lblRunName.setGeometry(QtCore.QRect(30, 20, 71, 20))
        self.lblRunName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblRunName.setObjectName("lblRunName")
        self.lblConfiguration = QtWidgets.QLabel(self.centralwidget)
        self.lblConfiguration.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.lblConfiguration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblConfiguration.setObjectName("lblConfiguration")
        self.inpConfiguration = QtWidgets.QLineEdit(self.centralwidget)
        self.inpConfiguration.setGeometry(QtCore.QRect(110, 50, 261, 21))
        self.inpConfiguration.setObjectName("inpConfiguration")
        self.lblAirspeed = QtWidgets.QLabel(self.centralwidget)
        self.lblAirspeed.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.lblAirspeed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAirspeed.setObjectName("lblAirspeed")
        self.lblMPH = QtWidgets.QLabel(self.centralwidget)
        self.lblMPH.setGeometry(QtCore.QRect(140, 90, 31, 16))
        self.lblMPH.setObjectName("lblMPH")
        self.lblFtPerSec = QtWidgets.QLabel(self.centralwidget)
        self.lblFtPerSec.setGeometry(QtCore.QRect(140, 120, 41, 16))
        self.lblFtPerSec.setObjectName("lblFtPerSec")
        self.outSpeedMPH = QtWidgets.QLCDNumber(self.centralwidget)
        self.outSpeedMPH.setGeometry(QtCore.QRect(90, 80, 41, 31))
        self.outSpeedMPH.setDigitCount(3)
        self.outSpeedMPH.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.outSpeedMPH.setObjectName("outSpeedMPH")
        self.lblLift = QtWidgets.QLabel(self.centralwidget)
        self.lblLift.setGeometry(QtCore.QRect(50, 220, 31, 16))
        self.lblLift.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLift.setObjectName("lblLift")
        self.lblDrag = QtWidgets.QLabel(self.centralwidget)
        self.lblDrag.setGeometry(QtCore.QRect(40, 250, 41, 16))
        self.lblDrag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDrag.setObjectName("lblDrag")
        self.lblMoment = QtWidgets.QLabel(self.centralwidget)
        self.lblMoment.setGeometry(QtCore.QRect(20, 280, 61, 16))
        self.lblMoment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblMoment.setObjectName("lblMoment")
        self.tblLiftDragMoment = QtWidgets.QTableWidget(self.centralwidget)
        self.tblLiftDragMoment.setGeometry(QtCore.QRect(90, 210, 311, 101))
        self.tblLiftDragMoment.setWordWrap(False)
        self.tblLiftDragMoment.setRowCount(3)
        self.tblLiftDragMoment.setColumnCount(3)
        self.tblLiftDragMoment.setObjectName("tblLiftDragMoment")
        self.tblLiftDragMoment.horizontalHeader().setVisible(False)
        self.tblLiftDragMoment.verticalHeader().setVisible(False)
        self.lblKg = QtWidgets.QLabel(self.centralwidget)
        self.lblKg.setGeometry(QtCore.QRect(110, 190, 61, 16))
        self.lblKg.setAlignment(QtCore.Qt.AlignCenter)
        self.lblKg.setObjectName("lblKg")
        self.lblLb = QtWidgets.QLabel(self.centralwidget)
        self.lblLb.setGeometry(QtCore.QRect(210, 190, 61, 16))
        self.lblLb.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLb.setObjectName("lblLb")
        self.lblKgStd = QtWidgets.QLabel(self.centralwidget)
        self.lblKgStd.setGeometry(QtCore.QRect(310, 190, 61, 16))
        self.lblKgStd.setAlignment(QtCore.Qt.AlignCenter)
        self.lblKgStd.setObjectName("lblKgStd")
        self.lblSampleRate = QtWidgets.QLabel(self.centralwidget)
        self.lblSampleRate.setGeometry(QtCore.QRect(390, 30, 81, 20))
        self.lblSampleRate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSampleRate.setObjectName("lblSampleRate")
        self.outSpeedFps = QtWidgets.QLCDNumber(self.centralwidget)
        self.outSpeedFps.setGeometry(QtCore.QRect(70, 120, 61, 31))
        self.outSpeedFps.setDigitCount(5)
        self.outSpeedFps.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.outSpeedFps.setObjectName("outSpeedFps")
        self.outSampleRate = QtWidgets.QLCDNumber(self.centralwidget)
        self.outSampleRate.setGeometry(QtCore.QRect(480, 20, 41, 31))
        self.outSampleRate.setDigitCount(3)
        self.outSampleRate.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.outSampleRate.setObjectName("outSampleRate")
        self.lblAoA = QtWidgets.QLabel(self.centralwidget)
        self.lblAoA.setGeometry(QtCore.QRect(190, 90, 41, 20))
        self.lblAoA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAoA.setObjectName("lblAoA")
        self.outAoaDeg = QtWidgets.QLCDNumber(self.centralwidget)
        self.outAoaDeg.setGeometry(QtCore.QRect(240, 80, 41, 31))
        self.outAoaDeg.setDigitCount(3)
        self.outAoaDeg.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.outAoaDeg.setObjectName("outAoaDeg")
        self.lblDeg = QtWidgets.QLabel(self.centralwidget)
        self.lblDeg.setGeometry(QtCore.QRect(290, 90, 31, 16))
        self.lblDeg.setObjectName("lblDeg")
        self.lblPower = QtWidgets.QLabel(self.centralwidget)
        self.lblPower.setGeometry(QtCore.QRect(350, 90, 41, 20))
        self.lblPower.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPower.setObjectName("lblPower")
        self.outPower = QtWidgets.QLCDNumber(self.centralwidget)
        self.outPower.setGeometry(QtCore.QRect(400, 80, 71, 31))
        self.outPower.setDigitCount(6)
        self.outPower.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.outPower.setObjectName("outPower")
        self.lblWatts = QtWidgets.QLabel(self.centralwidget)
        self.lblWatts.setGeometry(QtCore.QRect(480, 90, 31, 16))
        self.lblWatts.setObjectName("lblWatts")
        self.outAnemometerMPH = QtWidgets.QLCDNumber(self.centralwidget)
        self.outAnemometerMPH.setGeometry(QtCore.QRect(490, 150, 41, 31))
        self.outAnemometerMPH.setDigitCount(3)
        self.outAnemometerMPH.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.outAnemometerMPH.setObjectName("outAnemometerMPH")
        self.lblAnemometer = QtWidgets.QLabel(self.centralwidget)
        self.lblAnemometer.setGeometry(QtCore.QRect(390, 160, 91, 20))
        self.lblAnemometer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAnemometer.setObjectName("lblAnemometer")
        self.lblFtPerSec_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblFtPerSec_2.setGeometry(QtCore.QRect(540, 190, 41, 16))
        self.lblFtPerSec_2.setObjectName("lblFtPerSec_2")
        self.outAnemometerFps = QtWidgets.QLCDNumber(self.centralwidget)
        self.outAnemometerFps.setGeometry(QtCore.QRect(470, 190, 61, 31))
        self.outAnemometerFps.setDigitCount(5)
        self.outAnemometerFps.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.outAnemometerFps.setObjectName("outAnemometerFps")
        self.lblMPH_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblMPH_2.setGeometry(QtCore.QRect(540, 160, 31, 16))
        self.lblMPH_2.setObjectName("lblMPH_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLoadTare.setText(_translate("MainWindow", "Set Load Tare"))
        self.btnSaveResults.setText(_translate("MainWindow", "Save Results"))
        self.lblRunName.setText(_translate("MainWindow", "Run Name:"))
        self.lblConfiguration.setText(_translate("MainWindow", "Configuration:"))
        self.lblAirspeed.setText(_translate("MainWindow", "Airspeed:"))
        self.lblMPH.setText(_translate("MainWindow", "MPH"))
        self.lblFtPerSec.setText(_translate("MainWindow", "ft/sec"))
        self.lblLift.setText(_translate("MainWindow", "Lift:"))
        self.lblDrag.setText(_translate("MainWindow", "Drag:"))
        self.lblMoment.setText(_translate("MainWindow", "Moment:"))
        self.lblKg.setText(_translate("MainWindow", "Kg"))
        self.lblLb.setText(_translate("MainWindow", "lb"))
        self.lblKgStd.setText(_translate("MainWindow", "sd Kg"))
        self.lblSampleRate.setText(_translate("MainWindow", "Sample Rate:"))
        self.lblAoA.setText(_translate("MainWindow", "AoA:"))
        self.lblDeg.setText(_translate("MainWindow", "Deg"))
        self.lblPower.setText(_translate("MainWindow", "Power:"))
        self.lblWatts.setText(_translate("MainWindow", "W"))
        self.lblAnemometer.setText(_translate("MainWindow", "Anemometer:"))
        self.lblFtPerSec_2.setText(_translate("MainWindow", "ft/sec"))
        self.lblMPH_2.setText(_translate("MainWindow", "MPH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

