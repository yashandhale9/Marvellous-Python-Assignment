def Maximum(n):
    numbers=[]
    for i in range(n):
        num=int(input(f"Enter element {i+1}:"))
        numbers.append(num)
    return max(numbers)

#   MaxN=numbers[0]
#    for num in numbers:
#       if num>MaxN:
#            MaxN=num
#   return MaxN

def main():
    no=int(input("Enter how many elements you want to add:"))
    result=Maximum(no)
    
    print("Maximum number from the list is:",result)
if __name__=="__main__":
    main()