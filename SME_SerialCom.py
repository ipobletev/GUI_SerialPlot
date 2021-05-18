from PySide2.QtCore import Signal,QObject
import serial, serial.tools.list_ports
from threading import Thread, Event

#errors
"""
0: No error
1: Serial port cannot open or not found
2: Serial Port has been disconnected

"""

class SME_Serial_Communication(QObject):
    data_receive = Signal(str)

    def __init__(self):
        super().__init__()
        self.serial_com = serial.Serial()
        self.serial_com.timeout = 0.5

        self.baudrates = ['1200','2400','4800','9600','19200','38400','115200','250000']
        self.serial_ports = []
        self.text_serial_ports = []

        self.thread_h = None
        self.alive = Event()
        self.error = 0
    
    def ports_availables(self):
        self.serial_ports = [port.device for port in serial.tools.list_ports.comports()]
        self.text_serial_ports = [str(onePort) for onePort in serial.tools.list_ports.comports()]
        
    def serial_connection(self):
        try:
            self.serial_com.open()
        except:
            #Port was saturate, reconnect.
            if(self.serial_com.is_open): pass
            else:
                #Port cannot open
                self.error = 1

        if(self.serial_com.is_open):
            self.serial_com.flush()
            self.start_thread()
    
    def serial_disconnect(self):
        self.stop_thread()
        self.serial_com.close()
    
    def serial_read_data(self):
       
        while(self.alive.isSet() and self.serial_com.is_open):
            try: 
                data = self.serial_com.readline().decode("utf-8").strip()
                if(len(data)>1):
                    self.data_receive.emit(data)
            except:
                self.alive.clear()
                self.thread_h=None
                self.error = 2

    def start_thread(self):
        self.thread_h=Thread(target=self.serial_read_data)
        self.thread_h.setDaemon(1)
        self.alive.set()
        self.thread_h.start()
    
    def stop_thread(self):
        if(self.thread_h is not None):
            self.alive.clear()
            self.thread_h.join()
            self.thread_h=None
            
