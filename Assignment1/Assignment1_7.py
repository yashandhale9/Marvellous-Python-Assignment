def CheckDivisible(num):
    if num % 5== 0:
        return True
    else:
        return False
    
    
def main():
    print("Enter a number:")
    number=int(input())
    
    result=CheckDivisible(number)
    
    if result:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")
        
if __name__ =="__main__":
    main()