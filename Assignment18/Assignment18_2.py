import os

def main():
    print("Enter the name of file that you to read:")
    FileName=input()
    
    ret=os.path.exists(FileName)
    
    if (ret==True):
        print("File is present in current directory")
        fobj=open(FileName,'r')
        data=fobj.read()
        
        print("Content from file is:\n",data)

if __name__=="__main__":
    main()