from functools import reduce

Range=lambda No:70<=No<=90
Increase=lambda No:No+10
Product=lambda No1,No2:No1*No2
    
def main():
    
    N=int(input("How many element you want to insert ?: "))
    data=[]
    print(f"Enter Element in list:")
    
    for i in range(N):
        num=int(input(f"Enter Element {i+1}: "))
        data.append(num)
    
    print("Input Data:",data)
    
    FData=list(filter(Range,data))
    print("Filtered Data:",FData)
    
    MData=list(map(Increase,FData))
    print("Mapped Data:",MData)
    
    RData=reduce(Product,MData)
    print("Reduced Data:",RData)
    
if __name__=="__main__":
    main()