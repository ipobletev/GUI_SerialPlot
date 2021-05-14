import time
import os.path,csv
from datetime import datetime

class SME_DataLogger:
    def __init__(self,data):

        #Data form: data = [data_name,[data1,data2,...,datan]]
        #                   data_name = [name1,name2,...,namen]
        self.data = [[]]
        self.data = data

        #Get Datatime
        self.currentDate = datetime.now().strftime('%Y_%m_%d')

        #Create folder if not exist
        if not os.path.exists("Logger"): os.mkdir("Logger")
        if not (os.path.isfile('Logger/'+ self.currentDate+'.csv')):
            with open('Logger/'+ self.currentDate+'.csv','w',newline='') as csvfile:
                #Create a file if not exist
                fileWriter = csv.writer(csvfile,delimiter=',')
                fileWriter.writerow(self.data[0])

    def SME_DataLogger_SaveData(self,data):
        #Save data in file
        with open('Logger/'+ self.currentDate +'.csv','a+',newline='') as csvfile:
            fileWriter = csv.writer(csvfile,delimiter=',')
            fileWriter.writerow(self.data[1])

def main():

    #Variables and name to use
    data_name = ["x","y"]
    data1=0
    data2=0

    #Initialize SME_DataLogger class, name of data and initial data value
    data_logger = SME_DataLogger([data_name,[data1,data2]])
    print(data_logger.data)

    while data1 < 30:

        ###Update Data for every loop
        data_logger.data[1] = [data1,data2]

        data_logger.SME_DataLogger_SaveData(data_logger.data)
        
        #Update to new data
        data1+=1
        data2+=10

        print(data_logger.data[1])
        time.sleep(0.1)
        
    print("end")

if __name__ == "__main__":
    main()
    