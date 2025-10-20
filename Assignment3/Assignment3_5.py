from MarvellousNum import ChkPrime

def ListPrime(numbers):
    PrimeSum=0
    for num in numbers:
        if ChkPrime(num):
            PrimeSum +=num
    return PrimeSum

def main():
    no=int(input("Enter how many elements you want to add:"))
    data=[]
    
    for i in range(no):
        num=int(input(f"Enter number {i+1}:"))
        data.append(num)
        
    result=ListPrime(data)
    print("Addition of all prime numbers is :",result)

if __name__=="__main__":
    main()