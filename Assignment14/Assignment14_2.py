class Rectangle():
    def __init__(self,l,w):
        self.length=l
        self.width=w

    def Area(self):
        area=0.0
        area=self.length*self.width
        return area
    
    def Perimeter(self):
        perimeter=0.0
        perimeter=2*(self.length+self.width)
        return perimeter
        
def main():
    length=float(input("Enter length:"))
    width=float(input("Enter width:"))
    
    obj1=Rectangle(length,width)
    
    ret=obj1.Area()
    print("Area of Rectangle:",ret)
    
    ret=obj1.Perimeter()
    print("Perimeter of Rectangle:",ret)

if __name__=="__main__":
    main()