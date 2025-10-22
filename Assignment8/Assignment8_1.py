import threading

def DisplayOdd(no):
    for i in range(1,no+1):
        if(i%2!=0):
            print("Odd numbers:",i)

def DisplayEven(no):
    for i in range(1,no+1):
        if (i % 2==0):
            print("Even numbers:",i)


def main():
    Odd=threading.Thread(target=DisplayOdd,args=(10,))
    Even=threading.Thread(target=DisplayEven,args=(10,))
    
    Odd.start()
    Even.start()
    
    Odd.join()
    Even.join()
    
if __name__=="__main__":
    main()