import time
import schedule
import datetime

def CheckMail():
    print(f"{datetime.datetime.now()}:Checking mail...")
    
def main():
    print("Application started..")
    print("Scheduler for email checking is running...")
    print("Current time:",datetime.datetime.now())
    
    schedule.every(10).seconds.do(CheckMail)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
        
if __name__=="__main__":
    main()