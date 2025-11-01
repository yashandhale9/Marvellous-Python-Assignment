
import os
import hashlib
import time
import datetime

def CalculateChecksum(path, BlockSize=1024):
    fobj = open(path, 'rb')
    hobj = hashlib.md5()
    buffer = fobj.read(BlockSize)
    while (len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)
    fobj.close()
    return hobj.hexdigest()

def GetLogFileName():
    timestamp = time.ctime()
    filename = "MarvellousLog%s.log" % (timestamp)
    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "_")
    return filename

def LogMessage(message, LogFile):
    try:
        lobj = open(LogFile, 'a')
        timestamp = datetime.datetime.now()
        lobj.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"Error writing to log: {e}")

def FindDuplicate(DirectoryName="Marvellous"):
    flag = os.path.isabs(DirectoryName)
    if (flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if (flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    if (flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate

def DeleteDuplicate(MyDict, LogFile):
    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))
    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if (Count > 1):
                os.remove(subvalue)
                LogMessage(f"Deleted file: {subvalue}", LogFile)
                Cnt = Cnt + 1
        Count = 0

    LogMessage(f"Total deleted files: {Cnt}", LogFile)
