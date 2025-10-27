# 🧠 Assignment 14 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 14** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **Object-Oriented Programming (OOP)** concepts like  
**Encapsulation, Inheritance, Method Overriding, and Operator Overloading**.  
You’ll learn how to design, derive, and manipulate classes to build real-world models.

Key concepts covered:
- 🧩 Class creation and object instantiation  
- 💼 Encapsulation and access modifiers  
- 🧮 Method overloading and overriding  
- ⚙️ Use of `super()` and constructor chaining  
- 🔢 Operator overloading and object comparison  

Each program is implemented in an independent `.py` file using clean, modular, and structured code.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Class `Employee` – Display employee details | `Assignment14_1.py` |
| 2 | Class `Rectangle` – Compute area and perimeter | `Assignment14_2.py` |
| 3 | Class `Book` – Demonstrate encapsulation with private variable | `Assignment14_3.py` |
| 4 | Class `Student` – Use class variable `school_name` | `Assignment14_4.py` |
| 5 | Class `BankAccount` – Deposit, withdraw, and display balance | `Assignment14_5.py` |
| 6 | Class `Calculator` – Perform basic arithmetic operations | `Assignment14_6.py` |
| 7 | Class `Person` and `Teacher` – Demonstrate inheritance and `super()` | `Assignment14_7.py` |
| 8 | Class `Vehicle` and `Car` – Demonstrate method overriding | `Assignment14_8.py` |
| 9 | Class `Product` – Implement `__eq__()` to compare prices | `Assignment14_9.py` |
| 10 | Class `Employee` – Demonstrate private, protected, and public variables | `Assignment14_10.py` |

Each file:
- Implements one OOP concept clearly  
- Uses constructors and proper encapsulation  
- Demonstrates input/output for easy understanding  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Class Employee**
Create a class `Employee` with attributes `name`, `emp_id`, and `salary`.  
Create multiple objects and print their details using a display method.

**Example:**
Name: Rohit, ID: 101, Salary: 50000


---

### 2️⃣ **Program 2 – Class Rectangle**
Create a class `Rectangle` with `length` and `width`.  
Add methods to compute **area** and **perimeter**.

**Expected Output:**

Area: 50

Perimeter: 30


---

### 3️⃣ **Program 3 – Class Book (Encapsulation)**
Create a class `Book` with a **private attribute** `__price`.  
Add `get_price()` and `set_price()` methods to show encapsulation.

**Example:**

Book Price: 500

Updated Price: 650


---

### 4️⃣ **Program 4 – Class Student with Class Variable**
Create a class `Student` with attributes `name`, `roll_no`, and a **class variable** `school_name`.  
Print student details and change the school name using the class name.

**Example:**

Student Name: Yash

Roll No: 15

School Name: Marvellous High School


---

### 5️⃣ **Program 5 – Class BankAccount**
Create a class `BankAccount` with attributes `account_number`, `name`, and `balance`.  
Use `__init__()` and define methods for **deposit**, **withdraw**, and **display balance**.

**Example:**

Account No: 101

Name: Rohit

Balance: 5000

Deposit: +2000 → Balance: 7000


---

### 6️⃣ **Program 6 – Class Calculator**
Create a class `Calculator` with methods for **add**, **subtract**, **multiply**, and **divide**.  
Accept user input for values and call methods accordingly.

**Example:**

Enter first number: 10

Enter second number: 5

Addition: 15

Subtraction: 5

Multiplication: 50

Division: 2.0


---

### 7️⃣ **Program 7 – Inheritance using Person and Teacher**
Create a base class `Person` with `name` and `age`.  
Derive class `Teacher` with `subject` and `salary`.  
Use `super()` to call the base class constructor and display both.

**Example:**

Name: Piyush

Age: 35

Subject: Python

Salary: 75000


---

### 8️⃣ **Program 8 – Method Overriding (Vehicle → Car)**
Create a base class `Vehicle` with a method `start()`.  
Derive class `Car` and override the method `start()` to add additional behavior.

**Example:**

Vehicle starting...

Car started with keyless ignition.

Withdraw: -1000 → Balance: 6000


---

### 9️⃣ **Program 9 – Operator Overloading (__eq__)**
Create a class `Product` with attributes `name` and `price`.  
Implement `__eq__()` to compare two products by their price.

**Example:**

Product A and Product B have the same price.


---

### 🔟 **Program 10 – Access Modifiers Demonstration**
Create a class `Employee` with attributes:  
- `__salary` (private)  
- `_department` (protected)  
- `name` (public)  

Demonstrate how each access modifier behaves inside and outside the class.

**Example:**

Name: Yash

Department: HR

Salary: 60000


---

## 📝 Notes

- Use Python 3.x or later  
- Demonstrate proper use of OOP principles  
- Encapsulation → Private/Protected/Public  
- Inheritance → `super()` keyword  
- Operator overloading → `__eq__()`  

---

## 🎯 Learning Outcomes

- Strengthened understanding of **Object-Oriented Programming**  
- Practiced **Encapsulation**, **Inheritance**, and **Polymorphism**  
- Learned how to override and overload methods  
- Understood **access modifiers** in Python (`public`, `protected`, `private`)  
- Improved ability to design modular, reusable class-based programs  

---

## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment14

# Run any program
python Assignment14_1.py
python Assignment14_2.py
python Assignment14_3.py
...

Sample Execution:

# Example – Assignment14_7.py
Name: Piyush
Age: 35
Subject: Python
Salary: 75000
```
---
**👨‍💻 Author**

Yash Andhale

---
