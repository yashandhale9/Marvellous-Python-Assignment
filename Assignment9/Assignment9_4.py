import multiprocessing
import threading
import time

def Add():
    sum=0
    for i in range(1,10000000):
        sum+=i
    print(sum)

def main():
    StartTime1=time.time()
    Add() 
    EndTime1=time.time()
    print("Time taken for execution using normal function:",EndTime1-StartTime1)
    
    StartTime2=time.time()
    Thread=threading.Thread(target=Add)
    Thread.start()
    Thread.join()
    EndTime2=time.time()
    print("Time taken for execution using threading:",EndTime2-StartTime2)
    
    StartTime3=time.time()
    P=multiprocessing.Process(target=Add)
    P.start()
    P.join()
    EndTime3=time.time()
    print("Time taken for execution using multiprocessing:",EndTime2-StartTime2)
    
    print("Exit main")
if __name__=="__main__":
    main()