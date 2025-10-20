# 🧠 Assignment 4 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 4** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **functional programming in Python** using  
**lambda**, **filter**, **map**, and **reduce**.  
The problems are designed to improve:
- 🧩 Understanding of anonymous (lambda) functions  
- 🔁 Data transformation using functional tools  
- 🧮 Combining `filter()`, `map()`, and `reduce()` effectively  
- 🧠 Logical problem-solving using compact Python expressions  

Each program is implemented in a **separate `.py` file** following the modular and functional programming principles.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Lambda function to return power of two | `Assignment4_1.py` |
| 2 | Lambda function for multiplication of two numbers | `Assignment4_2.py` |
| 3 | Use filter(), map(), and reduce() on numbers between 70 and 90 | `Assignment4_3.py` |
| 4 | Use filter(), map(), and reduce() on even numbers and find sum of squares | `Assignment4_4.py` |
| 5 | Use filter(), map(), and reduce() to process prime numbers and find maximum | `Assignment4_5.py` |

Each file:
- Defines functions cleanly  
- Accepts list or numbers from user  
- Prints all intermediate and final outputs clearly  

---

## 🧩 Problem Statements

### 1️⃣ Program 1 – Power of Two using Lambda
Write a Python program containing one **lambda function** that accepts one parameter and returns its **power of two**.

**Examples:**
Input: 4 → Output: 16

Input: 6 → Output: 64


---

### 2️⃣ Program 2 – Multiplication using Lambda
Write a Python program containing one **lambda function** that accepts two parameters and returns their **multiplication**.

**Examples:**
Input: 4 3 → Output: 12

Input: 6 3 → Output: 18


---

### 3️⃣ Program 3 – Filter, Map, Reduce (Range 70–90)
Write a Python program which uses `filter()`, `map()`, and `reduce()` on a list of numbers entered by the user.

- **Filter:** Keep only numbers ≥ 70 and ≤ 90  
- **Map:** Increase each number by 10  
- **Reduce:** Return the **product** of all mapped numbers  

**Example:**
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

List after filter = [76, 89, 86, 90, 70]

List after map = [86, 99, 96, 100, 80]

Output of reduce = 6538752000


---

### 4️⃣ Program 4 – Filter Even Numbers, Square Them, and Sum
Write a Python program which uses `filter()`, `map()`, and `reduce()`.

- **Filter:** Select only even numbers  
- **Map:** Find the square of each even number  
- **Reduce:** Return the **sum** of all squared values  

**Example:**
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

List after filter = [2, 4, 4, 2, 8, 10]

List after map = [4, 16, 16, 4, 64, 100]

Output of reduce = 204


---

### 5️⃣ Program 5 – Prime Numbers and Reduce Maximum
Write a Python program which uses `filter()`, `map()`, and `reduce()`.

- **Filter:** Keep only prime numbers  
- **Map:** Multiply each prime number by 2  
- **Reduce:** Return the **maximum number** from the resulting list  

**Example:**
Input List = [2, 70, 11, 10, 17, 23, 31, 77]

List after filter = [2, 11, 17, 23, 31]

List after map = [4, 22, 34, 46, 62]

Output of reduce = 62

---

## 🎯 Learning Outcomes
- Understood the concept of anonymous (lambda) functions in Python  
- Applied functional programming using filter(), map(), and reduce()  
- Learned how to transform and process data efficiently using built-in functions  
- Strengthened logic building with compact and expressive Python code  


---

## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment4

# Run any program
python Assignment4_1.py
python Assignment4_2.py
python Assignment4_3.py
...

📝 Notes:
Use Python 3.x or later
Each file runs independently
The functools module is used for reduce()

# Example – Assignment4_3.py
Enter list of numbers: 4 34 36 76 68 24 89 23 86 90 45 70
List after filter: [76, 89, 86, 90, 70]
List after map: [86, 99, 96, 100, 80]
Result of reduce: 6538752000
```
---
## 👨‍💻 Author
**Name:** Yash Andhale  
