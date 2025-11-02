import psutil
import os
import sys
import time
import smtplib
import ssl
from email.message import EmailMessage

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolderName, "Marvellous%s.log" %(timestamp))

    fobj = open(FileName, "w")

    border = "-"*80
    fobj.write(border + "\n")
    fobj.write("\t\tMarvellous Infosystems Process Log\n")
    fobj.write("\t\tLog file is created at : "+time.ctime()+"\n")
    fobj.write(border + "\n")

    return FileName

def ProcessScan(LogFile):
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            data = "PID : {0}\tProcess Name : {1}\tUser : {2}\n".format(
                info['pid'], info['name'], info['username']
            )
            fobj=open(LogFile, 'a')
            fobj.write(data)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def SendMail(Sender, Receiver, Password, FileName):
    try:
        message = EmailMessage()
        message['From'] = Sender
        message['To'] = Receiver
        message['Subject'] = 'Marvellous Process Log File'

        message.set_content("Please find attached the log file of running processes.")

        fobj=open(FileName, 'rb')
        file_data = fobj.read()
        file_name = os.path.basename(FileName)
        
        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        context = ssl.create_default_context()
        sobj= smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
        sobj.login(Sender, Password)
        sobj.send_message(message)
    
    except Exception as e:
        print("Unable to send email:", e)

def main():
    if(len(sys.argv) == 3):
        FolderName = sys.argv[1]
        MailID = sys.argv[2]

        LogFile = CreateLog(FolderName)
        ProcessScan(LogFile)

        
        Sender = ""    
        Password = ""
        
        SendMail(Sender, MailID, Password, LogFile)

    else:
        print("Invalid number of arguments")
        print("Usage : ProcInfoLog.py DirectoryName MailID")

if __name__ == "__main__":
    main()
