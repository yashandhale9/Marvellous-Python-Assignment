import multiprocessing

def Fun(n):
    return n*n

def main():
    data=[]
    
    print("How many elements you wanna add ?")
    no=int(input())
    
    for i in range(no):
        print("Enter number:")
        num=int(input())
        data.append(num)
        
        result=[]
        
        p=multiprocessing.Pool()
        result=p.map(Fun,data)
        
        p.close()
        p.join()
        
        print(result)

if __name__=="__main__":
    main()