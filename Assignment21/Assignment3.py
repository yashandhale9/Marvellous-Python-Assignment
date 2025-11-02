import psutil
import os
import sys
import time

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

def main():
    if(len(sys.argv) == 2):
        FolderName = sys.argv[1]
        logfile = CreateLog(FolderName)
        ProcessScan(logfile)
    else:
        print("Invalid number of arguments")
        print("Usage : ProcInfoLog.py DirectoryName")

if __name__ == "__main__":
    main()
