import os
import hashlib
import time

def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path, 'rb')
    hobj = hashlib.md5()
    buffer = fobj.read(BlockSize)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()
    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):
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

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate

def GetLogFileName():
    timestamp = time.ctime()
    filename = "MarvellousLog%s.log" % (timestamp)
    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "_")
    return filename

def LogMessage(message, log_file):
    lobj=open(log_file, 'a')
    lobj.write(message + "\n")

def DeleteDuplicate(Path, log_file):
    MyDict = FindDuplicate(Path)
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
