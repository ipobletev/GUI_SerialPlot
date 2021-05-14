import os.path,csv
from datetime import datetime

class SME_DataLogger:
    def __init__(self,in_data_name,in_data):

        self.data = []
        self.data_name = []
        self.data = in_data
        self.data_name = in_data_name

        #Get Datatime
        self.currentDate = datetime.now().strftime('%Y_%m_%d')

        #Create folder if not exist
        if not os.path.exists("Logger"): os.mkdir("Logger")
        if not (os.path.isfile('Logger/'+ self.currentDate+'.csv')):
            with open('Logger/'+ self.currentDate+'.csv','w',newline='') as csvfile:
                #Create a file if not exist
                fileWriter = csv.writer(csvfile,delimiter=',')
                fileWriter.writerow(self.data_name)

    def SME_DataLogger_SaveData(self,in_data):
        #Save data in file
        self.data = in_data
        with open('Logger/'+ self.currentDate +'.csv','a+',newline='') as csvfile:
            fileWriter = csv.writer(csvfile,delimiter=',')
            fileWriter.writerow(self.data)