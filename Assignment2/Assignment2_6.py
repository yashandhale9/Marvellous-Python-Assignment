def Pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()
def main():
    num=int(input("Enter a number:"))
    Pattern(num)
    
if __name__=="__main__":
    main()
    