import os
import sys

def main():
    if len(sys.argv)!=2:
        print("Use: python FileName.py SourceFileName")
        return
    
    SourceFile=sys.argv[1]
    DestinationFile="Demo.txt"
    
    ret=os.path.exists(SourceFile)

    if(ret==True):
        print("Source file exists..")
        print("Copying content..")
        
        fsrc=open(SourceFile,'r')
        data=fsrc.read()
        
        fdest=open(DestinationFile,'w')
        fdest.write(data)
        
        print(f"Content copied to{DestinationFile} successfulyy..")
        
    else:
        print("File is not present in current directory")

if __name__=="__main__":
    main()