def Even(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
            
    print("Sum of even numbers between 1 to 100:",sum)
    
def main():
    Even(100)
    
if __name__=="__main__":
    main()