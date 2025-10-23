Fact=1
def Factorial(no):
    global Fact
    if(no>=1):
        Fact=Fact*no
        no-=1
        Factorial(no)
    return Fact

def main():
        no=int(input("Enter a number:"))
        ret=Factorial(no)
        
        print("Factorial is:",ret)

if __name__=="__main__":
    main()