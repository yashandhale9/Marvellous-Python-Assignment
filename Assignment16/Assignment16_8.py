def RemoveBlankLines(source_file, destination_file):
    try:
        sobj=open(source_file, 'r') 
        dobj=open(destination_file, 'w')
        for line in sobj:
                if line.strip(): 
                    dobj.write(line)
        print(f"Blank lines removed successfully.")
        
    except FileNotFoundError:
        print("The file does not exist.")

def main():
    print("Enter the source file name: ")
    source = input()
    print("Enter the destination file name: ")
    destination = input()
    
    RemoveBlankLines(source, destination)

if __name__ == "__main__":
    main()
