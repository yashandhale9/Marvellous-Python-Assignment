PowerOfTwo = lambda No: 2 ** No

def main():
    number = int(input("Enter a number: "))
    result = PowerOfTwo(number)
    print(f"Power of two of {number} is:", result)
    
if __name__ == "__main__":
    main()
