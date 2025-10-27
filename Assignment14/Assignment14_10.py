class Employee:
    def __init__(self, emp_name, emp_salary, emp_dept):
        self.name = emp_name            # Public 
        self._salary = emp_salary       # Protected 
        self.__department = emp_dept    # Private 
        
    def display(self):
        print("Name:",self.name)
        print("Salary: ",self._salary)
        print("Department: ",self.__department)


def main():
    obj1= Employee("Yash", 50000, "IT")

    print("Accesing from inside class..")
    obj1.display()
    
    print("\nAccessing from outside class:")
    print("Name:", obj1.name)          # Public is  allowed
    print("Salary:", obj1._salary)     # Protected is allowed pan recomend nahi

   #private acceesing error yeil
    try:
        print("Department:", obj1.__department)  # Private allowed nahi
    except:
        print("Cannot access __department directly!")

if __name__ == "__main__":
    main()
