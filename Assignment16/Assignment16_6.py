def CopyFile(SourceFile, DestinationFile):
    try:
        fsrc = open(SourceFile, 'r')
        data = fsrc.read()
        fsrc.close()

        fdest = open(DestinationFile, 'w')
        fdest.write(data)
        fdest.close()

        print(f"Content copied from '{SourceFile}' to '{DestinationFile}' successfully.")

    except FileNotFoundError:
        print("File does not exist.")

def main():
    print("Enter the source file name: ")
    Source=input()
    print("Enter the destination file name: ")
    Destination=input()
    
    CopyFile(Source, Destination)

if __name__ == "__main__":
    main()
