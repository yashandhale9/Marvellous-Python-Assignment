from functools import reduce 

ChkEven=lambda No:(No%2==0)
Square=lambda No:No*No
Add=lambda No1,No2:No1+No2

def main():
    N=int(input("How many elements you want to insert ?:"))
    Data=[]
    
    for i in range(N):
        num=int(input(f"Enter Element{i+1}:"))
        Data.append(num)
        
    print("Input Elements:",Data)
    
    FData=list(filter(ChkEven,Data))
    print("Filtered Data:",FData)

    MData=list(map(Square,FData))
    print("Mapped Data:",MData)
    
    RData=reduce(Add,MData)
    print("Reduced Data:",RData)
    
if __name__=="__main__":
    main()