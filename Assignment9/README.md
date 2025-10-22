# 🧠 Assignment 9 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 9** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **multithreading and multiprocessing** concepts in Python.  
The programs demonstrate:
- ⚙️ Creating and managing multiple threads  
- 💻 Using multiprocessing for parallel execution  
- 🧮 Performance comparison between threading, multiprocessing, and sequential execution  
- ⏱ Measuring and comparing execution time  
- 🧩 Understanding process pools and CPU parallelism  

Each problem is implemented in a **separate `.py` file** with proper structure and clear output.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Create 3 threads that print numbers 1–5 with 1-second delay | `Assignment9_1.py` |
| 2 | Square numbers using multiprocessing | `Assignment9_2.py` |
| 3 | Compute factorial using multiprocessing Pool | `Assignment9_3.py` |
| 4 | Compare execution time of normal, threading, and multiprocessing approaches | `Assignment9_4.py` |

Each file:
- Uses either **threading** or **multiprocessing** modules  
- Displays results and timing output clearly  
- Includes proper synchronization where required  

---

## 🧩 Problem Statements

### 1️⃣ Program 1 – Threads Printing Numbers
Create a Python program that starts **3 threads**,  
each printing numbers from **1 to 5** with a **delay of 1 second**.

**Example Output:**

Thread-1: 1

Thread-1: 2

...

Thread-3: 5


---

### 2️⃣ Program 2 – Square Numbers using Multiprocessing
Write a Python program using `multiprocessing.Process`  
to **square a list of numbers** using multiple processes.

**Example:**

Input List: [1, 2, 3, 4, 5]

Output: [1, 4, 9, 16, 25]


---

### 3️⃣ Program 3 – Factorial using Multiprocessing Pool
Create a Python program that uses `multiprocessing.Pool`  
to compute **factorials of numbers** from a given list.

**Example:**

Input List: [3, 5, 7]

Output: [6, 120, 5040]


---

### 4️⃣ Program 4 – Compare Execution Time
Create a Python program to compare execution time of summing  
numbers from **1 to 10 million** using:
- Normal function  
- Threading  
- Multiprocessing  

Display the total time taken by each method.

**Expected Output:**

Normal Function Time: 2.35 seconds

Threading Time: 1.74 seconds

Multiprocessing Time: 0.98 seconds


---

**📝 Notes:**

Use Python 3.x or later  
Import `time`, `threading`, and `multiprocessing` modules  
Ensure proper use of `start()` and `join()` for threads and processes  

---

**🎯 Learning Outcomes**

- Understood difference between **threads** and **processes**  
- Learned to create and manage multiple threads and processes  
- Implemented **parallel computing** to improve performance  
- Compared real execution time for different approaches  
- Strengthened understanding of **concurrency and CPU utilization**  

---

## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment9

# Run any program
python Assignment9_1.py
python Assignment9_2.py
python Assignment9_3.py
...

🧪 Sample Execution
# Example – Assignment9_3.py
Input List: [3, 5, 7]
Output: [6, 120, 5040]
```
---
**👨‍💻 Author**

Yash Andhale
