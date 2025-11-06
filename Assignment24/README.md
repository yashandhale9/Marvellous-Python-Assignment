# 🧠 Assignment 24 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python – Machine Learning Assignment 24** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **Data Normalization, Encoding, and Visualization** using Python libraries such as **Pandas, NumPy, and Matplotlib**.  
It aims to develop a deeper understanding of **data preprocessing techniques** and **graphical representation** in Machine Learning.

Key concepts covered:
- ⚙️ **Min-Max Normalization**
- 👩‍🏫 **One-Hot Encoding**
- 📊 **Grouping and Aggregation**
- 🥧 **Pie, Histogram, and Box Plot Visualization**
- 🧩 **Column Manipulation and Data Export**

Each task is implemented in a separate `.py` file with modular, well-commented code.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Normalize ‘Math’ scores using Min-Max scaling | `Assignment24_1.py` |
| 2 | Create Gender column and perform One-Hot Encoding | `Assignment24_2.py` |
| 3 | Group students by Gender and calculate average marks | `Assignment24_3.py` |
| 4 | Plot a Pie Chart of subject marks for Sagar | `Assignment24_4.py` |
| 5 | Add column ‘Status’ (Pass/Fail) based on total marks | `Assignment24_5.py` |
| 6 | Count number of students who passed | `Assignment24_6.py` |
| 7 | Export final DataFrame to CSV file | `Assignment24_7.py` |
| 8 | Plot Histogram of Math marks | `Assignment24_8.py` |
| 9 | Rename ‘Math’ column to ‘Mathematics’ | `Assignment24_9.py` |
| 10 | Plot Boxplot for English marks | `Assignment24_10.py` |

---

## 🧩 Problem Statements

### 1️⃣ **Normalize Math Scores**
Use **Min-Max scaling** to normalize the `Math` column between 0 and 1.

---

### 2️⃣ **One-Hot Encoding**
Add a new column **‘Gender’** and perform **One-Hot Encoding** to convert categorical data into numerical form.

---

### 3️⃣ **Group by Gender**
Group students by **Gender** and calculate their **average marks** in each subject.

---

### 4️⃣ **Pie Chart for Sagar**
Create a **Pie Chart** to visualize Sagar’s marks across all subjects.

---

### 5️⃣ **Add Pass/Fail Status**
Add a new column **‘Status’**:  
- If total marks ≥ 250 → `Pass`  
- Otherwise → `Fail`

---

### 6️⃣ **Count Passed Students**
Count and display how many students achieved a **‘Pass’** status.

---

### 7️⃣ **Export DataFrame to CSV**
Save the final DataFrame (with all modifications) into a new CSV file using **`to_csv()`**.

---

### 8️⃣ **Histogram of Math Marks**
Plot a **Histogram** showing the distribution of **Math scores**.

---

### 9️⃣ **Rename Column**
Rename column **‘Math’** → **‘Mathematics’** using **`rename()`** function.

---

### 🔟 **Boxplot for English Marks**
Create a **Boxplot** to visualize the distribution and detect outliers in **English marks**.

---

## 🧰 Required Libraries

Install the following dependencies before running the programs:
```bash
pip install pandas
pip install numpy
pip install matplotlib
```

---

### 🎯 **Learning Outcomes**

Learned Min-Max normalization for scaling data

Performed one-hot encoding to handle categorical values

Practiced grouping, filtering, and aggregation in Pandas

Visualized data using Pie, Histogram, and Box plots

Exported cleaned data to a CSV file

Strengthened understanding of data preprocessing and EDA (Exploratory Data Analysis)

---

### ⚙️ **How to Run Programs**
```
# Navigate to this folder
cd Assignment24

# Run any program
python Assignment24_1.py
python Assignment24_2.py
python Assignment24_3.py
...


🧪 Sample Output:

Normalized Math Scores:
0    0.75
1    1.00
2    0.50
3    0.25
Name: Math, dtype: float64

Number of Students Passed: 4
Data exported successfully to Final_StudentData.csv
```
---

### 👨‍💻 **Author**

Yash Andhale

---
