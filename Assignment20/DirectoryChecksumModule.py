#This is the module to perform file operations

import os
import time
import datetime
import hashlib

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

def CalculateChecksum(path, BlockSize = 1024):
    try:
        fobj = open(path,'rb')
        hobj = hashlib.md5()
        buffer = fobj.read(BlockSize)
        while(len(buffer) > 0):
            hobj.update(buffer)
            buffer = fobj.read(BlockSize)
        fobj.close()
        return hobj.hexdigest()
    except:
        return None

def DirectoryWatcher(DirectoryName, LogFile):
    try:
        flag = os.path.isabs(DirectoryName)
        if(flag == False):
            DirectoryName = os.path.abspath(DirectoryName)

        flag = os.path.exists(DirectoryName)
        if(flag == False):
            LogMessage("The path is invalid", LogFile)
            return

        flag = os.path.isdir(DirectoryName)
        if(flag == False):
            LogMessage("Path is valid but the target is not a directory", LogFile)
            return

        for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
            for fname in FileNames:
                fname = os.path.join(FolderName,fname)
                checksum = CalculateChecksum(fname)
                if checksum:
                    LogMessage("File name : %s" % fname, LogFile)
                    LogMessage("Checksum  : %s" % checksum, LogFile)
                    LogMessage("", LogFile)
    except Exception as e:
        LogMessage("Exception occurred: %s" % str(e), LogFile)
