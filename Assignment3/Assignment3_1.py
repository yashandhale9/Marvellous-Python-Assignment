def Add(n):
    numbers=[]
    for i in range(n):
        num=int(input(f"Enter element{i+1}:"))
        numbers.append(num)
    return sum(numbers)

def main():
    no=int(input("Enter how many elements you want to add:"))
    result=Add(no)
    print("Addition of all elements:",result)  

if __name__=="__main__":
    main()