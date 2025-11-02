# 🧠 Assignment 21 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 21** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **Process Monitoring and System Automation** in Python.  
It covers process handling, logging, and email automation — essential topics for advanced automation scripting.

Key concepts covered:
- ⚙️ Process management using the `psutil` module  
- 📋 Retrieving process details (Name, PID, Username)  
- 🧾 Logging system information in real time  
- 📧 Sending log files via email automatically  
- 🧠 Modular programming and exception handling  

Each automation script follows the **Marvellous Automation Standards**:
- Accept input through **command-line arguments**  
- Display messages only through **log files**  
- Define **separate functions** for each task  
- Handle **expected exceptions** robustly  
- Perform **validations** before every operation  

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Display all running processes with Name, PID, and Username | `ProcInfo.py` |
| 2 | Display information of a specific running process | `ProcInfo.py` (with process name argument) |
| 3 | Create a log file in a given directory containing process information | `ProcInfoLog.py` |
| 4 | Create log file and send it to given email address automatically | `ProcInfoLog.py` (with directory and email arguments) |

Each script:
- Uses **`psutil`** for process information retrieval  
- Stores output in a **log file** (not printed to console)  
- Accepts inputs (like directory name or process name) via command-line  
- Implements **email sending feature** using SMTP  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Display Running Processes**

Design an automation script that displays information of all running processes — including **Name**, **PID**, and **Username**.

**Usage:**
```
python ProcInfo.py
```

**Example Output (in log file):**
```
[INFO] Process Name: chrome.exe    PID: 4520    User: yash
[INFO] Process Name: notepad.exe   PID: 6124    User: yash

```
---

### 2️⃣ **Program 2 – Display Specific Process Information**

Design an automation script which accepts a process name from the user
and displays information of that process if it is running.

**Usage:**
```
python ProcInfo.py notepad
```

**Example Output (in log file):**

```
[INFO] Process Found:
Name: notepad.exe
PID: 6234
User: yash
```

### 3️⃣ **Program 3 – Create Process Log File**

Design an automation script which accepts a directory name from the user and
creates a log file in that directory containing information about all running processes (Name, PID, Username).

**Usage:**
```
python ProcInfoLog.py Demo
```

**Example Output (in Demo/ProcessLog.txt):**
```
[INFO] Process Name: chrome.exe    PID: 4520    User: yash
[INFO] Process Name: explorer.exe  PID: 1012    User: yash
```

---

### 4️⃣ **Program 4 – Email Log File Automatically**

Design an automation script which accepts a directory name and an email address.
It should create a process log file in that directory and send the log file as an email attachment to the specified email.

**Usage:**
```
python ProcInfoLog.py Demo xyz@gmail.com
```

**Example Output (in log file):**
```

[INFO] Log file created: Demo/ProcessLog.txt
[INFO] Email sent successfully to xyz@gmail.com

```
---

### 📝 **Notes**

Use Python 3.x or later

Install required modules using:
```
pip install psutil
pip install smtplib
```

Use psutil.process_iter() for retrieving running processes

Use the os module for directory handling

Use smtplib for email sending functionality

Log all operations and errors to a log file instead of printing to console

---

### 🎯 **Learning Outcomes**

Learned to monitor and manage system processes programmatically

Practiced logging automation for process tracking

Implemented email-based file reporting using SMTP

Strengthened understanding of modular design and error handling

Built a foundation for system administration automation scripts

---

### ⚙️ **How to Run Programs**
```
# Navigate to this folder
cd Assignment21

# Run any program
python ProcInfo.py
python ProcInfo.py notepad
python ProcInfoLog.py Demo
python ProcInfoLog.py Demo xyz@gmail.com


🧪 Sample Execution:

# Example – ProcInfoLog.py
[INFO] Log file created at: Demo/ProcessLog.txt
[INFO] Total processes logged: 65
[INFO] Email sent successfully to xyz@gmail.com

```

---

### 👨‍💻 **Author**

Yash Andhale

---
