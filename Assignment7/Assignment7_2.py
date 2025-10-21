def Double(No):
    return No*2

def main():
    data=[]
    size=int(input("Enter the size of list:"))
    print("Enter list:")
    for i in range(size):
        no=int(input())
        data.append(no)
    
    
    
    MData=list(map(Double,data))
    print("Doubled list:",MData)
    
if __name__=="__main__":
    main()