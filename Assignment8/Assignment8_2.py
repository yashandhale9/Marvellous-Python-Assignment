import threading

def EvenFactor(no):
    sum=0
    for i in range(1,no+1):
        if no % i == 0:
            if i%2==0:
                sum+=i
    print("Sum of even factors:",sum)            
            
            
def OddFactor(no):
    sum=0
    for i in range(1,no+1):
        if no%i==0:
            if i%2!=0:
                sum+=i
    print("Sum od odd factors:",sum)            
    
def main():
    evenfactor=threading.Thread(target=EvenFactor,args=(900,))
    oddfactor=threading.Thread(target=OddFactor,args=(900,))
    
    evenfactor.start()
    oddfactor.start()
    
    evenfactor.join()
    oddfactor.join()
    
    print("Exit from main")

if __name__=="__main__":
    main()