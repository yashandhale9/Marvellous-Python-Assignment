class Person():
    def __init__(self,pName,pAge):
        self.name=pName
        self.age=pAge
        
class Teacher(Person):
    def __init__(self,pName,pAge,tSubject,tSalary):
        super().__init__(pName,pAge)
        self.subject=tSubject
        self.salary=tSalary
        
    def Display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Subject",self.subject)
        print("Salary:",self.salary)
        
def main():
    Teacher_Name=input("Enter teacher name:")
    Teacher_Age=int(input("Enter teacher age:"))
    Teacher_Subject=input("Enter teacher subject:")
    Teacher_Salary=float(input("Enter teacher salary:"))
    
    obj1=Teacher(Teacher_Name,Teacher_Age,Teacher_Subject,Teacher_Salary)
    obj1.Display()

if __name__=="__main__":
    main()