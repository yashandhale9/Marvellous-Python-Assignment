def Frequency(numbers,target):
    count=0
    for num in numbers:
        if num==target:
            count+=1
    return count

def main():
    N=int(input("How many elements you want to enter?:"))
    data=[]
    
    for i in range(N):
        num=int(input(f"Enter number {i+1}:"))
        data.append(num)
        
    SearchNum=int(input("Enter the number to find frequency of:"))
    freq=Frequency(data,SearchNum)
    
    print(f"Frequency of {SearchNum} is:",freq)

if __name__=="__main__":
    main()