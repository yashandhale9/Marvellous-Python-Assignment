# 🧠 Assignment 8 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 8** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **multithreading concepts in Python**.  
The programs are designed to help understand:
- ⚙️ Creating and managing threads  
- 🔁 Synchronizing multiple threads  
- 🧮 Performing parallel computations  
- 🔤 Handling threads with string and numeric data  
- 🧠 Coordination between threads and the main program  

Each problem is implemented in a **separate `.py` file** using the `threading` module in Python.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Display first 10 even and odd numbers using two threads | `Assignment8_1.py` |
| 2 | Display addition of even and odd factors using threads | `Assignment8_2.py` |
| 3 | Display sum of even and odd numbers from a list using threads | `Assignment8_3.py` |
| 4 | Count small letters, capital letters, and digits using three threads | `Assignment8_4.py` |
| 5 | Display numbers 1–50 and 50–1 using two threads in sequence | `Assignment8_5.py` |

Each file:
- Uses Python’s `threading` module  
- Demonstrates synchronization and parallel execution  
- Prints results for each thread along with program flow  

---

## 🧩 Problem Statements

### 1️⃣ Program 1 – Even and Odd Threads
Design a Python application which creates two threads named **even** and **odd**.  
- Even thread will display first 10 even numbers.  
- Odd thread will display first 10 odd numbers.

**Expected Output:**

Even Thread: 2 4 6 8 10 12 14 16 18 20

Odd Thread: 1 3 5 7 9 11 13 15 17 19


---

### 2️⃣ Program 2 – EvenFactor and OddFactor Threads
Design a Python application which creates two threads named **evenfactor** and **oddfactor**.  
- Both threads accept one parameter as an integer.  
- Evenfactor thread will display addition of even factors of that number.  
- Oddfactor thread will display addition of odd factors of that number.  
- After both threads complete, the main thread should display the message:  
  `"Exit from main"`.

**Example:**
Input: 18

Output:

Even Factor Addition: 24

Odd Factor Addition: 13

Exit from main


---

### 3️⃣ Program 3 – EvenList and OddList Threads
Design a Python application which creates two threads named **evenlist** and **oddlist**.  
- Both threads accept a list of integers as a parameter.  
- Evenlist thread adds all even numbers and displays the sum.  
- Oddlist thread adds all odd numbers and displays the sum.

**Example:**
Input: [11, 20, 17, 22, 34, 51, 55, 60]

Output:

EvenList Addition: 136

OddList Addition: 134


---

### 4️⃣ Program 4 – String Thread Character Count
Design a Python application which creates three threads named **small**, **capital**, and **digits**.  
- Each thread accepts a string as a parameter.  
- Small thread displays number of lowercase characters.  
- Capital thread displays number of uppercase characters.  
- Digits thread displays number of digits.  
Also display **Thread ID** and **Thread Name** for each thread.

**Example:**
Input: "MarvellousInfosystems123"

Output:

Small letters: 16

Capital letters: 2

Digits: 3

Thread Name: small | Thread ID: 11564

Thread Name: capital | Thread ID: 11565

Thread Name: digits | Thread ID: 11566


---

### 5️⃣ Program 5 – Sequential Thread Execution
Design a Python application which creates two threads named **thread1** and **thread2**.  
- Thread1 displays numbers from 1 to 50.  
- Thread2 displays numbers from 50 to 1.  
- After `thread1` completes, schedule and execute `thread2`.

**Expected Output:**

Thread1: 1 2 3 4 ... 50

Thread2: 50 49 48 47 ... 1


---

**📝 Notes:**

Use Python 3.x or later  
All programs use the `threading` module  
Ensure proper use of `start()` and `join()` for synchronization  

---

**🎯 Learning Outcomes**

- Learned to create and manage multiple threads in Python  
- Understood synchronization using `join()` method  
- Practiced executing independent and parallel thread operations  
- Gained experience with thread communication and sequence control  
- Strengthened concepts of parallel execution and CPU task sharing  

---

## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment8

# Run any program
python Assignment8_1.py
python Assignment8_2.py
python Assignment8_3.py
...

🧪 Sample Execution
# Example – Assignment8_1.py
Even Thread: 2 4 6 8 10 12 14 16 18 20
Odd Thread: 1 3 5 7 9 11 13 15 17 19

```
---

**👨‍💻 Author**
Yash Andhale
