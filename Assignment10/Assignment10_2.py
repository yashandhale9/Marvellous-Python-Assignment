# Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4   3   Output : 12
# Input : 6   3   Output : 18

Multiply=lambda No1,No2:No1*No2

def main():
    Num1=int(input("Enter first number:"))
    Num2=int(input("Enter second number:"))
    
    result=Multiply(Num1,Num2)
    print("Multiplication is:",result)
    
if __name__=="__main__":
    main()