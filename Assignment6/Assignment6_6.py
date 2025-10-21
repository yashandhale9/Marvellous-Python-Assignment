def Pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()

def main():
    no=int(input("Enter a number:"))
    Pattern(no)
if __name__=="__main__":
    main()