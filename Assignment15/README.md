# 🧠 Assignment 15 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 15** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **File Handling in Python**, covering file creation, reading, writing, copying, comparing, and string search operations.  
It enhances your practical understanding of:
- 📄 Working with files (open, read, write, close)  
- 🧩 Using command-line arguments for file operations  
- 🔍 String and content comparison  
- ⚙️ Handling exceptions in file processing  

Each problem is implemented in a **separate `.py` file**, written with clean structure and modular approach.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Check whether a file exists in the current directory | `Assignment15_1.py` |
| 2 | Open a file and display its contents | `Assignment15_2.py` |
| 3 | Copy contents from one file to another using command-line arguments | `Assignment15_3.py` |
| 4 | Compare contents of two files and display success or failure | `Assignment15_4.py` |
| 5 | Count the frequency of a given string in a file | `Assignment15_5.py` |

Each file:
- Accepts filename(s) or string input from the user  
- Performs the specified file operation  
- Handles invalid inputs and displays results clearly  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Check File Existence**

Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

**Example:**

Input: Demo.txt

Output: File exists.

---


---

### 2️⃣ **Program 2 – Display File Contents**

Write a program which accepts a file name from the user and displays its contents on the console.

**Example:**

Input: Demo.txt

Output: (Contents of Demo.txt displayed on screen)

---


---

### 3️⃣ **Program 3 – Copy File Contents (Command-Line Arguments)**

Write a program which accepts the source file name from the user (through command-line arguments) and creates a new file named **Demo.txt**, copying all contents from the source file.

**Example:**

Input: ABC.txt

Output: File Demo.txt created successfully.

Contents of ABC.txt copied into Demo.txt

---


---

### 4️⃣ **Program 4 – Compare Two Files**

Write a program which accepts two file names from the user and compares their contents.  
If both files contain the same data, display **Success**, otherwise display **Failure**.  
Accept file names using command-line arguments.

**Example:**

Input: Demo.txt Hello.txt

Output: Success (if contents are same)

---


---

### 5️⃣ **Program 5 – Search String Frequency in File**

Write a program which accepts a file name and a string from the user and returns the **frequency** of that string in the file.

**Example:**

Input: Demo.txt Marvellous

Output: Frequency of 'Marvellous' in Demo.txt is: 5

---


---

## 📝 Notes

- Use Python 3.x or later  
- Use `os.path.exists()` or `open()` to verify file existence  
- Handle invalid file paths using `try-except` blocks  
- Use `sys.argv` for command-line argument inputs  
- Always close files properly after operations  

---

## 🎯 Learning Outcomes

- Gained practical experience in **file handling operations**  
- Learned how to **read, write, and copy files** in Python  
- Understood **command-line arguments** with `sys.argv`  
- Implemented **string search and comparison logic**  
- Improved error handling and exception management skills  

---

## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment15

# Run any program
python Assignment15_1.py
python Assignment15_2.py
python Assignment15_3.py
...

# Example (with command-line arguments)
python Assignment15_3.py ABC.txt
python Assignment15_4.py Demo.txt Hello.txt
```

🧪 **Sample Execution:**
```
Input File: Demo.txt
Output: File exists.

Input Files: Demo.txt Hello.txt
Output: Success (Both files have identical contents)
```
---

## 👨‍💻 **Author**

Yash Andhale

---
