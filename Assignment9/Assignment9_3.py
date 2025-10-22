import multiprocessing

def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact  
    
def main():
    data=[]
    print("Enter how many elements you wanna add ?")
    no=int(input())
    
    for i in range(no):
        print("Enter number:")
        num=int(input())
        data.append(num)
        
        result=[]
        
        p=multiprocessing.Pool()
        result=p.map(Factorial,data)
        
        p.close()
        p.join()
        
        print(result)    
        
if __name__=="__main__":
    main()