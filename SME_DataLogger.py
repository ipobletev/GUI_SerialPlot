import os.path,csv

class SME_DataLogger:
    def __init__(self,in_folder_name,in_file_name,in_data_name,in_data):
        self.folder_name = ""
        self.file_name = ''
        self.data = []
        self.data_name = []
  
        self.data = in_data
        self.data_name = in_data_name
        self.folder_name = in_folder_name
        self.file_name = in_file_name
        
        #Create folder if not exist
        if not os.path.exists(self.folder_name): os.mkdir(self.folder_name)
        if not (os.path.isfile(self.file_name +'.csv')):
            with open(self.file_name +'.csv','w',newline='') as csvfile:
                #Create a file if not exist
                fileWriter = csv.writer(csvfile,delimiter=',')
                fileWriter.writerow(self.data_name)

    def SME_DataLogger_SaveData(self,in_data):
        #Save data in file
        self.data = in_data
        with open(self.file_name +'.csv','a+',newline='') as csvfile:
            fileWriter = csv.writer(csvfile,delimiter=',')
            fileWriter.writerow(self.data)