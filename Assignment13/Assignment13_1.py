class BookStore:
    NoOfBooks=0
    
    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        BookStore.NoOfBooks=BookStore.NoOfBooks+1
        
    def Display(self):
        print(self.Name,"by",self.Author,".","No of books:",BookStore.NoOfBooks)   

def main():
    print("Object 1 called...")
    obj1=BookStore("Linux System programming","Robert Love")
    obj1.Display()
    
    print("Object 2 called.....")
    obj2=BookStore("C Programming","Dennis Ritchie")
    obj2.Display()
    

if __name__=="__main__":
    main()