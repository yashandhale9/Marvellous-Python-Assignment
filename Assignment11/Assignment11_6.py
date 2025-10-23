sum=0
i=1
def DisplaySum(no):
    global sum,i
    if (i<=no):
        sum+=i
        i+=1
        DisplaySum(no)
    return sum

def main():
    no=int(input("Enter a number:"))
    ret=DisplaySum(no)
    
    print("Sum is:",ret)

if __name__=="__main__":
    main()