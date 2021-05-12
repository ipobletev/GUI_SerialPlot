################################################################################
## Proyect:
## Autor: Ismael Poblete
## Date: 
## Brief:
## 
##
################################################################################

###IMPORTS
import sys
import os
from PySide2.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
###SME
from SME_SerialCom import SME_Serial_Communication

## ==> SPLASH SCREEN

## ==> MAIN WINDOW
from GUI_pyqt5 import *




class MyApp(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize principal definitions
        self.range_x_data = 100
        self.axis_p_y = 5
        self.axis_n_y = 0
        self.factor_ksum = 0
        self.factor_kmul = 1
        self.factor_time = 1

        #Configure Serial COM
        self.serial = SME_Serial_Communication()
        self.serial.ports_availables()
        self.serial.data_receive.connect(self.update_data)
        self.ui.ComboBox_Baud.addItems(self.serial.baudrates)
        self.ui.ComboBox_Baud.setCurrentText("9600")
        #Data of serial COM
        self.data_1=0.0

        #Configure Range Type of X axis
        self.ui.ComboBox_rangetype.addItems(['Static','AutoAdjustX'])
        self.ui.ComboBox_rangetype.setCurrentText("Static")
        self.range_type = "Static"
        self.spinBox_range_xvalue = self.range_x_data
        
        #Axis configuration
        self.ui.spinBox_limit_py.setMaximum(999999999)
        self.ui.spinBox_limit_py.setMinimum(-999999999)
        self.ui.spinBox_limit_ny.setMaximum(999999999)
        self.ui.spinBox_limit_ny.setMinimum(-999999999)
        self.ui.spinBox_range_xvalue.setMaximum(999999999)
        self.ui.spinBox_range_xvalue.setMinimum(0)
        self.ui.spinBox_limit_py.setValue(self.axis_p_y)
        self.ui.spinBox_limit_ny.setValue(self.axis_n_y)
        self.ui.spinBox_range_xvalue.setValue(self.range_x_data)
        self.timeacquisition=0.0
        self.ui.TL_factor_sum.setText(str(self.factor_ksum))
        self.ui.TL_factor_multiplier.setText(str(self.factor_kmul))
        self.ui.TL_factor_time.setText(str(self.factor_time))
        self.ui.TL_label_y.setText("")
        self.ui.TL_label_x.setText("")
        self.ui.TL_label_time.setText(str(self.timeacquisition))

        #Configure the conects of Buttons and Methods
        self.ui.BT_Refresh.clicked.connect(self.clickbutton_refresh)
        self.ui.BT_Connect.clicked.connect(self.clickbutton_connect)
        self.ui.BT_Disconnect.clicked.connect(self.clickbutton_disconnect)
        self.ui.BT_Clear.clicked.connect(self.clickbutton_cleardata)
        self.ui.BT_ModifyGraph.clicked.connect(self.clickbutton_ModifyRangeGraph)

        # Set Up Plot Graph
        self.x=[]
        self.y=[]
        self.cont_x=0;
        #Add Background colour to white
        self.ui.graphicsView.setBackground('w')
        # Add Title
        #self.ui.graphicsView.setTitle("Plot1", color="b", size="15pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.ui.graphicsView.setLabel("left", "Signal", **styles)
        #self.ui.graphicsView.setLabel("bottom", "TIME", **styles)
        #Add legend
        self.ui.graphicsView.addLegend()
        #Add grid
        self.ui.graphicsView.showGrid(x=True, y=True)
        #Set Range
        self.ui.graphicsView.setXRange(0, self.range_x_data, padding=0)
        self.ui.graphicsView.setYRange(0, 5, padding=0)
        self.ui.graphicsView.enableAutoRange(axis=None, enable=True, x=True, y=False)
        #Set legend plot
        pen = pg.mkPen(color=(255, 0, 0))
        self.ui.graphicsView.setMouseEnabled(x=False, y=False)
        self.data_line =  self.ui.graphicsView.plot(self.x, self.y, pen=pen)

    def update_data(self,data):

        limit_axis_py = self.ui.spinBox_limit_py.value()
        limit_axis_ny = self.ui.spinBox_limit_ny.value()
        limit_range_x = self.ui.spinBox_range_xvalue.value()
        self.range_type = self.ui.ComboBox_rangetype.currentText()
        self.ui.graphicsView.setYRange(limit_axis_ny, limit_axis_py, padding=0)

        #Save data of serial COM
        self.data_1 = (float(data) * float(self.ui.TL_factor_multiplier.text())) + float(self.ui.TL_factor_sum.text())

        #Process data
        self.x.append(self.cont_x)
        self.y.append(self.data_1)  # Add a new random value.
        if((len(self.y)>int(limit_range_x)) and (self.range_type == "Static")):

            self.x = self.x[1:]  # Remove the first y element.
            self.x.append(self.cont_x)  # Add a new value 1 higher than the last.

            self.y = self.y[1:]  # Remove the first
            self.y.append(self.data_1)  # Add a new random value.
        
        self.timeacquisition = float(self.ui.TL_factor_time.text()) * float(self.cont_x)

        #Update Text Label data
        self.ui.TL_label_x.setText(str(format(self.cont_x, '.1f')))
        self.ui.TL_label_y.setText(str(format(self.data_1, '.3f')))
        self.ui.TL_label_time.setText(str(format(self.timeacquisition, '.1f')))

        #Update Plot Graph
        self.data_line.setData(self.x, self.y)

        self.cont_x+=1

    def clickbutton_ModifyRangeGraph(self):
        self.x=[]
        self.y=[]
        limit_range_x_1 = self.ui.spinBox_range_xvalue.value()
        range_type = self.ui.ComboBox_rangetype.currentText()
        limit_range_x_2 = self.cont_x - limit_range_x_1
        self.ui.graphicsView.setXRange(limit_range_x_1, limit_range_x_2 ,padding=0)
        self.ui.graphicsView.enableAutoRange(axis=None, enable=True, x=True, y=False)

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
        self.ui.TL_label_x.setText("")
        self.ui.TL_label_y.setText("")
        self.clickbutton_ModifyRangeGraph()
        self.cont_x=0
        self.timeacquisition=0.0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())