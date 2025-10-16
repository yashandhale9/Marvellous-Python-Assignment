import Arithmetic

def main():
    
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))

    ans=Arithmetic.Add(no1,no2)
    print("Addition is :",ans)
    #print("Addition is :",Arithmetic.Add(no1,no2))

    ans=Arithmetic.Sub(no1,no2)
    print("Substraction is :",ans)

    ans=Arithmetic.Mul(no1,no2)
    print("Multiplication is :",ans)

    ans=Arithmetic.Div(no1,no2)
    print("Division is :",ans)

if __name__== "__main__":
    main()