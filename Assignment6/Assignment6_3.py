def Table(n):
    for i in range(1,11):
        print(f"{n}*{i}=",n*i)
        i+=n

def main():
    no=int(input("Enter a number:"))
    Table(no)

if __name__=="__main__":
    main()