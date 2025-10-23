def Power(b,x):
    if x ==0:
        return 1
    
    else:
        return b * Power(b, x - 1)
    
def main():
    Base=int(input("Enter base:"))
    Expo=int(input("Enter exponential:"))
    
    ret=Power(Base,Expo)
    
    print("Result is:",ret)

if __name__=="__main__":
    main()