################################################################################
## Proyect: 
## Autor: Ismael Poblete
## Date: 13-05-2021
## Brief: Program
## 
##
################################################################################

###IMPORTS
import sys
import os
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QTimer
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from datetime import datetime

###SME
from SME_SerialCom import SME_Serial_Communication
from SME_DataLogger import *

## ==> SPLASH SCREEN
from UI_SplashScreen import *
## ==> MAIN WINDOW
from UI_MainWindow import *



class MyApp(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize principal definitions
        self.range_x_data = 100
        self.axis_p_y = 100
        self.axis_n_y = 0
        self.factor_ksum = 0
        self.factor_kmul = 1
        self.factor_time = 1

        self.flag_data_acquisition=False

        #Configure Serial COM
        self.serial = SME_Serial_Communication()
        self.serial.ports_availables()
        self.serial.data_receive.connect(self.update_data)
        self.ui.ComboBox_Baud.addItems(self.serial.baudrates)
        self.ui.ComboBox_Baud.setCurrentText("9600")
        #Data of serial COM
        self.data_1=0.0
        #Set indicator level off not connected
        self.ui.Indicador.setStyleSheet("border-radius:130px;\n"
"background-color:rgb(225, 225, 225);\n"
"")
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
        self.ui.Check_datapoint.stateChanged.connect(self.check_dataplot)
        self.ui.Check_Record.stateChanged.connect(self.data_acquisition)

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
        self.ui.graphicsView.setYRange(0, self.axis_p_y, padding=0)
        self.ui.graphicsView.enableAutoRange(axis=None, enable=True, x=True, y=False)
        #Set legend plot
        self.pen = pg.mkPen(color=(255, 0, 0), width=4, style=QtCore.Qt.SolidLine)
        self.ui.graphicsView.setMouseEnabled(x=False, y=False)
        
        self.data_line =  self.ui.graphicsView.plot(self.x, self.y, pen=self.pen)
        
        #self.data_line =  self.ui.graphicsView.plot(self.x, self.y, pen=pen, symbol='o', symbolPen ='r',symbolSize=5, symbolBrush=0.2, name ='blue')
        #self.data_line.setSymbolPen(QColor(220, 30, 30))

        # Add crosshair lines.
        self.crosshair_v = pg.InfiniteLine(angle=90, movable=False)
        self.crosshair_h = pg.InfiniteLine(angle=0, movable=False)
        self.ui.graphicsView.addItem(self.crosshair_v, ignoreBounds=True)
        self.ui.graphicsView.addItem(self.crosshair_h, ignoreBounds=True)
        
        self.proxy = pg.SignalProxy(self.ui.graphicsView.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
   
    def update_data(self,data):

        limit_axis_py = self.ui.spinBox_limit_py.value()
        limit_axis_ny = self.ui.spinBox_limit_ny.value()

        self.range_type = self.ui.ComboBox_rangetype.currentText()
        self.ui.graphicsView.setYRange(limit_axis_ny, limit_axis_py, padding=0)

        #Save data of serial COM
        self.data_1 = (float(data) * float(self.ui.TL_factor_multiplier.text())) + float(self.ui.TL_factor_sum.text())
        
        #Process data
        if((len(self.y)>int(self.range_x_data)) and (self.range_type == "Static")):

            self.x = self.x[1:]  # Remove the first X element.
            self.y = self.y[1:]  # Remove the first Y element.

        self.x.append(self.cont_x)  # Add a new value 1 higher than the last.
        self.y.append(self.data_1)  # Add a new random value.
        
        self.timeacquisition = float(self.ui.TL_factor_time.text()) * float(self.cont_x)

        #Update Text Label data
        self.ui.TL_label_x.setText(str(format(self.cont_x, '.1f')))
        self.ui.TL_label_y.setText(str(format(self.data_1, '.3f')))
        self.ui.TL_label_time.setText(str(format(self.timeacquisition, '.1f')))
     
        #Update Plot Graph
        self.data_line.setData(self.x, self.y)
       
        #Save data acquisition
        if(self.flag_data_acquisition):
            self.data_logger.SME_DataLogger_SaveData([self.cont_data, format(self.data_1, '.3f')])
            self.cont_data+=1
     
        self.cont_x+=1
        
    def mouseMoved(self, e):
        pos = e[0]
        if self.ui.graphicsView.sceneBoundingRect().contains(pos):
            mousePoint = self.ui.graphicsView.getPlotItem().vb.mapSceneToView(pos)
            self.mouse_x = format(mousePoint.x(), '.0f')

            

            if (int(self.mouse_x) < int(self.cont_x)):
                self.crosshair_v.setPos(mousePoint.x())
                self.ui.TL_cursor_x.setText(str(format(mousePoint.x(), '.0f')))
                
                if (int(self.cont_x) > int(self.range_x_data)):
                    self.location_y = int(self.range_x_data) - int(self.cont_x) + int(self.mouse_x) + 1
                else :
                    self.location_y = int(self.mouse_x) + 1

                self.crosshair_h.setPos(self.y[self.location_y])
                self.ui.TL_cursor_y.setText(str(self.y[self.location_y]))

    def check_dataplot(self):
        self.data_line.clear()
        if(self.ui.Check_datapoint.checkState()):
            self.data_line =  self.ui.graphicsView.plot(self.x, self.y, pen=self.pen, symbol='o', symbolPen ='r',symbolSize=5, symbolBrush=0.2)
            self.data_line.setSymbolPen(QColor(220, 30, 30))
        else :
            self.data_line =  self.ui.graphicsView.plot(self.x, self.y, pen=self.pen)

    def clickbutton_connect(self):
        self.x.clear()
        self.y.clear()
        self.x=[]
        self.y=[]
        index = self.ui.ComboBox_PortSerial.currentIndex()
        port = self.serial.serial_ports[index]
        baud = self.ui.ComboBox_Baud.currentText()
        self.serial.serial_com.port = port
        self.serial.serial_com.baudrate = baud
        self.serial.serial_connection()
        if(self.serial.alive):
            self.ui.Indicador.setStyleSheet("border-radius:130px;\n"
            "background-color:rgb(0, 255, 0);\n"
            "")

    def clickbutton_disconnect(self):

        self.serial.serial_disconnect()
        self.ui.Indicador.setStyleSheet("border-radius:130px;\n"
        "background-color:rgb(225, 225, 225);\n"
        "")

    def clickbutton_refresh(self):

        self.serial.ports_availables()
        self.ui.ComboBox_PortSerial.clear()
        self.ui.ComboBox_PortSerial.addItems(self.serial.text_serial_ports)

    def clickbutton_cleardata(self):
        self.ui.TL_label_x.setText("")
        self.ui.TL_label_y.setText("")

        #Get the new range value and clear plot x and y data
        self.range_x_data = self.ui.spinBox_range_xvalue.value()
        self.x.clear()
        self.y.clear()
        self.x=[]
        self.y=[]

        #Set limits 1________2
        limit_range_x_1 = self.cont_x
        limit_range_x_2 = limit_range_x_1 + self.range_x_data
        self.ui.graphicsView.setXRange(limit_range_x_1, limit_range_x_2 ,padding=0)
        self.ui.graphicsView.enableAutoRange(axis=None, enable=True, x=True, y=False)
        self.cont_x=0
        self.timeacquisition=0.0

    def data_acquisition(self):
        
        if(self.ui.Check_Record.checkState()):
            #Acquire Date
            now = datetime.now()
            currentDate = now.strftime("%m-%d-%Y_%H.%M.%S")
            #Variables and name to use
            folder_name = "Logger"
            file_name = 'Logger/'+ str(currentDate) +'.csv'
            data_name = ["x","y"]
            self.flag_data_acquisition = True
            self.cont_data=0
            self.data_logger = SME_DataLogger(folder_name,file_name,data_name,[self.cont_data,self.y])

        else:
            self.flag_data_acquisition = False         

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        
        ## UI ==> INTERFACE CODES
        ########################################################################
        ## REMOVE TITLE BAR
        self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setBlurRadius(30)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(self.shadow)  

        self.show()
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress_bar)
        # TIMER IN MILLISECONDS
        self.timer.start(10)
        self.counter = 0

    def progress_bar(self):

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(self.counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MyApp()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.counter += 1    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())