class Arithmetic:
    def __init__(self,aValue):
        self.Value=aValue
        
    def ChkPrime(self):
        if(self.Value<=1):
            return False
        for i in range(2,self.Value):
            if(self.Value %i ==0):
                return False
        return True
    
    def ChkPerfect(self):
        
        Sum=0
        for i in range(1,self.Value):
            if(self.Value%i==0):
                Sum+=i
        
        if(Sum==self.Value):
            return True
        else:
            return False
    
    def SumFactors(self):
        Sum =0
        for i in range(1,self.Value):
            if(self.Value%i==0):
                Sum+=i
                
        return Sum
    
    def Factors(self):
        for i in range(1,self.Value):
            if(self.Value%i==0):
                print("Factors are:",i)
    
def main():
    Num1=int(input("Enter a value:"))
    obj1=Arithmetic(Num1)
    
    ret=obj1.ChkPrime()
    if(ret):
        print("Number is prime")
    else:
        print("Number is not prime")
        
    ret=obj1.ChkPerfect()
    if(ret):
        print("Number is perfect")
    else:
        print("Number is not perfect")
        
    ret=obj1.SumFactors()
    print("Sum of factors is:",ret)
    
    obj1.Factors() 
    print("-----------------")
    
    Num2=int(input("Enter a value:"))
    obj2=Arithmetic(Num2)
    
    ret=obj2.ChkPrime()
    if(ret):
        print("Number is prime")
    else:
        print("Number is not prime")
        
    ret=obj2.ChkPerfect()
    if(ret):
        print("Number is perfect")
    else:
        print("Number is not perfect")
        
    ret=obj2.SumFactors()
    print("Sum of factors is:",ret)
    
    obj2.Factors()  

if __name__=="__main__":
    main()