import threading

def DisplaySmall(str):
    count=0
    for i in range(len(str)):
        ch=str[i]
        if (ch>='a' and ch<='z'):
            count+=1
    print("Small letters:",count)
    print("Id is:",threading.get_ident())
    print("Thread name:",threading.current_thread().name)
    
def DisplayCapital(str):
    count=0
    for i in range(len(str)):
        ch=str[i]
        if (ch>='A' and ch<='Z'):
            count+=1
    print("capital letters:",count)
    print("Id is:",threading.get_ident())
    print("Thread name:",threading.current_thread().name)
    
def DisplayDigit(str):
    count=0
    for i in range(len(str)):
        ch=str[i]
        if (ch>='0' and ch<='9'):
            count+=1
    print("Digit count:",count)
    print("Id is:",threading.get_ident())
    print("Thread name:",threading.current_thread().name)

def main():
    
    str=input("Enter a string:")
    
    small=threading.Thread(target=DisplaySmall,args=(str,))
    capital=threading.Thread(target=DisplayCapital,args=(str,))
    digit=threading.Thread(target=DisplayDigit,args=(str,))
    
    small.start()
    capital.start()
    digit.start()
    
    small.join()
    capital.join()
    digit.join()

if __name__=="__main__":
    main()