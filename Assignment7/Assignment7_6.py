def Prime(n):
    if(n<=1):
        return False
    
    for i in range(2,n):
        if(n % i == 0):
            return False
        else:
            return True
    

def main():
    Data = []
    size = int(input("Enter the size of List : "))

    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    FData = list(filter(Prime,Data))
    print("Prime numbers : ",FData)

if __name__ == "__main__":
    main()