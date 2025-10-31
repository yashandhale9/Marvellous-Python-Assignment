#This is the main file

import sys
from Assignment19_3_FileOperations import GetLogFileName, LogMessage, CopyFiles

def main():
    Border = "-" * 54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    LogFile = GetLogFileName()
    LogMessage("Script started.", LogFile)

    if len(sys.argv) == 2:
        if sys.argv[1] in ["--h", "--H"]:
            print("This application is used to copy files from one directory to another.")
            LogMessage("Displayed help message.", LogFile)

        elif sys.argv[1] in ["--u", "--U"]:
            print("Use the given script as:")
            print("python main.py SourceDirectory DestinationDirectory")
            LogMessage("Displayed usage message.", LogFile)

        else:
            print("Invalid flag. Use --h or --u for help.")
            LogMessage("Invalid flag provided.", LogFile)

    elif len(sys.argv) == 3:
        SourceDir = sys.argv[1]
        DestDir = sys.argv[2]
        CopyFiles(SourceDir, DestDir, LogFile)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as:")
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
