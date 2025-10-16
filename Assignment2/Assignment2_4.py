def AdditionFactors(n):
    sum=0
    for i in range(1,n):
        if n % i ==0:
            sum+=i
    return sum            
        
def main():
    num=int(input("Enter a number:"))
    result=AdditionFactors(num)
    print("Addition of factors is:",result)

if __name__=="__main__":
    main()