def CreateFile():
    fobj = open("marks.txt", 'w')
    print("Enter name and marks for 5 students:")
    
    for i in range(5):
        print(f"Enter name of student {i+1}: ")
        name = input()
        print(f"Enter marks of {name}: ")
        marks = input()
        fobj.write(f"{name} {marks}\n")
    
    fobj.close()
    print("\nFile 'marks.txt' created successfully.\n")

def DisplayScorer():
    try:
        fobj = open("marks.txt", 'r')

        print("Students who scored more than 75 marks:\n")

        for line in fobj:
            line = line.strip()
            data = line.split()

            if len(data) == 2:
                name = data[0]
                marks = data[1]

                if marks.isdigit():
                    if int(marks) > 75:
                        print(f"{name} : {marks} marks")

        fobj.close()

    except FileNotFoundError:
        print("File 'marks.txt' not found.")

def main():
    CreateFile()
    DisplayScorer()

if __name__ == "__main__":
    main()
