# 🧠 Assignment 33 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains the solution for **Python – Machine Learning Assignment 33** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

The objective of this assignment is to **cluster students** into different academic performance groups using the **K-Means Clustering Algorithm**.  
This is an example of **Unsupervised Learning**, where the model groups students based on similarity in performance indicators without predefined labels.

---

## 🎯 Objective

To cluster students into performance-based groups:
- 🥇 **Top Performers**
- ⚖️ **Average Students**
- 🚫 **Struggling Students**

based on their **grades**, **study time**, **failures**, and **absences**.

---

## ⚙️ Steps Performed

### **Step 1: Load the Dataset**
- Load the **Student Performance Dataset** using Pandas.
- Select numerical features:
  - `G1` – First grade  
  - `G2` – Second grade  
  - `G3` – Final grade  
  - `studytime` – Weekly study time  
  - `failures` – Number of past class failures  
  - `absences` – Number of school absences  

---

### **Step 2: Data Preprocessing**
- Handle any missing or null values.
- Normalize/scale features using **StandardScaler** to ensure all values are in a comparable range.
- Inspect dataset statistics using `.describe()` and `.info()`.

---

### **Step 3: Apply K-Means Clustering**
- Use the **K-Means Algorithm** from `sklearn.cluster`.
- Choose **3 clusters** to represent:
  - Cluster 0 → Top Performers  
  - Cluster 1 → Average Students  
  - Cluster 2 → Struggling Students
- Fit the model using:
```
  kmeans = KMeans(n_clusters=3, random_state=42)
  kmeans.fit(X_scaled)

```

Add a new column **Cluster** to the DataFrame to store the cluster labels.

---

### **Step 4: Analyze and Interpret Results**

Display number of students in each cluster.

Analyze cluster characteristics:

Mean grades, study time, failures, and absences per group.

Visualize clusters using Matplotlib and Seaborn:

Scatter plots for G3 vs studytime

Cluster distribution by color coding

---

### 📁 **Files Included**

| No | Description                                   | Filename              |
| -- | --------------------------------------------- | --------------------- |
| 1  | Student Performance Clustering implementation | `StudentCluster.py`   |
| 2  | Input dataset for training                    | `student-mat.csv`     |
| 3  | Clustered results with labels                 | `ClusteredOutput.csv` |

---

### 🧩 **Dataset Overview**

**Dataset Name:** Student Performance Data Set
**Selected Features:**

| Feature   | Description                   |
| :-------- | :---------------------------- |
| G1        | First period grade            |
| G2        | Second period grade           |
| G3        | Final grade                   |
| studytime | Weekly study time             |
| failures  | Number of past class failures |
| absences  | Number of school absences     |

---

### 🧮 **Cluster Interpretation**

| Cluster | Label                  | Characteristics                                           |
| :-----: | :--------------------- | :-------------------------------------------------------- |
|  **0**  | 🥇 Top Performers      | High grades, low failures, high study time, few absences  |
|  **1**  | ⚖️ Average Students    | Moderate scores, average study time, few failures         |
|  **2**  | 🚫 Struggling Students | Low grades, high failures, high absences, less study time |

---

### 🧰 **Required Libraries**

Install the following Python libraries before running the program:

pip install pandas
pip install numpy
pip install scikit-learn
pip install matplotlib
pip install seaborn

---

### 🎯 **Learning Outcomes**

Learned to apply K-Means Clustering for performance-based grouping

Understood Unsupervised Learning principles

Performed data scaling and feature normalization

Interpreted cluster results and their real-world significance

Visualized clusters for better understanding of student performance

---

### ⚙️ **How to Run Program**
```
# Navigate to this folder
cd Assignment33

# Run the main Python file
python StudentCluster.py


🧪 Sample Output:

Number of students in each cluster:
Cluster 0 (Top Performers): 120
Cluster 1 (Average Students): 250
Cluster 2 (Struggling Students): 130

Cluster Analysis Summary:
Cluster 0 → High G3, Low Failures
Cluster 1 → Moderate G3, Moderate Study Time
Cluster 2 → Low G3, High Absences

```
---

### 👨‍💻 **Author**

Yash Andhale

---
