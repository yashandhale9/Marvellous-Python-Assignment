# 🧠 Assignment 22 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 22** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **File System Automation** using Python.  
It involves building an automation script that identifies and deletes duplicate files periodically,  
maintains logs, and sends operation details via email — combining multiple automation concepts into one practical task.

Key concepts covered:
- 🧩 **File handling and checksum computation**
- ⚙️ **Automated duplicate detection and removal**
- 🧾 **Logging with timestamped log files**
- 📧 **Sending log files through email**
- ⏳ **Periodic execution using time intervals**
- 💡 **Modular programming and exception handling**

Each task follows the **Marvellous Automation Standards**:
- Accept input through **command-line arguments**
- Display messages only through **log files**
- Define **modular functions** for each operation
- Handle **exceptions** safely with proper validation

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Main automation script to remove duplicate files periodically and email logs | `DuplicateFileRemoval.py` |
| 2 | User-defined module for file operations, checksum creation, and email handling | `MarvellousModule.py` |
| 3 | README file describing functionality and usage | `README.md` |

Each file:
- Uses **modular and reusable design**
- Accepts **dynamic input** via command line
- Implements **logging** instead of console printing
- Generates **structured, timestamped log files**

---

## 🧩 Problem Statement

Design an automation script that performs the following operations:

### 1️⃣ **Accept Directory Path from User**
Scan the specified directory and identify **duplicate files** based on checksum values.

### 2️⃣ **Delete Duplicate Files Automatically**
Delete duplicate files while preserving the original copies.

### 3️⃣ **Create Log File in ‘Marvellous’ Folder**
Inside a folder named **Marvellous**, create a log file with the **current date and time**.  
The log file must include:
- Names of deleted duplicate files  
- Operation timestamp  

### 4️⃣ **Run Automatically at Regular Intervals**
Accept a **time interval (in minutes)** and repeat the duplicate removal process periodically.

### 5️⃣ **Email the Log File Automatically**
Accept a **receiver’s email ID**, attach the log file, and send operation statistics via email.  
The email body should contain:
- 🕒 **Start time of scanning**  
- 📁 **Total files scanned**  
- 🧮 **Total duplicates found**

---

## 🧠 Command-Line Options

**Usage Example:**
```bash
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
```
---

## **Command-Line Arguments:**

| Argument                         | Description                                       |
| -------------------------------- | ------------------------------------------------- |
| `DuplicateFileRemoval.py`        | Name of the automation script                     |
| `E:/Data/Demo`                   | Absolute path of directory to scan for duplicates |
| `50`                             | Time interval (in minutes)                        |
| `marvellousinfosystem@gmail.com` | Email ID to receive the log file                  |

---

## 📝 **Notes**

Each operation should be implemented as a separate function.

All logic functions must be placed inside MarvellousModule.py.

Display no console output — use log files only.

Validate:

Directory path

Time interval input

Email address format

Support help options using -h or --help.

---

## 🎯 **Learning Outcomes**

Understood checksum-based duplicate detection

Learned to delete duplicates safely and efficiently

Practiced logging and automation scripting

Implemented email automation with attachments

Strengthened understanding of modular programming and CLI automation

---

## ⚙️ **How to Run the Program**
```
# Navigate to this folder
cd Assignment22

# Run the automation script
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com


🧪 Sample Execution:

[INFO] Scanning started at: 2025-02-14 10:00:00
[INFO] Total files scanned: 154
[INFO] Total duplicate files found: 6
[INFO] Deleted Duplicate: img_copy1.jpg
[INFO] Deleted Duplicate: report(1).pdf
[INFO] Log file created at: Marvellous/Log_2025-02-14_10-00-00.txt
[INFO] Email sent successfully to marvellousinfosystem@gmail.com

```
---
## 👨‍💻 **Author**

Yash Andhale

---
