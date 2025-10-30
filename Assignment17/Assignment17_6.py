import time 
import datetime
import schedule

def MySchedule1():
    print("Lunch Time!")

def MySchedule2():
    print("Wrap up work!")

def main():
    print("Current date and time is:",datetime.datetime.now())
    schedule.every().day.at("13:00").do(MySchedule1)
    schedule.every().day.at("18:00").do(MySchedule2)
    
    print("Application is in waiting state..")
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
    main()