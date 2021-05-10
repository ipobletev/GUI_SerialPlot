# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HMI_SerialPlot.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../SME-trans.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 30, 211, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../SME-trans.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(50, 140, 761, 291))
        self.graphicsView.setObjectName("graphicsView")
        self.comboBox_comserial = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_comserial.setGeometry(QtCore.QRect(60, 80, 211, 22))
        self.comboBox_comserial.setObjectName("comboBox_comserial")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.BT_Connect = QtWidgets.QPushButton(self.centralwidget)
        self.BT_Connect.setGeometry(QtCore.QRect(60, 110, 101, 23))
        self.BT_Connect.setObjectName("BT_Connect")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(130, 450, 81, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 450, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 480, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 480, 81, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 450, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 450, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(320, 480, 91, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.BT_Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.BT_Refresh.setGeometry(QtCore.QRect(190, 20, 81, 23))
        self.BT_Refresh.setObjectName("BT_Refresh")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(760, 440, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 440, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_baud = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_baud.setGeometry(QtCore.QRect(100, 50, 81, 22))
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 50, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.BT_clear = QtWidgets.QPushButton(self.centralwidget)
        self.BT_clear.setGeometry(QtCore.QRect(600, 110, 211, 23))
        self.BT_clear.setObjectName("BT_clear")
        self.BT_Disconnect = QtWidgets.QPushButton(self.centralwidget)
        self.BT_Disconnect.setGeometry(QtCore.QRect(170, 110, 101, 23))
        self.BT_Disconnect.setObjectName("BT_Disconnect")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "SERIAL COM"))
        self.BT_Connect.setText(_translate("MainWindow", "Connect"))
        self.label_3.setText(_translate("MainWindow", "Limit +Y"))
        self.label_4.setText(_translate("MainWindow", "Limit  -Y"))
        self.label_5.setText(_translate("MainWindow", "Range X"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "AutoAdjustX"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Static"))
        self.BT_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_6.setText(_translate("MainWindow", "Data:"))
        self.comboBox_baud.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_baud.setItemText(1, _translate("MainWindow", "115200"))
        self.label_7.setText(_translate("MainWindow", "Bauds:"))
        self.BT_clear.setText(_translate("MainWindow", "Clear Data"))
        self.BT_Disconnect.setText(_translate("MainWindow", "Disconnect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
