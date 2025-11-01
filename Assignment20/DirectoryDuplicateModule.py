#This is the module to perform file operations

import os
import hashlib
import time
import datetime

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
        lobj.write("[" + str(timestamp) + "] " + message + "\n")
    except Exception as e:
        print("Error writing to log:", e)

def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path, 'rb')
    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()
    return hobj.hexdigest()

def FindDuplicate(DirectoryName, LogFile):
    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag == False):
        LogMessage("The path is invalid", LogFile)
        exit()

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        LogMessage("Path is valid but the target is not a directory", LogFile)
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

    for key in Duplicate:
        if(len(Duplicate[key]) > 1):
            LogMessage("Duplicate files found for checksum : " + key, LogFile)
            for file in Duplicate[key]:
                LogMessage(file, LogFile)
