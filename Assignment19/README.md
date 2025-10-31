# 🧠 Assignment 19 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 19** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **Directory Automation and File Operations** using Python.  
You will learn to automate common system tasks such as searching, renaming, and copying files with specific extensions.

Key concepts covered:
- 📁 Directory traversal using `os` and `shutil` modules  
- 🧩 File extension filtering and renaming  
- 🪄 File copy operations between directories  
- ⚙️ Command-line argument handling  
- 🧠 Logging, exception handling, and modular coding practices  

Each automation task is implemented in a **separate `.py` file**, following a structured, modular, and professional approach.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Display all files with a specific extension in a directory | `DirectoryFileSearch.py` |
| 2 | Rename all files with one extension to another | `DirectoryRename.py` |
| 3 | Copy all files from one directory to another (new directory created at runtime) | `DirectoryCopy.py` |
| 4 | Copy only specific file types (by extension) from one directory to another | `DirectoryCopyExt.py` |

Each file:
- Uses **command-line arguments** for user input  
- Displays output in a **log file** instead of the console  
- Handles **all exceptions** gracefully  
- Includes **input validation** and **user-defined functions** for each task  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Directory File Search**
Design an automation script that accepts a **directory name** and a **file extension** from the user.  
Display all files inside that directory with the given extension.

**Usage:**
```bash
python DirectoryFileSearch.py "Demo" ".txt"

Example Output (in log file):

[INFO] Files with .txt extension:
Demo1.txt
Sample.txt
Notes.txt
```
---

### 2️⃣ **Program 2 – Directory Rename**

Design an automation script that accepts a directory name and two file extensions from the user.
Rename all files with the first extension to the second extension.

**Usage:**
```
python DirectoryRename.py "Demo" ".txt" ".doc"

Example Output (in log file):

[INFO] Renamed: Notes.txt → Notes.doc
[INFO] Renamed: Demo1.txt → Demo1.doc
```
---

### 3️⃣ **Program 3 – Directory Copy**

Design an automation script that accepts two directory names.
Copy all files from the first directory into the second directory,
creating the second directory at runtime if it doesn’t exist.

**Usage:**
```
python DirectoryCopy.py "Demo" "Temp"
Example Output (in log file):

pgsql
Copy code
[INFO] Source Directory: Demo
[INFO] Destination Directory: Temp created
[INFO] 12 files copied successfully.

```

---

### 4️⃣ **Program 4 – Copy Files by Extension**

Design an automation script that accepts two directory names and a file extension.
Copy all files with that specific extension from the first directory to the second directory.
The second directory should be created at runtime.

**Usage:**
```
python DirectoryCopyExt.py "Demo" "Temp" ".exe"
Example Output (in log file):

pgsql
Copy code
[INFO] Source Directory: Demo
[INFO] Destination Directory: Temp created
[INFO] Copied 4 files with extension .exe
📝 Notes
Use Python 3.x or later

Accept inputs using command-line arguments (sys.argv)

Store all operation messages in a log file (no console printing)

Perform proper exception handling and validation

Use user-defined modules for reusability and cleaner code
```

---

### 🎯 **Learning Outcomes**

Mastered directory automation with Python

Learned to handle file extensions and renaming dynamically

Implemented copy and search operations using the os and shutil modules

Practiced logging, exception handling, and validation techniques

Built a foundation for advanced file system automation

---

### ⚙️ **How to Run Programs**
```

# Navigate to this folder
cd Assignment19

# Run any program
python DirectoryFileSearch.py "Demo" ".txt"
python DirectoryRename.py "Demo" ".txt" ".doc"
python DirectoryCopy.py "Demo" "Temp"
python DirectoryCopyExt.py "Demo" "Temp" ".exe"

---

🧪 Sample Execution (Log File Output):

[INFO] Source Directory: Demo
[INFO] Destination Directory: Temp created successfully.
[INFO] Copied 8 files with extension .txt

```
---

**👨‍💻 Author**

Yash Andhale

---

