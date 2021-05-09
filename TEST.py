import sys
from HMI_SerialPlot import *
from PySide2.QtCore import QTimer
from serial_com import *

class MiApp(MainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serial = 
