import sys
from HMI_SerialPlot import *
from PySide2.QtCore import QTimer
from SME_SerialCom import SME_Serial_Communication
from PyQt5.QtWidgets import QApplication, QMainWindow

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyApp(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serial = SME_Serial_Communication()
        self.serial.ports_availables()
        self.data_1=0.0

        self.serial.data_receive.connect(self.data_serial)
        self.ui.ComboBox_Baud.addItems(self.serial.baudrates)
        self.ui.ComboBox_Baud.setCurrentText("9600")

        self.ui.BT_Refresh.clicked.connect(self.clickbutton_refresh)
        self.ui.BT_Connect.clicked.connect(self.clickbutton_connect)
        self.ui.BT_Disconnect.clicked.connect(self.clickbutton_disconnect)
        self.ui.BT_Clear.clicked.connect(self.clickbutton_cleardata)
    
    def data_serial(self,data):
        self.data_1 = float(data)

        #Update Text data
        self.ui.lineEdit.setText(str(self.data_1))

        #Update Graph Plot


    def clickbutton_connect(self):
        index = self.ui.ComboBox_PortSerial.currentIndex()
        port = self.serial.serial_ports[index]
        baud = self.ui.ComboBox_Baud.currentText()
        self.serial.serial_com.port = port
        self.serial.serial_com.baudrate = baud
        self.serial.serial_connection()
        print("Connect")

    def clickbutton_disconnect(self):

        self.serial.serial_disconnect()
        print("Disconnect")

    def clickbutton_refresh(self):

        self.serial.ports_availables()
        self.ui.ComboBox_PortSerial.clear()
        self.ui.ComboBox_PortSerial.addItems(self.serial.text_serial_ports)
        print("Refresh")

    def clickbutton_cleardata(self):
        self.ui.lineEdit.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())