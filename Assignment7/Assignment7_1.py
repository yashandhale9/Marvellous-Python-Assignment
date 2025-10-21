square=lambda No:No**2
cube=lambda No:No**3

def main():
    no=int(input("Enter a number:"))
    result=square(no)
    print("Square:",result)
    
    result=cube(no)
    print("Cube:",result)
    
if __name__=="__main__":
    main()