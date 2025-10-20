def TempConverter(c):
    temp=0
    temp=(c*9/5)+32
    return temp

def main():
    no=float(input("Enter temperature in celcius:"))
    result=TempConverter(no)
    
    print("Temperature in Fahrenheit:",result,)
if __name__ =="__main__":
    main()