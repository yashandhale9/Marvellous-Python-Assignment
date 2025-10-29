def FrequencyCount(FileName,str):
    fobj=open(FileName,'r')
    data=fobj.read()
    fobj.close()
    
    Frequency=data.count(str)
    
    return Frequency

def main():
    FileName=input("Enter file name:")
    str=input("Enter string to search:")
    
    ret=FrequencyCount(FileName,str)
    
    print(f"The {str} occurs {ret} times in the file")
    
if __name__=="__main__":
    main()