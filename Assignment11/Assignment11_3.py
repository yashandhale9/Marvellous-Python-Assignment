sum=0

def DigitSum(no):
    global sum
    if(no!=0):
        Digit=no%10
        sum=sum+Digit
        no=no//10
        DigitSum(no)
    return sum

def main():
    no=int(input("Enter a number:"))
    ret=DigitSum(no)
    
    print("Sum of digit is:",ret)

if __name__=="__main__":
    main()