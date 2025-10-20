import Arithmetic5_1 as A

def main():
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    
    result=A.Sum(no1,no2)
    print("Sum of two numbers is:",result)
    
    result=A.Difference(no1,no2)
    print("Difference of two numbers is:",result)
    
    result=A.Product(no1,no2)
    print("Product of two numbers is:",result)
    
    result=A.Division(no1,no2)
    print("Division of two numbers is:",result)

if __name__=="__main__":
    main()