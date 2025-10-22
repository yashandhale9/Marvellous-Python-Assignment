import threading
import time 

def Display1(no):
    for i in range(1,no+1):
        print(i)
        time.sleep(1.0)
        
def Display2(no):
    for i in range(1,no+1):
        print(i)
        time.sleep(1.0)
        
def Display3(no):
    for i in range(1,no+1):
        print(i)
        time.sleep(1.0)
               

def main():
    t1=threading.Thread(target=Display1,args=(5,))
    t2=threading.Thread(target=Display2,args=(5,))
    t3=threading.Thread(target=Display3,args=(5,))

    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
        
if __name__=="__main__":
    main()