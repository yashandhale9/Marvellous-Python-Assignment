import os
import sys

def main():
    if len(sys.argv)!=3:
        print("Use:python Filename.py FileName1 FileName2")
        return
    
    FileName1=sys.argv[1]
    FileName2=sys.argv[2]
    
    ret=os.path.exists(FileName1)
    if(ret==True):
        print(f"{FileName1} exists")
    else:
        print(f"{FileName1} not exists")
        
    ret=os.path.exists(FileName2)
    if(ret==True):
        print(f"{FileName2} exists")
    else:
        print(f"{FileName2} not exists")
        
    fobj1=open(FileName1,'r')
    data1=fobj1.read()
    fobj1.close()
    
    fobj2=open(FileName2,'r')
    data2=fobj2.read()
    fobj2.close()
    
    if(data1==data2):
        print("Both the files contains same content")
    else:
        print("Content is not same")

if __name__=="__main__":
    main()