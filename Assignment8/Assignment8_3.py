import threading

def EvenListAddition(no):
    sum=0
    for i in no:
        if i%2==0:
            sum+=i
    print("Sum of even numbers:",sum)

def OddListAddition(no):
    sum=0
    for i in no:
      if i%2!=0:
          sum+=i 
    print("Sum of odd numbers:",sum) 

def main():
    no=int(input("How many elements you want to add ?"))
    data=[]
    
    for i in range(no):
        num=int(input("Enter number:"))
        data.append(num)

    EvenList=threading.Thread(target=EvenListAddition,args=(data,))
    OddList=threading.Thread(target=OddListAddition,args=(data,))
    
    EvenList.start()
    OddList.start()
    
    EvenList.join()
    OddList.join()
    
if __name__=="__main__":
    main()