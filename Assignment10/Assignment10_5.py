# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def ChkPrime(No):
    Result=[]
    if No<=1:
        return False
    for i in range(2,No):
        if(No%i==0):
            return False
    return True

def Multiply(No):
    return No*2

def Max(No1,No2):
    Max=No1
    if(No2>=Max):
        Max=No2
    return Max

def main():
    no=int(input("How many elements u wanna insert?:"))
    Data=[]
    
    print("Enter elements:")
    for i in range(no):
        num=int(input())
        Data.append(num)
        
    FData=list(filter(ChkPrime,Data))
    print("List after filter:",FData)
    
    MData=list(map(Multiply,FData))
    print("List after map:",MData)
    
    RData=reduce(Max,MData)
    print("Output of reduce:",RData)

if __name__=="__main__":
    main()
    