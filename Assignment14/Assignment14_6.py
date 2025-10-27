class Calculator():
    pass

    def __init__(self,No1,No2):
        self.Value1=No1
        self.Value2=No2
        
    def Add(self):
        return (self.Value1+self.Value2)
    
    def Subtract(self):
        return (self.Value1-self.Value2)
    
    def Multiply(self):
        return (self.Value1*self.Value2)
    
    def Divide(self):
        return (self.Value1/self.Value2)
    
def main():
    Value1=float(input("Enter first value:"))
    Value2=float(input("Enter second value:"))
    
    obj1=Calculator(Value1,Value2)
    
    ret=obj1.Add()
    print("Addition is:",ret)
    
    ret=obj1.Subtract()
    print("Subtraction is:",ret)
    
    ret=obj1.Multiply()
    print("Multiplication is:",ret)
    
    ret=obj1.Divide()
    print("Division is:",ret)

if __name__=="__main__":
    main()