from functools import reduce

def Product(n1,n2):
    return n1*n2

def main():
    data=[]
    size=int(input("Enter the size of list:"))
    
    print("enter the elements:")
    for i in range(size):
        no=int(input())
        data.append(no)
        
    RData=reduce(Product,data)
    print("Product is:",RData)
    
if __name__ == "__main__":
    main()