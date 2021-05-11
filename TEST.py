import sys
import os
from HMI_SerialPlot import *
from PySide2.QtCore import QTimer
from SME_SerialCom import SME_Serial_Communication
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
#https://www.mfitzp.com/tutorials/plotting-pyqtgraph/
from random import randint
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

        # Set up GUI configuration

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points
        #Add Background colour to white
        self.ui.graphicsView.setBackground('w')
        # Add Title
        self.ui.graphicsView.setTitle("Your Title Here", color="b", size="15pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.ui.graphicsView.setLabel("left", "Voltage [V]", **styles)
        #self.ui.graphicsView.setLabel("bottom", "TIME", **styles)
        #Add legend
        self.ui.graphicsView.addLegend()
        #Add grid
        self.ui.graphicsView.showGrid(x=True, y=True)
        #Set Range
        self.ui.graphicsView.setXRange(0, 100, padding=0)
        self.ui.graphicsView.setYRange(0, 5, padding=0)
        #Set legend plot
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.ui.graphicsView.plot(self.x, self.y, pen=pen)
        self.ui.graphicsView.clear()
        self.ui.graphicsView.resize(500,200)

    def data_serial(self,data):
        self.data_1 = float(data)

        #Update Text data
        self.ui.lineEdit.setText(str(self.data_1))

        #Update Graph Plot
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append( self.data_1)  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

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