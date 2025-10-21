def Pallindrome(Input):
    originalLength = len(Input)

    for i in range(len(Input) // 2):
        if Input[i] != Input[originalLength - i - 1]:
            return False

    return True

def main():

    str = input("Enter the string : ")

    ret = Pallindrome(str)

    if(ret == True):
        print(str," is a pallindrome ")
    else:
        print("string is not pallindrome ")

if __name__ == "__main__":
    main()