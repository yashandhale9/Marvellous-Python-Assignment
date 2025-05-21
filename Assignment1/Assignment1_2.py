def ChkNum(number):
    if number % 2==0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter a number:")
    num=int(input())
    ChkNum(num)

if __name__ == "__main__":
    main()