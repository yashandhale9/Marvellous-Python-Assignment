# 🧠 Assignment 13 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 13** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **advanced Object-Oriented Programming (OOP)** concepts in Python.  
It helps strengthen your understanding of:
- 🧩 Class and object creation  
- ⚙️ Instance and class variables  
- 💰 Banking and interest calculation using OOP principles  
- 🔢 Number processing using class methods  
- 💡 Reusability and modular program design  

Each program is implemented in a **separate `.py` file**, following a clean, structured, and modular approach.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Class `BookStore` – Tracks books, authors, and total number of books | `Assignment13_1.py` |
| 2 | Class `BankAccount` – Deposit, withdraw, and calculate interest | `Assignment13_2.py` |
| 3 | Class `Numbers` – Check prime, perfect, factors, and sum of factors | `Assignment13_3.py` |

Each file:
- Defines a Python class with proper encapsulation  
- Uses constructors (`__init__`) and class variables  
- Displays results using instance methods  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Class BookStore**

Write a program which contains one class named **BookStore**.  

**Description:**
- Instance variables: `Name`, `Author`  
- Class variable: `NoOfBooks` (initialized to 0)  
- Methods:  
  - `__init__()` → Accepts book name and author, increments `NoOfBooks`  
  - `Display()` → Displays book details and total count  

**Example:**
```python
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()  # Linux System Programming by Robert Love. No of books: 1

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()  # C Programming by Dennis Ritchie. No of books: 2
```
---
## 2️⃣ **Program 2 – Class BankAccount**

Write a program which contains one class named **BankAccount.**

**Description:**

Instance variables: Name, Amount

Class variable: ROI = 10.5 (Rate of Interest)

**Methods:**

__init__() → Initializes name and amount

Display() → Displays name and balance

Deposit() → Accepts amount and adds to balance

Withdraw() → Accepts amount and deducts from balance

CalculateInterest() → Calculates and displays interest based on balance and ROI

**Example:**

Enter Name: Yash

Enter Initial Amount: 10000

Deposit Amount: 5000

Withdraw Amount: 2000

Interest: 1575.0

Final Balance: 13000

---

## 3️⃣ **Program 3 – Class Numbers**

Write a program which contains one class named **Numbers.**

**Description:**

Instance variable: Value

**Methods:**

ChkPrime() → Returns True if the number is prime, else False

ChkPerfect() → Returns True if the number is perfect, else False

Factors() → Displays all factors of the number

SumFactors() → Returns the sum of all factors

**Example:**

Enter number: 28  
Factors: 1 2 4 7 14  
Sum of factors: 28  
28 is a Perfect Number  
28 is not a Prime Number

---

**📝 Notes**

Use Python 3.x or later

Use self for instance variable access

Use class variables for shared data (e.g., interest rate or book count)

Create multiple objects to test methods

---

**🎯 Learning Outcomes**

Strengthened understanding of classes and objects in Python

Learned use of constructors, instance variables, and class variables

Practiced writing banking and number-based logic using OOP principles

Understood how to organize code modularly with methods and attributes

Enhanced ability to design and use real-world object-oriented models

---

## ⚙️ **How to Run Programs**
```
Navigate to this folder
cd Assignment13

Run any program
python Assignment13_1.py
python Assignment13_2.py
python Assignment13_3.py

🧪 Sample Execution:

Example – Assignment13_1.py
Linux System Programming by Robert Love. No of books: 1
C Programming by Dennis Ritchie. No of books: 2
```
---

**👨‍💻 Author**

Yash Andhale

---

