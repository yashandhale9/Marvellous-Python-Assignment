def LenName(name):
    print("Length of string is:",len(name))
    
def main():
    print("Enter a name:")
    result=str(input())
    LenName(result)
    
if __name__ == "__main__":
    main()