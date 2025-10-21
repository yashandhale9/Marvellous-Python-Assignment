def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def main():
    no=int(input("Enter a number:"))
    result=Factorial(no)
    
    print("Factorial of number is:",result)

if __name__=="__main__":
    main()