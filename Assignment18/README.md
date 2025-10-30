# 🧠 Assignment 18 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 18** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **File Handling using Command-Line Arguments** in Python.  
It strengthens your ability to work with file operations, string processing, and data verification through command-line execution.

Key concepts covered:
- 📄 Reading and writing files  
- 🧩 Using `sys.argv` for command-line input  
- ⚙️ File comparison and validation  
- 🔍 String search and counting in files  
- 🧠 File I/O exception handling  

Each program is implemented in a **separate `.py` file**, following a modular and clean structure.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Check if a file exists in the current directory | `Assignment18_1.py` |
| 2 | Open a file and display its contents | `Assignment18_2.py` |
| 3 | Copy contents of one file into a new file (`Demo.txt`) | `Assignment18_3.py` |
| 4 | Compare contents of two files (Success/Failure) | `Assignment18_4.py` |
| 5 | Count the frequency of a given string in a file | `Assignment18_5.py` |

Each file:
- Accepts filenames or string input through command-line arguments  
- Performs operations like reading, writing, or comparing data  
- Displays results clearly in the console  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Check File Existence**
Write a program which accepts a file name from the user and checks whether that file exists in the current directory.

**Example:**

Input: Demo.txt

Output: File exists in the current directory.


---

### 2️⃣ **Program 2 – Display File Contents**
Write a program which accepts a file name from the user and displays its contents on the console.

**Example:**

Input: Demo.txt

Output: (Contents of Demo.txt displayed)


---

### 3️⃣ **Program 3 – Copy File Contents**
Write a program which accepts the source file name from the user (through command-line arguments)  
and creates a new file named `Demo.txt`, copying all contents from the existing file into the new one.

**Example:**

Input: ABC.txt

Output: New file Demo.txt created successfully with copied contents.


---

### 4️⃣ **Program 4 – Compare Two Files**
Write a program which accepts two file names from the user and compares their contents.  
If both files contain the same data, display **Success**, otherwise display **Failure**.  
Accept names of both files through command-line arguments.

**Example:**

Input: Demo.txt Hello.txt

Output: Success (if contents are same)


---

### 5️⃣ **Program 5 – String Frequency in File**
Write a program which accepts a file name and a string from the user and returns the **frequency** of that string in the file.

**Example:**

Input: Demo.txt Marvellous

Output: Frequency of 'Marvellous' in Demo.txt is: 5


---

## 📝 Notes

- Use Python 3.x or later  
- Import `sys` for accessing command-line arguments  
- Handle invalid filenames with `try-except`  
- Close files properly using `with open()`  
- Always verify file existence before reading  

---

## 🎯 Learning Outcomes

- Learned to handle **file operations** dynamically using command-line inputs  
- Practiced **reading, writing, copying, and comparing** file data  
- Implemented **string search** and frequency counting in text files  
- Strengthened understanding of **exception handling** in file I/O  
- Built practical skills for **automation and system scripting**  

---

## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment18

# Run any program
python Assignment18_1.py
python Assignment18_2.py
python Assignment18_3.py
...

# Example (with command-line arguments)
python Assignment18_3.py ABC.txt
python Assignment18_4.py Demo.txt Hello.txt
python Assignment18_5.py Demo.txt Marvellous
```

🧪 **Sample Execution:**
```
Input File: Demo.txt
Output: File exists in current directory.

Input Files: Demo.txt Hello.txt
Output: Success

```
---
👨‍💻 **Author**

Yash Andhale

---
