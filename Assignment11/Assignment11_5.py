count = 0

def CountZero(no):
    global count
    if no == 0:
        return count

    digit = no % 10
    if digit == 0:
        count += 1

    no = no // 10
    CountZero(no)
    return count

def main():
    no = int(input("Enter a number: "))
    ret = CountZero(no)
    print("Zero count:", ret)

if __name__ == "__main__":
    main()
