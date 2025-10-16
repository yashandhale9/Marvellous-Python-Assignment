def EvenOdd(n):
    if (n % 2== 0):
        return True
    else:
        return False
              
        
def main():
    num=int(input("Enter a number:"))
    result=EvenOdd(num)
    
    if result == True:
        print("Number is even")
    else:
        print("Number is odd")

if __name__=="__main__":
    main()