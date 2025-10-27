class Book:
    def __init__(self):
        self.__price=0
        
    def set(self,bPrice):
        self.__price=bPrice
    
    def get(self):
        return self.__price

def main():
    obj1=Book()
    
    obj1.set(101)
    
    ret=obj1.get()
    print("Book price is:",ret)

if __name__=="__main__":
    main()