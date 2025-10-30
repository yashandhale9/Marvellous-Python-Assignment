import time 
import datetime
import schedule
import os

def Backup():
    SourceFile="Source.txt"
    BackupFile="Backup.txt"
    
    if os.path.exists(SourceFile):
        sobj=open(SourceFile,'r')
        data=sobj.read()
    
        bobj=open(BackupFile,'w')
        bobj.write(data)
    
        log_entry=f"{datetime.datetime.now()}:Backup successful\n"
    else:
        log_entry = f"{datetime.datetime.now()}: Backup failed - Source file not found!\n"
        
    lobj=open("Backup_log.txt",'a')
    lobj.write(log_entry)
    

def main():
    print("Current date and time is:",datetime.datetime.now())
    schedule.every().hour.do(Backup)
    
    print("Application is in waiting state..")
    print("Scheduler for Backingup Files is running...")
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
    main()