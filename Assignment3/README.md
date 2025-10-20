# 🧠 Assignment 3 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 3** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **list data structures**, **loops**, and **modular programming**.  
The problems are designed to improve understanding of:
- 📋 List creation and traversal  
- 🔢 Number manipulation using loops  
- 🧩 Functions and modularity  
- 🧮 Practical problem-solving using Python logic  

Each program is implemented in an **independent `.py` file** with a clean, function-based approach.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Accept N numbers, store in list, and return addition of all elements | `Assignment3_1.py` |
| 2 | Accept N numbers, store in list, and return maximum number | `Assignment3_2.py` |
| 3 | Accept N numbers, store in list, and return minimum number | `Assignment3_3.py` |
| 4 | Accept N numbers and one element, return its frequency from list | `Assignment3_4.py` |
| 5 | Accept N numbers, return addition of all prime numbers (using module) | `Assignment3_5.py` |

Each file:
- Uses proper input handling  
- Defines logic inside a function  
- Displays the final output clearly on console  


---

## 🧩 Problem Statements

### 1️⃣ Program 1 – Addition of List Elements
Write a program that accepts `N` numbers from the user, stores them in a list,  
and returns the **addition of all elements**.

**Example:**
Input:
Number of elements: 6

Input Elements: 13 5 45 7 4 56

Output: 130


---

### 2️⃣ Program 2 – Maximum Number in List
Write a program that accepts `N` numbers from the user, stores them in a list,  
and returns the **maximum number**.

**Example:**
Input:
Number of elements: 7

Input Elements: 13 5 45 7 4 56 34

Output: 56


---

### 3️⃣ Program 3 – Minimum Number in List
Write a program that accepts `N` numbers from the user, stores them in a list,  
and returns the **minimum number**.

**Example:**
Input:
Number of elements: 4

Input Elements: 13 5 45 7

Output: 5


---

### 4️⃣ Program 4 – Frequency of Element
Write a program that accepts `N` numbers from the user, stores them in a list,  
then accepts one more number and returns its **frequency** in that list.

**Example:**
Input:
Number of elements: 11

Input Elements: 13 5 45 7 4 56 5 34 2 5 65

Element to search: 5

Output: 3


---

### 5️⃣ Program 5 – Addition of Prime Numbers
Write a program that accepts `N` numbers from the user, stores them in a list,  
and returns the **addition of all prime numbers** from that list.

Create a user-defined module named **`MarvellousNum`** containing function:
- `ChkPrime(num)` → Returns `True` if number is prime, otherwise `False`.

The main file should include function:
- `ListPrime()` → Calls `ChkPrime()` for each element and sums the prime numbers.

**Example:**
Input:
Number of elements: 11

Input Elements: 13 5 45 7 4 56 10 34 2 5 8

Output: 54 (13 + 5 + 7 + 2 + 5)


## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment3

# Run any program
python Assignment3_1.py
python Assignment3_2.py
python Assignment3_3.py
...

📝 Notes:

Use Python 3.x or later
Each file is independent
Program 5 requires an external module MarvellousNum.py in the same directory

# Example – Assignment3_1.py
Enter number of elements: 6
Input elements: 13 5 45 7 4 56
Addition of all elements is: 130

