def ChkMax(n1,n2,n3):
    if n2<n1>n3:
        print(f"Largest number is:{n1}")
    elif n1<n2>n2:
        print(f"Largest number is:{n2}")
    else:
        print(f"Largest number is:{n3}")
        
    
def main():
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    no3=int(input("Enter third number:"))
    ChkMax(no1,no2,no3)
    
if __name__=="__main__":
    main()