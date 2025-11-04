import sys
import time
import schedule
import datetime
from DuplicateFileRemovalModule import DeleteDuplicateFiles, LogMessage, GetLogFileName, SendMail, ValidateInputs

def Job(Directory, Email):
    StartTime = datetime.datetime.now()
    LogFile = GetLogFileName()

    LogMessage(f"Scan started at: {StartTime}", LogFile)

    Total, Duplicates = DeleteDuplicateFiles(Directory, LogFile)

    LogMessage(f"Scan completed.", LogFile)

    body = f"""Duplicate File Removal Report

Scan Start Time : {StartTime}
Total Files Scanned : {Total}
Duplicate Files Found and Deleted : {Duplicates}
"""

    Sender = ""
    Password = ""
    SendMail(Sender, Email, Password, LogFile, body)

def DisplayHelp():
    print("This application removes duplicate files from a directory periodically and sends logs via email.")
    print("Usage:")
    print("DuplicateFileRemoval.py <DirectoryPath> <TimeIntervalInMinutes> <RecipientEmail>")

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] in ["--h", "--H"]):
            DisplayHelp()
            return
        
    if len(sys.argv) == 4:
        Directory = sys.argv[1]
        try:
            Interval = int(sys.argv[2])
            Email = sys.argv[3]
        except ValueError:
            print("Time interval must be an integer (minutes).")
            return

        if not ValidateInputs(Directory, Email):
            return

        schedule.every(Interval).minutes.do(Job, Directory, Email)

        print("Scheduled job started. Press Ctrl+C to stop.")
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid arguments.") 
        print("Use --h for help.")

if __name__ == "__main__":
    main()
