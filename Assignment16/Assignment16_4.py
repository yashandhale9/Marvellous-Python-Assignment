def main():
    fobj=open("numbers.txt",'w')
    
    print("Enter 10 numbers:")

    for i in range(10):
        print(f"Enter number{i+1}:")
        num=input()
        fobj.write(num +"\n")
        
    fobj.close()
        
    print("Numbers written succesfulyy...")
if __name__=="__main__":
    main()