#This is the main file

import sys
from DirectoryChecksumModule import GetLogFileName, LogMessage, DirectoryWatcher

def main():
    Border = "-" * 54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    LogFile = GetLogFileName()
    LogMessage("Script started.", LogFile)

    if(len(sys.argv) == 2):
        if(sys.argv[1] in ["--h", "--H"]):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")
            LogMessage("Displayed help message.", LogFile)

        elif(sys.argv[1] in ["--u", "--U"]):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")
            LogMessage("Displayed usage message.", LogFile)

        else:
            DirectoryWatcher(sys.argv[1], LogFile)

    else:
        print("Invalid number of coomand line arguments")
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
