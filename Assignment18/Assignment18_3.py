import os
import sys

def main():
    if len(sys.argv)!=2:
        print("Use:python FileName SourceFileName")
        return
    
    SourceFile=sys.argv[1]
    DestinationFile="Demo.txt"
    
    ret=os.path.exists(SourceFile)
    if(ret==False):
        print(f"{SourceFile} is not exist")
        return
    
    else:
        try:
            sobj=open(SourceFile,'r')
            data=sobj.read()
            
            dobj=open(DestinationFile,'w')
            dobj.write(data)
            
            print(f"Contents copied from {SourceFile} to {DestinationFile} sucessfulyyyyyyy")
            
        except Exception as eobj:
            print("Error occured:",eobj)
            
if __name__=="__main__":
    main()
            