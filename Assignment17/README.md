# 🧠 Assignment 17 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python Assignment 17** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **Task Scheduling and Automation in Python**, using the `schedule` and `datetime` modules to automate repetitive jobs.  
It helps in understanding how to execute specific functions periodically or at specific times.

Concepts covered:
- ⏰ Task scheduling with the `schedule` module  
- 🕐 Automating time-based tasks (seconds, minutes, hours, daily)  
- 📅 Using the `datetime` module for date and time tracking  
- 🧠 Combining scheduling with file operations and logging  

Each problem is implemented in a **separate `.py` file**, using a clean and modular approach.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Print “Jay Ganesh…” every 2 seconds | `Assignment17_1.py` |
| 2 | Display current date and time every minute | `Assignment17_2.py` |
| 3 | Print “Do Coding..!” every 30 minutes | `Assignment17_3.py` |
| 4 | Print “Namskar…” daily at 9:00 AM | `Assignment17_4.py` |
| 5 | Write current time to `Marvellous.txt` every 5 minutes | `Assignment17_5.py` |
| 6 | Schedule “Lunch Time!” at 1 PM and “Wrap up work” at 6 PM | `Assignment17_6.py` |
| 7 | Perform file backup every hour and log in `backup_log.txt` | `Assignment17_7.py` |
| 8 | Check for “email updates” every 10 seconds | `Assignment17_8.py` |

Each program:
- Uses the `schedule` module for periodic automation  
- Runs continuously using a simple loop (`while True`)  
- Uses clear print statements for user feedback  

---

## 🧩 Problem Statements

### 1️⃣ **Program 1 – Print “Jay Ganesh…” every 2 seconds**
Write a Python script that prints “Jay Ganesh…” every 2 seconds using  
`schedule.every(2).seconds.do(...)`.

**Example:**

Output:

Jay Ganesh…

Jay Ganesh…

(repeats every 2 seconds)


---

### 2️⃣ **Program 2 – Display Current Date and Time**
Schedule a task that displays the current date and time **every minute** using the `datetime` module.

**Example:**

Output:

Current Time: 2025-10-06 18:30:00

(Current time updates every minute)


---

### 3️⃣ **Program 3 – Print “Do Coding..!” every 30 minutes**
Write a program that schedules a function to print “Do Coding..!” every 30 minutes.

**Example:**

Output:

Do Coding..!

Do Coding..! (after 30 minutes)


---

### 4️⃣ **Program 4 – Daily Task at 9:00 AM**
Create a task that runs once every day at **9:00 AM** and prints “Namskar…”.

**Example:**

Output:

Namskar… (runs at 9:00 AM daily)


---

### 5️⃣ **Program 5 – Log Time to File**
Schedule a job that runs **every 5 minutes** to write the current time into a file `Marvellous.txt`.

**Example:**

Output File: Marvellous.txt

Contents:

2025-10-06 14:30:00

2025-10-06 14:35:00
...


---

### 6️⃣ **Program 6 – Multiple Scheduled Tasks**
Write a script that schedules multiple tasks:
- Print **"Lunch Time!"** at **1:00 PM**  
- Print **"Wrap up work"** at **6:00 PM**

**Example:**

Output:

Lunch Time!

Wrap up work


---

### 7️⃣ **Program 7 – Hourly File Backup**
Schedule a function that performs **file backup every hour** and writes a log entry into `backup_log.txt`.

**Example:**

Output File: backup_log.txt

Entry:
[2025-10-06 12:00:00] Backup completed successfully.


---

### 8️⃣ **Program 8 – Email Check Simulation**
Write a script that simulates checking for email updates every 10 seconds.  
(Use a print statement like “Checking mail…” instead of real email logic.)

**Example:**

Output:

Checking mail…

Checking mail…

(Repeats every 10 seconds)


---

## 📝 Notes

- Use Python 3.x or later  
- Install the **`schedule`** module using `pip install schedule`  
- Use `while True:` loop with `time.sleep(1)` to keep scheduler running  
- Use `datetime.now()` for timestamps  
- Press **Ctrl + C** to stop script execution manually  

---

## 🎯 Learning Outcomes

- Learned how to **automate repetitive tasks** in Python  
- Gained practical experience using the **`schedule`** module  
- Understood **time-based execution** and periodic jobs  
- Implemented **logging and file-based scheduling**  
- Built a foundation for real-world **automation and monitoring systems**  

---

## ⚙️ How to Run Programs

```bash
# Navigate to this folder
cd Assignment17

# Run any program
python Assignment17_1.py
python Assignment17_2.py
python Assignment17_3.py
...

# Install required package
pip install schedule

```

🧪 **Sample Execution:**
```

# Example – Assignment17_1.py
Jay Ganesh…
Jay Ganesh…
Jay Ganesh…

```
---

**👨‍💻 Author**

Yash Andhale

---
