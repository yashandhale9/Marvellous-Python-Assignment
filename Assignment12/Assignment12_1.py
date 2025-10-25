class Demo:
    
    def __init__(self,Num1,Num2):
        self.No1=Num1
        self.No2=Num2
        
    def Fun(self):
        print("Inside Fun...")
        print("Value of No1:",self.No1)
        print("Value of No2:",self.No2)
        
    def Gun(self):
        print("Inside Gun....")
        print("Value of No1:",self.No1)
        print("Value of No2:",self.No2)
        
def main():
    obj1=Demo(11,21)
    obj2=Demo(51,101)
    
    obj1.Fun()
    obj2.Fun()
    
    obj1.Gun()
    obj2.Gun()

if __name__=="__main__":
    main()