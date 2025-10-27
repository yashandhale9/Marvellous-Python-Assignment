class Employee:
    def __init__(self,name,emp_id,salary):
        self.Name=name
        self.Emp_Id=emp_id
        self.Salary=salary

    def Display(self):
        print("Name of Employee:",self.Name)
        print("Employee ID:",self.Emp_Id)
        print("Employee salary:",self.Salary)

def main():
    obj1=Employee("Rohit",101,50000)
    obj1.Display()

if __name__=="__main__":
    main()