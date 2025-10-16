def Pattern(n):
    for i in range(n):
        for j in range(1,n+1):
            print("*" ,end=" ")
        print()

def main():
    num=int(input("Enter a number:"))
    Pattern(num)
    
if __name__=="__main__":
    main()
    