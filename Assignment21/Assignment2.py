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

def ProcessInfoByName(process_name, LogFile):
    flag = False

    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == process_name.lower():
                info = proc.as_dict(attrs=['pid','name','username'])
                data = "PID : {0}\tProcess Name : {1}\tUser : {2}\n".format(
                    info['pid'], info['name'], info['username']
                )
                with open(LogFile, 'a') as fobj:
                    fobj.write(data)
                flag = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if(flag == False):
        fobj=open(LogFile, 'a')
        fobj.write("Flag : No such running process exists with name : %s\n" % process_name)

def main():
    foldername = "MarvellousProcess"
    logpath = CreateLog(foldername)

    if(len(sys.argv) == 2):
        ProcessInfoByName(sys.argv[1], logpath)
    else:
        print("Invalid number of arguments.")
        print("Usage: ProcInfo.py ProcessName")

if __name__ == "__main__":
    main()
