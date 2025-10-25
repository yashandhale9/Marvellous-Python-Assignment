# 🧠 Assignment 12 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 12** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **Object-Oriented Programming (OOP)** concepts in Python.  
You will learn how to define classes, use instance and class variables, and work with multiple objects.  

Key concepts covered:
- 🧩 Class and Object creation  
- 🧮 Instance vs Class variables  
- ⚙️ Method definitions and `__init__()` constructor  
- 🔁 Object manipulation and method calls  
- 💡 Code modularity using class-based design  

Each program is implemented in a **separate `.py` file** with clear structure and clean logic.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Class `Demo` with instance and class variables, and two methods (`Fun`, `Gun`) | `Assignment12_1.py` |
| 2 | Class `Circle` with methods for area and circumference calculation | `Assignment12_2.py` |
| 3 | Class `Arithmetic` performing addition, subtraction, multiplication, and division | `Assignment12_3.py` |

Each file:
- Defines a class with data and behavior  
- Demonstrates instance and class-level data  
- Accepts input and displays formatted output  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Class Demo**

Write a program which contains one class named **Demo**.  
- The class contains two **instance variables**: `no1`, `no2`  
- One **class variable**: `Value`  
- Two **methods**: `Fun()` and `Gun()` to display instance variables  

**Initialize instance variables** in the `__init__()` method by accepting values from the user.

**Example:**
```python
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
```
---
### 2️⃣ **Program 2 – Class Circle**

Write a program which contains one class named **Circle.**

Instance variables: Radius, Area, Circumference

Class variable: PI = 3.14

**Methods:**

**Accept()** → Accepts radius from user

**CalculateArea()** → Calculates and stores area

**CalculateCircumference()** → Calculates and stores circumference

**Display()** → Displays radius, area, and circumference

**Example:**

Enter radius: 5  

Area of circle: 78.5 

Circumference of circle: 31.4

---
## 3️⃣ **Program 3 – Class Arithmetic**

Write a program which contains one class named **Arithmetic.**

Instance variables: Value1, Value2

**Methods:**

**Accept()** → Accepts two numbers from user

**Addition()** → Returns sum

**Subtraction()** → Returns difference

**Multiplication()** → Returns product

**Division()** → Returns quotient

**Example:**

Enter first number: 20  
Enter second number: 10  
Addition is: 30  
Subtraction is: 10  
Multiplication is: 200  
Division is: 2.0

---
**📝 Notes**

Use Python 3.x or later

Use class variables for shared data (PI, Value)

Use instance variables for object-specific data

Create multiple objects to test your class methods

---
**🎯 Learning Outcomes**

Understood the difference between instance and class variables

Learned how to design and use constructors (__init__)

Practiced encapsulation using class-based structure

Implemented basic OOP principles like data abstraction and modularity

Strengthened Python OOP foundation for future assignments

---
## ⚙️ **How to Run Programs**
```
# Navigate to this folder
cd Assignment12

# Run any program
python Assignment12_1.py
python Assignment12_2.py
python Assignment12_3.py

🧪Sample Execution:

# Example – Assignment12_2.py
Enter radius: 5
Area of circle: 78.5
Circumference of circle: 31.4
```
---

**👨‍💻 Author**

Yash Andhale

---
