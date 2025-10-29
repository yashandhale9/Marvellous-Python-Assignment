# 🧠 Assignment 16 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 16** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment continues the exploration of **File Handling in Python**, emphasizing **file creation, reading, writing, copying, and filtering**.  
It helps in building a deeper understanding of file I/O operations, content processing, and data validation.

Concepts covered:
- 📄 File creation and writing using `open()`  
- 🔍 Reading and displaying file contents  
- 🧮 Counting lines, words, and characters  
- 📤 Copying, filtering, and cleaning file data  
- ⚙️ Real-world data handling with text files  

Each program is implemented in an individual `.py` file, written with clarity and modularity.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Create `student.txt` and write 5 student names into it | `Assignment16_1.py` |
| 2 | Read and display contents of `data.txt` | `Assignment16_2.py` |
| 3 | Count lines, words, and characters in a given file | `Assignment16_3.py` |
| 4 | Accept 10 numbers and write them into `numbers.txt` | `Assignment16_4.py` |
| 5 | Display lines from a file that contain more than 5 words | `Assignment16_5.py` |
| 6 | Copy contents from `source.txt` to `destination.txt` | `Assignment16_6.py` |
| 7 | Read `marks.txt` and display students scoring more than 75 | `Assignment16_7.py` |
| 8 | Remove all blank lines from a file and save cleaned data | `Assignment16_8.py` |

Each file:
- Uses file handling operations (`open`, `read`, `write`, `close`)  
- Handles invalid file paths with exception handling  
- Ensures clear and formatted console output  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Write Student Names into File**
Write a Python program to create a file named `student.txt` and write the names of **5 students** into it.

**Example:**

File Created: student.txt

Data Written: [“Vedant”, “Yash”, “Atharva”, “Sahil”, “Pragati”]


---

### 2️⃣ **Program 2 – Display File Contents**
Write a program to read and display the contents of a file named `data.txt`.

**Example:**

Input: data.txt

Output: (File contents displayed on screen)


---

### 3️⃣ **Program 3 – Count Lines, Words, and Characters**
Write a Python script to count and display the number of **lines**, **words**, and **characters** in a given file.

**Example:**

Lines: 4

Words: 23

Characters: 136


---

### 4️⃣ **Program 4 – Write 10 Numbers to File**
Accept **10 numbers** from the user and write each number on a **new line** inside a file named `numbers.txt`.

**Example:**

Input: 5 8 10 12 15 20 25 30 35 40

Output File: numbers.txt created successfully


---

### 5️⃣ **Program 5 – Display Lines with More Than 5 Words**
Write a Python program to read a file line by line and display only those lines which contain **more than 5 words**.

**Example:**

Input File: notes.txt

Output: (Displays lines containing > 5 words)


---

### 6️⃣ **Program 6 – Copy File Contents**
Write a Python program to copy the contents of one file named `source.txt` into another file named `destination.txt`.

**Example:**

Source File: source.txt

Destination File: destination.txt created successfully


---

### 7️⃣ **Program 7 – Display Students Scoring Above 75**
Create a file `marks.txt` containing **student names and marks**.  
Read this file and display the names of students who scored **more than 75 marks**.

**Example:**

Input (marks.txt):

Yash 85

Rohit 72

Amit 90

Output:

Students scoring above 75:

Yash – 85

Amit – 90


---

### 8️⃣ **Program 8 – Remove Blank Lines**
Write a script to remove all **blank lines** from a file and save the cleaned output into a new file.

**Example:**

Input File: messy.txt

Output File: clean.txt (All blank lines removed)


---

## 📝 Notes

- Use Python 3.x or later  
- Always close files after reading/writing  
- Prefer using context managers (`with open()`) for safety  
- Apply exception handling for file access errors  
- Use string functions like `split()` for word operations  

---

## 🎯 Learning Outcomes

- Strengthened understanding of **File Handling** in Python  
- Learned to **read, write, and process** text files efficiently  
- Practiced **line-by-line and word-based processing**  
- Understood how to handle real-world text data  
- Improved error handling and data filtering logic  

---

## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment16

# Run any program
python Assignment16_1.py
python Assignment16_2.py
python Assignment16_3.py
...

🧪 Sample Execution
# Example – Assignment16_3.py
Lines: 4
Words: 23
Characters: 136
```

👨‍💻 **Author**

Yash Andhale

---
