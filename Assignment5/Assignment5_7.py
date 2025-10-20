def Area(l,w):
    area=l*w
    return area

def Perimeter(l,w):
    perimeter=(l+w)*2
    return perimeter

def main():
    length=float(input("Enter length of rectangle:"))
    width=float(input("Enter width of rectangle:"))
    
    result=Area(length,width)
    print("Area of rectangle is:",result)
    
    result=Perimeter(length,width)
    print("Perimeter of rectangle is:",result)

if __name__=="__main__":
    main()