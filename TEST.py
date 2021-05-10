import sys
from HMI_SerialPlot import *
from PySide2.QtCore import QTimer
from SME_SerialCom import serial_communication

class MyApp(MainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serial = serial_communication()
        self.ports_availables()
        self.data_1=0.0

        self.serial.data_receive.connect(self.data_serial)
        self.ui.comboBox_baud.addItem(self.serial.baudrates)
        self.ui.comboBox.setCurrentText("9600")

        self.ui.BT_Refresh.clicked.connect(self.clickbutton_refresh)
        self.ui.BT_Connect.clicked.connect(self.clickbutton_connect)
        self.ui.BT_Disconnect.clicked.connect(self.clickbutton_disconnect)
        #self.ui.BT_clear.clicked.connect(self.clickbutton_disconnect)
    
    def data_serial(self,data):
        self.data_1 = float(data)

    def clickbutton_connect(self):

        port = COM4
        baud = self.comboBox_baud.currentText()

        self.serial.serial_ports = port
        self.serial.baudrates = baud
        self.serial.serial_connection()

    def clickbutton_disconnect(self):

        self.serial.serial_disconnect()

    def clickbutton_refresh(self):

        self.serial.ports_availables()
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.serial.serial_ports)
        
    def update_visual_data(self):
        self.data_acquisition()
        QTimer.singleShot(10,self.update_visual_data)

    def data_acquisition(self):
        self.ui.lineEdit.setText(str(self.data_1))
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())