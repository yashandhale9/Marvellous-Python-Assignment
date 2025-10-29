def main():
    fobj=open("student.txt",'w')
    
    print("Enter name of 5 students:")
    for i in range(5):
        print(f"Enter name of student{i+1}")
        name=input()
        fobj.write(name+"\n")
        
    fobj.close()
        
    print("Name written successfulyy")

if __name__=="__main__":
    main()