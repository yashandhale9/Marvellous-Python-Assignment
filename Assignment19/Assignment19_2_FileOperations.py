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

def RenameFilesByExtension(directory_name, OldExt, NewExt, LogFile):
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
                if fname.endswith(OldExt):
                    old_path = os.path.join(folder_name, fname)
                    new_name = fname.rsplit(NewExt, 1)[0] + NewExt
                    new_path = os.path.join(folder_name, new_name)
                    os.rename(old_path, new_path)
                    LogMessage(f"Renamed: {fname} to {new_name}", LogFile)
                    file_found = True

        if not file_found:
            LogMessage(f"No files found with extension '{OldExt}'", LogFile)

    except Exception as e:
        LogMessage(f"Exception occurred: {e}", LogFile)
