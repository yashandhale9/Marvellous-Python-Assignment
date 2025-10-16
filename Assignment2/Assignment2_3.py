def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact
    
def main():
    num=int(input("Enter a number to find factorial:"))
    result=Factorial(num)
    print("Factorial of number is:",result)
    
if __name__=="__main__":
    main()