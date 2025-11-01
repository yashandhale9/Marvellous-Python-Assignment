
import sys
import time
from DirectoryDuplicateRemoval2Module import DeleteDuplicate, LogMessage, GetLogFileName

def main():
    Border = "-" * 54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    LogFile = GetLogFileName()
    LogMessage("Script started.", LogFile)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to remove duplicate files from a directory.")
            LogMessage("Displayed help message.", LogFile)

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirectory")
            print("Please provide valid absolute path")
            LogMessage("Displayed usage message.", LogFile)

        else:
            StartTime = time.time()
            DeleteDuplicate(sys.argv[1], LogFile)
            EndTime = time.time()
            
            exec_time = EndTime - StartTime
            print("Execution time required for the script is :", exec_time, "seconds")
            LogMessage(f"Execution time: {exec_time:.2f} seconds", LogFile)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 
        LogMessage("Invalid number of command line arguments.", LogFile)

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

    LogMessage("Script ended.", LogFile)

if __name__ == "__main__":
    main()
