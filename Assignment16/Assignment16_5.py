def Display(FileName):
    try:
        fobj = open(FileName, 'r')
        print("Lines with more than 5 words:\n")

        for i in fobj:
            words = i.strip().split() 
            if len(words) > 5:
                print(i.strip())      

        fobj.close()

    except FileNotFoundError:
        print("Error: The file does not exist..")
    
def main():
    print("Enter file name:")
    FileName=input()
    
    Display(FileName)
    
if __name__=="__main__":
    main()