from functools import reduce 

def Prime(No):
    if No<=1:
        return False
    for i in range(2,No):
        if No % i==0:
            return False
    return True    

def Increase(No):
    return No *2

def Max(a,b):
    return a if a>b else b
    

def main():
    N=int(input("How many elements you want to insert ?:"))
    Data=[]
    
    for i in range(N):
        num=int(input(f"Enter Element{i+1}:"))
        Data.append(num)
        
    print("Input Elements:",Data)
    
    FData=list(filter(Prime,Data))
    print("Filtered Data:",FData)

    MData=list(map(Increase,FData))
    print("Mapped Data:",MData)
    
    RData=reduce(Max,MData)
    print("Reduced Data:",RData)
    
if __name__=="__main__":
    main()