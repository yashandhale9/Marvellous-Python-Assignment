def ChkPrime(n):
    for i in range(2,n):
        if n %i ==0:
            return False
        else:
            return True

def main():
    no=int(input("Enter a number:"))
    result=ChkPrime(no)
    
    if result==True:
        print(f"{no} is a prime number")
    else:
        print(f"{no} is not a prime number")

if __name__=="__main__":
    main()