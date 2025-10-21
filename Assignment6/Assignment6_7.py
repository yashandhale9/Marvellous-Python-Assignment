
def main():
    data=[]
    print("Enter 5 numbers")
    for i in range(5):
        num=int(input("Enter number:"))
        data.append(num)
    
    large=data[0]
    for i in data:
        if i>large:
            large=i
    
    print("Larget number is:",large)
        
    
if __name__=="__main__":
    main()