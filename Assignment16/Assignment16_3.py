def Count(FileName):
    try:
        fobj=open(FileName,'r')
        lines=fobj.readlines()
        
        no_lines=len(lines)
        no_words=0
        no_char=0
        
        for i in lines:
            words=i.split()
            no_words+=len(words)
            no_char+=len(i)
            
        print("File:",FileName)
        print("Number of Lines:",no_lines)
        print("Number of Words:",no_words)
        print("Number of Characters:",no_char)

            
    except FileNotFoundError as eobj:
        print("File does not exist",eobj)

def main():
    print("Enter file name:")
    FileName=input()
    
    Count(FileName)

if __name__=="__main__":
    main()