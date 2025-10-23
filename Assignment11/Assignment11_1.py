i=1

def Display(no):
    global i
    if(i<=5):
        print(i,end=" ")
        i+=1
        Display(no)

def main():
    print("Enter a number:")
    n=int(input())
    
    Display(n)

if __name__=="__main__":
    main()