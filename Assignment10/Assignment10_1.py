# Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input : 4     Output : 16
# Input : 6     Output : 64

power=lambda No:2**No

def main():
    Num=int(input("Enter a number:"))
    ret=power(Num)
    
    print("Power of two of",Num,"is:",ret)

if __name__=="__main__":
    main()