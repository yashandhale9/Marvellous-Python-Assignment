class Arithmetic:
    
    def __init(self):
        self.Ans=0
        self.Value1=0
        self.Value2=0
        
    def Accept(self):
        try:
            print("Enter value1:")
            self.Value1=int(input())
            
            print("Enter value2:")
            self.Value2=int(input())
            
        except ValueError as vobj:
            print("Exception occured due to invalid datatype:",vobj)
    
    def Addition(self):
        self.Ans=self.Value1+self.Value2
        return self.Ans
    
    def Substraction(self):
        self.Ans=self.Value1-self.Value2
        return self.Ans
    
    def Multiplication(self):
        self.Ans=self.Value1*self.Value2
        return self.Ans
    
    def Division(self):
        try:
            self.Ans=self.Value1/self.Value2
            
        except ZeroDivisionError as zobj:
            print("Exception occurs due to second value:",zobj)
        
        return self.Ans
        
def main():
    obj1=Arithmetic()
    print("In Obj1...")
    obj1.Accept()
    
    Ret=obj1.Addition()
    print("Addition is:",Ret)
    
    Ret=obj1.Substraction()
    print("Substraction is:",Ret)
    
    Ret=obj1.Multiplication()
    print("Multiplication is:",Ret)
    
    Ret=obj1.Division()
    print("Division is:",Ret)
    print("\n")
    
    obj2=Arithmetic()
    print("In Obj2...")
    obj2.Accept()
    
    Ret=obj2.Addition()
    print("Addition is:",Ret)
    
    Ret=obj2.Substraction()
    print("Substraction is:",Ret)
    
    Ret=obj2.Multiplication()
    print("Multiplication is:",Ret)
    
    Ret=obj2.Division()
    print("Division is:",Ret)
    print("\n")
    
    obj3=Arithmetic()
    print("In Obj3...")
    obj3.Accept()
    
    Ret=obj3.Addition()
    print("Addition is:",Ret)
    
    Ret=obj3.Substraction()
    print("Substraction is:",Ret)
    
    Ret=obj3.Multiplication()
    print("Multiplication is:",Ret)
    
    Ret=obj3.Division()
    print("Division is:",Ret)
    

if __name__=="__main__":
    main()