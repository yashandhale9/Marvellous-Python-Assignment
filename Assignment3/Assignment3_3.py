def Minimum(n):
    numbers=[]
    for i in range(n):
        num=int(input(f"Enter element {i+1}:"))
        numbers.append(num)
    #return min(numbers)

    MinNum=numbers[0]
    for num in numbers:
       if num<MinNum:
            MinNum=num
    return MinNum

def main():
    no=int(input("Enter how many elements you want to add:"))
    result=Minimum(no)
    
    print("Minimum number from the list is:",result)
if __name__=="__main__":
    main()