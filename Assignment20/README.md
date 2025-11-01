# 🧠 Assignment 20 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 20** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **advanced file system automation** using Python.  
It covers checksum generation, duplicate file detection, and deletion — essential skills for optimizing and maintaining clean directories.

Key concepts covered:
- 🧩 File and directory traversal using `os` and `hashlib`  
- 🔍 Checksum-based file comparison  
- 🗂️ Detection and removal of duplicate files  
- 🧾 Logging automation output into log files  
- ⏱️ Measuring execution time for performance tracking  

Each task follows the **Marvellous Automation Script Rules**:
- Accept input via **command-line arguments**  
- Display all messages in a **log file** (not on console)  
- Use **modular functions** for clarity  
- Include **robust exception handling and validation**  

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Display checksums of all files in a directory | `DirectoryChecksum.py` |
| 2 | Find and log duplicate files in a directory | `DirectoryDuplicate.py` |
| 3 | Delete duplicate files and log deleted names | `DirectoryDuplicateRemoval.py` |
| 4 | Delete duplicate files and display execution time | `DirectoryDuplicateRemoval_Timed.py` |

Each file:
- Uses **hash-based checksum comparison** to detect duplicates  
- Generates a **timestamped log file** in the current directory  
- Handles all exceptions safely and logs errors where necessary  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Directory Checksum**

Design an automation script that accepts a **directory name** and displays the **checksum** (hash value) of all files within that directory.

**Usage:**
```
python DirectoryChecksum.py "Demo"
```
**Example Output (in log file):**

```
[INFO] File: data.txt → Checksum: 5d41402abc4b2a76b9719d911017c592
[INFO] File: image.jpg → Checksum: 4a7d1ed414474e4033ac29ccb8653d9b

```

---

### 2️⃣ **Program 2 – Directory Duplicate Logger**

Design an automation script that accepts a directory name and writes the names of duplicate files into a log file (Log.txt), created in the current directory.

**Usage:**
```
python DirectoryDuplicate.py "Demo"
```
**Example Output (in Log.txt):**

```
[INFO] Duplicate File Found: report1.pdf
[INFO] Duplicate File Found: image_copy.jpg
```
---

### 3️⃣ **Program 3 – Directory Duplicate Removal**

Design an automation script that accepts a directory name,
deletes all duplicate files, and writes their names into a log file (Log.txt).

**Usage:**
```
python DirectoryDuplicateRemoval.py "Demo"
```

**Example Output (in Log.txt):**
```
[INFO] Deleted Duplicate: photo1_copy.png
[INFO] Deleted Duplicate: notes_backup.txt
```

---

### 4️⃣ **Program 4 – Directory Duplicate Removal with Timer**

Design an automation script that performs duplicate file removal (as above)
and additionally displays the execution time required for completion.

**Usage:**
```
python DirectoryDuplicateRemoval_Timed.py "Demo"
```

**Example Output (in Log.txt):**
```
[INFO] Deleted: data_copy.csv
[INFO] Deleted: resume_old.docx
[INFO] Execution Time: 5.82 seconds
```

---

### 📝 **Notes**

Use Python 3.x or later

Accept command-line arguments using sys.argv

Calculate file checksum using the hashlib module (MD5/SHA1)

Create all log files dynamically (no console printing)

Use the time module to track script execution duration

Ensure safe file deletion using validation checks

---

### 🎯 **Learning Outcomes**

Understood file integrity verification using checksum

Learned to detect and remove duplicate files efficiently

Gained experience in logging automation results

Implemented performance measurement using timers

Practiced building modular and reliable automation scripts

---

### ⚙️ **How to Run Programs**

```
# Navigate to this folder
cd Assignment20

# Run any program
python DirectoryChecksum.py "Demo"
python DirectoryDuplicate.py "Demo"
python DirectoryDuplicateRemoval.py "Demo"
python DirectoryDuplicateRemoval_Timed.py "Demo"


🧪 Sample Execution:

[INFO] Directory Scanned: Demo
[INFO] Total Files Checked: 45
[INFO] Duplicates Found: 4
[INFO] Execution Time: 4.36 seconds

```

---

### 👨‍💻 **Author**

Yash Andhale

---
