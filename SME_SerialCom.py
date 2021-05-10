from PySide2.QtCore import Signal,QObject
import serial, serial.tools.list_ports
from threading import Thread, Event

class SME_Serial_Communication(QObject):
    data_receive = Signal(str)

    def __init__(self):
        super().__init__()
        self.serial_com = serial.Serial()
        self.serial_com.timeout = 0.5

        self.baudrates = ['1200','2400','4800','9600','19200','38400','115200']
        self.serial_ports = []
        self.text_serial_ports = []

        self.thread_h = None
        self.alive = Event()
    
    def ports_availables(self):
        self.serial_ports = [port.device for port in serial.tools.list_ports.comports()]
        self.text_serial_ports = [str(onePort) for onePort in serial.tools.list_ports.comports()]
        
    def serial_connection(self):
        try:
            self.serial_com.open()
        except:
                pass
        if(self.serial_com.is_open):
            self.start_thread()
    
    def serial_disconnect(self):
        self.stop_thread()
        self.serial_com.close()
    
    def serial_read_data(self):
        while(self.alive.isSet() and self.serial_com.is_open):
            data = self.serial_com.readline().decode("utf-8").strip()
            if(len(data)>1):
                self.data_receive.emit(data)
    
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
