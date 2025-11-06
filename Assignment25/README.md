# 🧠 Assignment 25 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains solutions for **Python – Machine Learning Assignment 25** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on **Data Preprocessing and Preparation** techniques — a crucial part of Machine Learning.  
It includes **outlier detection**, **encoding**, **scaling**, and **data splitting** to prepare datasets for modeling.

Key concepts covered:
- ⚙️ **Outlier detection using IQR**
- 🧮 **Data type conversion**
- 🔠 **Label and One-Hot Encoding**
- 📊 **Train-Test Splitting for Supervised Learning**
- 📏 **Min-Max Normalization**
- 🧩 **Value Replacement and Interpolation**

Each question is implemented in a separate `.py` file with modular structure and clear commenting.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Detect outliers in ‘Salary’ column using IQR | `Assignment25_1.py` |
| 2 | Detect column data types and convert ‘Age’ from float to int | `Assignment25_2.py` |
| 3 | Apply Label Encoding to a ‘City’ column | `Assignment25_3.py` |
| 4 | Apply One-Hot Encoding to a ‘Department’ column | `Assignment25_4.py` |
| 5 | Create a DataFrame and split into train/test sets | `Assignment25_5.py` |
| 6 | Replace multiple values in a column using a dictionary | `Assignment25_6.py` |
| 7 | Normalize ‘Age’ column using Min-Max Scaling | `Assignment25_7.py` |
| 8 | Fill missing values using interpolation | `Assignment25_8.py` |
| 9 | Replace marks less than 50 with ‘Fail’ using where() | `Assignment25_9.py` |
| 10 | Split a multi-feature DataFrame into train/test for ML | `Assignment25_10.py` |

---

## 🧩 Problem Statements

### 1️⃣ **Detect Outliers**
Detect outliers in the `Salary` column using the **IQR (Interquartile Range)** method.
```
data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}
```
---

### 2️⃣ **Data Type Conversion**

Detect column data types and convert **‘Age’** from float to integer.
```
data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}
```

---
### 3️⃣ **Label Encoding**

Apply **Label Encoding** to convert categorical ‘City’ data into numeric format.
```
data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
```

---
### 4️⃣ **One-Hot Encoding**

Perform One-Hot Encoding on the ‘Department’ column.
```
data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
```
---

### 5️⃣ **Train-Test Split**

Split the given dataset into training and testing sets.
```
data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}
```
---

### 6️⃣ **Replace Values Using Dictionary**

Replace multiple grade values with descriptive labels.
```
data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
```

Mapping:
```
A+ → Excellent  
A  → Very Good  
B+ → Good  
B  → Average  
C  → Poor
```

### 7️⃣ **Normalize ‘Age’ Column**

Perform Min-Max Scaling to normalize the Age column between 0 and 1.
```
data = {'Age': [18, 22, 25, 30, 35]}
```

### 8️⃣ **Fill Missing Values**

Use interpolation to fill missing numeric values.
```
data = {'Marks': [85, np.nan, 90, np.nan, 95]}
```

### 9️⃣ **Replace Marks Less Than 50**

Replace marks < 50 with "Fail" using the where() method.
```
data = {'Marks': [45, 67, 88, 32, 76]}
```

### 🔟 **Split Multi-Feature Dataset**

Split the DataFrame with multiple columns into training and testing datasets.
```
data = {
    'Age': [25, 30, 45, 35, 22],
    'Salary': [50000, 60000, 80000, 65000, 45000],
    'Purchased': [1, 0, 1, 0, 1]
}
```

### 🧰 **Required Libraries**

Install the following libraries before running the programs:
```
pip install pandas
pip install numpy
pip install scikit-learn
```

---
### 🎯 **Learning Outcomes**

Learned to detect outliers using IQR

Converted and validated data types

Implemented Label and One-Hot Encoding techniques

Practiced train-test splitting for supervised learning

Applied Min-Max normalization and data interpolation

Strengthened data cleaning and preprocessing knowledge

---

### ⚙️ **How to Run Programs**
```
# Navigate to this folder
cd Assignment25

# Run any program
python Assignment25_1.py
python Assignment25_2.py
python Assignment25_3.py
...


🧪 Sample Output:

IQR Range: 20000
Outliers detected: [100000]

Data Types before conversion:
Age    float64
Data Types after conversion:
Age      int64

Encoded City Column:
[2, 1, 0, 2, 0]
```
---

### 👨‍💻 **Author**

Yash Andhale

---
