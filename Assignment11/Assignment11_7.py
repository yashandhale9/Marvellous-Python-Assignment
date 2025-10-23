i = 1
j = 1

def PrintPattern(no):
    global i, j

    if i <= no:
        if j <= i:
            print("*", end=" ")
            j += 1
            PrintPattern(no)
        else:
            print()
            i += 1
            j = 1
            PrintPattern(no)

def main():
    no = int(input("Enter a number: "))
    PrintPattern(no)

if __name__ == "__main__":
    main()
