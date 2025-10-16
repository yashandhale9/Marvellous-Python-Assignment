def DigitCount(n):
    count=0
    if n == 0:
        return 1
    
    while n !=0:
        n=n//10
        count+=1
    return count

def main():
    num=int(input("Enter a number:"))
    result=DigitCount(num)
    print("Digit count is:",result)
    
if __name__=="__main__":
    main()