def DigitSum(n):
    sum=0
    while n != 0:
        digit=n%10
        sum+=digit
        n=n//10
    return sum

def main():
    num=int(input("Enter a number:"))
    result=DigitSum(num)
    print("Addition of digits:",result)
    
if __name__=="__main__":
    main()