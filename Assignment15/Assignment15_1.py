import os

def main():
    print("Enter the name of file that you want to check:")
    FileName=input()
    
    ret=os.path.exists(FileName)

    if(ret==True):
        print("File is present in the current directory")
    else:
        print("File is not present in current directory")
        
if __name__=="__main__":
    main()