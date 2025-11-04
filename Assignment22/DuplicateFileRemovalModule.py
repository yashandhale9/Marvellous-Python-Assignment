import os
import hashlib
import time
import smtplib
import ssl
from email.message import EmailMessage

def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path, 'rb')
    hobj = hashlib.md5()
    buffer = fobj.read(BlockSize)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()
    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        raise Exception("The path is invalid")

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        raise Exception("Path is valid but the target is not a directory")

    Duplicate = {}
    Total = 0

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            Total = Total + 1
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate, Total

def DeleteDuplicate(Path, log_file):
    MyDict, TotalFiles = FindDuplicate(Path)
    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                os.remove(subvalue)
                LogMessage(f"Deleted file : {subvalue}", log_file)
                Cnt = Cnt + 1
        Count = 0

    LogMessage(f"Total deleted files: {Cnt}", log_file)
    return TotalFiles, Cnt

def GetLogFileName():
    if not os.path.exists("Marvellous"):
        os.mkdir("Marvellous")

    timestamp = time.ctime()
    filename = "MarvellousLog%s.log" % (timestamp)
    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "_")
    return os.path.join("Marvellous", filename)

def LogMessage(message, log_file):
    lobj = open(log_file, 'a')
    lobj.write(message + "\n")

def SendMail(Sender, Receiver, Password, FileName, Body):
    try:
        message = EmailMessage()
        message['From'] = Sender
        message['To'] = Receiver
        message['Subject'] = 'Marvellous Duplicate File Removal Log'

        message.set_content(Body)

        fobj = open(FileName, 'rb')
        file_data = fobj.read()
        file_name = os.path.basename(FileName)

        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        context = ssl.create_default_context()
        sobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
        sobj.login(Sender, Password)
        sobj.send_message(message)
    except Exception as E:
        print("Unable to send mail:", E)

def ValidateInputs(Directory, Email):
    if not os.path.exists(Directory):
        print("Invalid directory path.")
        return False
    if '@' not in Email or '.' not in Email:
        print("Invalid email ID.")
        return False
    return True
