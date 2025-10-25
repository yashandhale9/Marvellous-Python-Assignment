class Circle:
    
    PI=3.14   #class variable
    
    def __init__(self):
         self.Radius=0.0
         self.Area=0.0
         self.Circumeference=0.0
      
    def Accept(self):
        print("Enter radius of a circle:")
        self.Radius=int(input())
        
    def CalculateArea(self):
        self.Area=Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumeference=2*Circle.PI*self.Radius
    
    def Display(self):
        print("Radius of Circle is:",self.Radius)
        print("Area of circle is:",self.Area)
        print("Circumference of circle is:",self.Circumeference)

def main():
    obj1=Circle()
    
    print("Values for obj1.......")
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()
    print("\n")
    
    obj2=Circle()
    
    print("Values for obj2.......")
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()
    print("\n")
    
    obj3=Circle()
    
    print("Values for obj3.......")
    obj3.Accept()
    obj3.CalculateArea()
    obj3.CalculateCircumference()
    obj3.Display()

if __name__=="__main__":
    main()