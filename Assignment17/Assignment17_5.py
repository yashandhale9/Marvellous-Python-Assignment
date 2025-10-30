import time
import schedule
import datetime

def WriteTimeIntoFile():
    CurrentTime=datetime.datetime.now()
    fobj=open("Marvellous.txt",'a')
    fobj.write(f"Current time:{CurrentTime}")
    print("Time written in file",CurrentTime)

def main():
    print("Current date and time is:",datetime.datetime.now())
    schedule.every(5).minutes.do(WriteTimeIntoFile)
    
    print("Application is in waiting state..")
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
    main()