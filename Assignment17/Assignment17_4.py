import time
import schedule
import datetime

def MySchedule():
    print("Namaskar...")

def main():
    print("Current date and time is:",datetime.datetime.now())
    schedule.every().day.at("09:00").do(MySchedule)
    
    print("Application is in waiting state..")
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
        
if __name__=="__main__":
    main()