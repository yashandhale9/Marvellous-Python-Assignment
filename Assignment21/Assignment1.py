import psutil
import os
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
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
        for element in listprocess:
            data = "PID : {0}\tProcess Name : {1}\tUser : {2}\n".format(
            element['pid'], element['name'], element['username'])
        fobj = open(LogFile, 'a')
        fobj.write(data)

def main():
    foldername = "MarvellousProcess"
    logpath = CreateLog(foldername)
    ProcessScan(logpath)

if __name__ == "__main__":
    main()
