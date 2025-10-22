import threading 

def DisplayThread1(no):
    print("Displaying thread1...")
    for i in range(1,no+1):
        print(i)
        
def displayThread2(no):
    print("Displaying thread2...")
    for i in range(50,0,-1):
        print(i)
        

def DisplayThread2(no):
    pass      

def main():
    thread1=threading.Thread(target=DisplayThread1,args=(50,))
    thread2=threading.Thread(target=DisplayThread2,args=(50,))
    
    thread1.start()
    thread1.join()
    
    thread2.start()
    thread1.join()

if __name__=="__main__":
    main()