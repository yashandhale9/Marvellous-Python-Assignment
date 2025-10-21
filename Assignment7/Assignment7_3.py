def Even(no):
    return no %2==0

def main():
    data=[]
    size=int(input("Enter the size of list:"))
    
    print("Enter the elemnts:")
    for i in range(size):
        no=int(input())
        data.append(no)
        
    FData=list(filter(Even,data))
    print("Even numbers:",FData)
    
if __name__=="__main__":
    main()