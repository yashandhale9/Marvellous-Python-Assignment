class Student:
    School_Name="Marvellous Infosystem School,Pune"
    
    def __init__(self,sname,rno):
        self.name=sname
        self.roll_no=rno
        
    def DisplayStudentDetails(self):
        print("School name is:",Student.School_Name)
        print("Student name is:",self.name)
        print("Student roll number is:",self.roll_no)
        
def main():
    obj1=Student("Yash",39)
    obj1.DisplayStudentDetails()
    print("\n")
    
    Student.School_Name="MIT School"
    print("After changing school name...")
    obj1.DisplayStudentDetails()

if __name__=="__main__":
    main()