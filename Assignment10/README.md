## 🧠 Assignment 10 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 10** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **functional programming using lambda, filter, map, and reduce** in Python.  
It helps strengthen your understanding of:

- 🧩 Anonymous (lambda) functions  
- 🔁 Data transformation with `map()` and `filter()`  
- 🧮 Aggregation and computation using `reduce()`  
- 🧠 Combining multiple functional tools to solve problems efficiently  

Each program is written in a **separate `.py` file**, following a clean and modular approach.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Lambda function to return power of two | `Assignment10_1.py` |
| 2 | Lambda function for multiplication of two numbers | `Assignment10_2.py` |
| 3 | Use filter(), map(), and reduce() on numbers between 70 and 90 | `Assignment10_3.py` |
| 4 | Use filter(), map(), and reduce() on even numbers and find sum of squares | `Assignment10_4.py` |
| 5 | Use filter(), map(), and reduce() to process prime numbers and find maximum | `Assignment10_5.py` |

Each file:
- Uses functional programming (`lambda`, `map`, `filter`, `reduce`)  
- Demonstrates step-by-step transformation of data  
- Prints intermediate and final results clearly  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Power of Two using Lambda**

Write a program containing one **lambda function** which accepts one parameter and returns the **power of two**.

**Example:**

Input: 4  
Output: 16  

Input: 6  
Output: 64  

---

### 2️⃣ **Program 2 – Multiplication using Lambda**

Write a program containing one **lambda function** which accepts two parameters and returns their **multiplication**.

**Example:**

Input: 4 3  
Output: 12  

Input: 6 3  
Output: 18  

---

### 3️⃣ **Program 3 – Filter, Map, Reduce (Range 70–90)**

Write a program using `filter()`, `map()`, and `reduce()` on a list of numbers entered by the user.  
- **Filter:** Keep only numbers between 70 and 90 (inclusive)  
- **Map:** Add 10 to each number  
- **Reduce:** Return the **product** of all mapped numbers  

**Example:**

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

List after filter = [76, 89, 86, 90, 70]

List after map = [86, 99, 96, 100, 80]

Output of reduce = 6538752000


---

### 4️⃣ **Program 4 – Filter Even Numbers, Square Them, and Sum**

Write a program using `filter()`, `map()`, and `reduce()` on a list of numbers entered by the user.  
- **Filter:** Keep only even numbers  
- **Map:** Calculate the square of each number  
- **Reduce:** Return the **sum** of all squares  

**Example:**

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

List after filter = [2, 4, 4, 2, 8, 10]

List after map = [4, 16, 16, 4, 64, 100]

Output of reduce = 204


---

### 5️⃣ **Program 5 – Prime Numbers using Filter, Map, Reduce**

Write a Python program which uses `filter()`, `map()`, and `reduce()` to:  
- **Filter:** Keep only prime numbers from the list  
- **Map:** Multiply each prime number by 2  
- **Reduce:** Return the **maximum number** from the list  

**Example:**

Input List = [2, 70, 11, 10, 17, 23, 31, 77]

List after filter = [2, 11, 17, 23, 31]

List after map = [4, 22, 34, 46, 62]

Output of reduce = 62


---

## 📝 Notes

- Use Python 3.x or later  
- Import `functools` for `reduce()`  
- Each function (`filter`, `map`, `reduce`) should be demonstrated clearly  

---

## 🎯 Learning Outcomes

- Learned how to define and use **lambda functions**  
- Practiced **filtering, mapping, and reducing** data with Python built-ins  
- Gained hands-on experience in **functional programming**  
- Understood how to apply functional tools for real-world logic problems  
- Improved efficiency through concise coding techniques  

---

## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment10

# Run any program
python Assignment10_1.py
python Assignment10_2.py
python Assignment10_3.py
...

🧪 Sample Execution
# Example – Assignment10_3.py
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000

```
---

**👨‍💻 Author**

Yash Andhale

