import time
import schedule
import datetime

def MySchedule():
    print("Current date and time is:",datetime.datetime.now())

def main():
    print("Current date and time is:",datetime.datetime.now())
    schedule.every(1).minutes.do(MySchedule)
    
    print("Application is in waiting state..")
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
        
if __name__=="__main__":
    main()