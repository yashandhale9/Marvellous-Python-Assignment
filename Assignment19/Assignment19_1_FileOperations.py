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
        lobj=open(LogFile, 'a')
        timestamp = datetime.datetime.now()
        lobj.write(f"[{timestamp}] {message}\n")
            
    except Exception as e:
        print(f"Error writing to log: {e}")

def DisplayFilesByExtension(directory_name, extension, LogFile):
    try:
        if not os.path.isabs(directory_name):
            directory_name = os.path.abspath(directory_name)

        if not os.path.exists(directory_name):
            LogMessage("The path is invalid", LogFile)
            return

        if not os.path.isdir(directory_name):
            LogMessage("Path is valid but the target is not a directory", LogFile)
            return

        file_found = False
        for folder_name, subfolder_names, file_names in os.walk(directory_name):
            for fname in file_names:
                if fname.endswith(extension):
                    print(fname)
                    LogMessage(f"Found file: {fname}", LogFile)
                    file_found = True

        if not file_found:
            LogMessage(f"No files found with extension '{extension}'", LogFile)

    except Exception as e:
        LogMessage(f"Exception occurred: {e}", LogFile)
