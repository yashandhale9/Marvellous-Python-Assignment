def main():
    try:
        fobj=open("data.txt",'r')
        data=fobj.read()
        print("Content of data.txt")
        print(data)
        fobj.close()
        
    except FileNotFoundError as eobj:
        print("File data.txt does not exist",eobj)

if __name__=="__main__":
    main()