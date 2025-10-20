def ChkAge(age):
    if age>=18:
        return True
    else:
        return False

def main():
    no=int(input("Enter age:"))
    result=ChkAge(no)

    if result==True:
        print("Eligible to vote")
        
    else:
        print("Not eligible to vote")
if __name__=="__main__":
    main()