import os

def main():
    print("Enter the name of file that you want to open:")
    FileName=input()
    
    ret=os.path.exists(FileName)
    
    if(ret==True):
        print("File is present in current directory")
        
        fobj=open(FileName,'r')
        Data=fobj.read()
        
        print("Data from file is:\n",Data)
        
        fobj.close()
    
    else:
        print("There is no such file")

if __name__=="__main__":
    main()