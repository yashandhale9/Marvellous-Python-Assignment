#This is the module to perform file operations

import os
import datetime
import time

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

def CopyFiles(SourceDir, DestDir, LogFile):
    try:
        if not os.path.isabs(SourceDir):
            SourceDir = os.path.abspath(SourceDir)
        
        if not os.path.exists(SourceDir):
            LogMessage("Source directory does not exist.", LogFile)
            return

        if not os.path.isdir(SourceDir):
            LogMessage("Source path is not a directory.", LogFile)
            return

        if not os.path.exists(DestDir):
            os.mkdir(DestDir)
            LogMessage(f"Destination directory '{DestDir}' created.", LogFile)

        for foldername, subfolders, filenames in os.walk(SourceDir):
            for fname in filenames:
                src_path = os.path.join(foldername, fname)
                dst_path = os.path.join(DestDir, fname)

                try:
                    sobj=open(src_path, 'rb')
                    dobj=open(dst_path, 'wb')
                    dobj.write(sobj.read())
                    LogMessage(f"Copied file: {fname}", LogFile)
                except Exception as inner_e:
                    LogMessage(f"Failed to copy {fname}: {inner_e}", LogFile)

    except Exception as e:
        LogMessage(f"Exception occurred: {e}", LogFile)