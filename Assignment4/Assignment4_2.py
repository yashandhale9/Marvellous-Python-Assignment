Multiplication = lambda No1,No2:No1*No2

def main():
    Value1=int(input("Enter first number:"))
    Value2=int(input("Enter second number:"))
    
    result=Multiplication(Value1,Value2)
    
    print("Multiplication is:",result)
    
if __name__=="__main__":
    main()