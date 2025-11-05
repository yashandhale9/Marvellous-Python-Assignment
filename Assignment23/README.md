# 🧠 Assignment 23 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python – Machine Learning Assignment 23** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **data analysis and visualization using Pandas and Matplotlib**.  
It helps you understand how to manipulate, clean, and visualize tabular data efficiently.

Key concepts covered:
- 🧩 **Creating and manipulating DataFrames**
- 📊 **Descriptive statistics using Pandas**
- ➕ **Adding, replacing, and sorting data**
- 📈 **Bar and line plotting using Matplotlib**
- 🧮 **Handling missing data**

Each question is implemented in a separate `.py` file with clear structure and comments.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Create DataFrame and display basic info (shape, columns, data types) | `Assignment23_1.py` |
| 2 | Display descriptive statistics using `.describe()` | `Assignment23_2.py` |
| 3 | Add new column ‘Total’ as sum of all subject marks | `Assignment23_3.py` |
| 4 | Display students scoring more than 85 in Science | `Assignment23_4.py` |
| 5 | Replace ‘Pooja’ with ‘Puja’ in Name column | `Assignment23_5.py` |
| 6 | Sort DataFrame by Total marks (descending) | `Assignment23_6.py` |
| 7 | Create bar plot of student names vs total marks | `Assignment23_7.py` |
| 8 | Plot line chart of marks for Amit across all subjects | `Assignment23_8.py` |
| 9 | Handle missing values using column mean | `Assignment23_9.py` |
| 10 | Drop ‘English’ column from DataFrame | `Assignment23_10.py` |

---

## 🧩 Problem Statements

### 1️⃣ **Create DataFrame and Print Basic Information**
Create a DataFrame for student marks and display its **shape**, **columns**, and **data types**.

```python
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
```
---

### 2️⃣ **Descriptive Statistics**

Using the same DataFrame, display summary statistics (mean, std, min, max, etc.) using **.describe().**

---

### 3️⃣ **Add ‘Total’ Column**

Add a new column named **‘Total’** as the sum of all subject marks.

---

### 4️⃣ **Filter Students**

Display only those students who scored **more than 85 in Science.**

---

### 5️⃣ **Replace Value**

Replace the value **‘Pooja’** with **‘Puja’** in the Name column.

---

### 6️⃣ **Sort by Total Marks**

Sort the DataFrame by the **‘Total’** column in **descending order.**

---

### 7️⃣ **Bar Plot – Names vs Total Marks**

Create a **bar plot** of student names vs total marks using **Matplotlib.**

---

### 8️⃣ **Line Chart – Amit’s Marks**

Plot a **line chart** of Amit’s marks across all subjects to visualize his performance.

---

### 9️⃣ **Handle Missing Values**

Create a new DataFrame with missing values and fill them using **column mean.**

```
data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

```

---

### 🔟 **Drop Column**

Drop the **‘English’** column from the original DataFrame

---

### 🧰 **Required Libraries**

Install these dependencies before running the programs:
```
pip install pandas
pip install numpy
pip install matplotlib
```

---

### 🎯 **Learning Outcomes**

Learned to create and manipulate Pandas DataFrames

Performed statistical analysis using .describe()

Practiced data filtering, sorting, and updating operations

Created bar and line charts using Matplotlib

Understood missing value handling techniques

---

### ⚙️ **How to Run Programs**
```
# Navigate to this folder
cd Assignment23

# Run any program
python Assignment23_1.py
python Assignment23_2.py
python Assignment23_3.py
...


🧪 Sample Execution:

DataFrame Shape: (3, 4)
Columns: ['Name', 'Math', 'Science', 'English']
Data Types:
Name        object
Math         int64
Science      int64
English      int64
dtype: object
```

---
### 👨‍💻 **Author**

Yash Andhale

---
