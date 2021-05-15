import time
import os.path,csv
from datetime import datetime

def main():
    
    now = datetime.now()
    currentTime = now.strftime("%m/%d/%Y %H:%M:%S")
    print(str(currentTime))
    

if __name__ == "__main__":
    main()
    