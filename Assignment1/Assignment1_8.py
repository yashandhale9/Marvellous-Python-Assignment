def Stars(count):
    for i in range(count):
        print("*")

def main():
    print("Enter a number:")
    number=int(input())
    Stars(number)
    
if __name__ == "__main__":
    main()