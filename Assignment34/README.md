# 🧠 Assignment 34 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains the solution for **Python – Machine Learning Assignment 34** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This project focuses on building a **Breast Cancer Prediction Model** using the **Breast Cancer Wisconsin Dataset**.  
The task is to predict whether a tumor is **Malignant (Harmful)** or **Benign (Non-Harmful)** using Machine Learning classification algorithms.

---

## 🎯 Objective

To develop a classification-based **Machine Learning Model** capable of accurately predicting the type of tumor  
based on medical diagnostic features such as radius, texture, perimeter, area, and smoothness.

---

## ⚙️ Steps Performed

### **Step 1: Load and Explore Dataset**
- Load the **Breast Cancer Wisconsin Dataset** using:
  ```
  from sklearn.datasets import load_breast_cancer
  ```
  Display:

  Dataset shape and feature names

  Target names (Malignant / Benign)

  First few records

---

### **Step 2: Data Preprocessing**

Handle missing values (if any)

Normalize the dataset using **StandardScaler** for uniform feature distribution

Convert dataset to a **Pandas DataFrame** for better manipulation and visualization

---

### **Step 3: Exploratory Data Analysis (EDA)**

Display:

Summary statistics using **.describe()**

Feature correlation using **.corr()**

Visualize:

**Heatmap** for feature correlations

**Histogram** and **pair plots** for feature relationships

---

### **Step 4: Split Dataset**

Split the data into:

**Training Set (80%)**

**Testing Set (20%)**

Use:
```
from sklearn.model_selection import train_test_split
```
---

### **Step 5: Build Classification Model**

Train classification models such as:

**Logistic Regression**

**Support Vector Machine (SVM)**

**Random Forest Classifier**

Train each model using:
```
model.fit(X_train, y_train)
```
---

### **Step 6: Evaluate the Model**

Evaluate model performance using:

**✅ Accuracy Score**

**📊 Confusion Matrix**

**🧮 Classification Report**

Example:
```
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
```
---

### **Step 7: Observations & Conclusion**

Compare accuracies across models

Identify which algorithm performs best

Conclude with insights on **feature importance** and **classification reliability**

---

### 📁 **Files Included**

| No | Description                              | Filename                   |
| -- | ---------------------------------------- | -------------------------- |
| 1  | Python code for Breast Cancer Prediction | `BreastCancerPredictor.py` |
| 2  | Dataset (loaded directly from sklearn)   | *(built-in dataset)*       |
| 3  | Output charts and results                | `results/`                 |

---

### 🧩 **Dataset Overview**

| Attribute        | Description                                              |
| :--------------- | :------------------------------------------------------- |
| Mean Radius      | Mean of distances from center to points on the perimeter |
| Mean Texture     | Standard deviation of gray-scale values                  |
| Mean Perimeter   | Average perimeter length                                 |
| Mean Area        | Average area of the tumor                                |
| Mean Smoothness  | Local variation in radius lengths                        |
| Mean Compactness | (Perimeter² / Area - 1.0)                                |
| Mean Concavity   | Severity of concave portions                             |
| Mean Symmetry    | Symmetry measurement                                     |
| ...              | (and other 22 real-valued features)                      |

---

### **Target Variable:**

| Label | Meaning                |
| :---- | :--------------------- |
| 0     | Malignant (Cancerous)  |
| 1     | Benign (Non-Cancerous) |

---

**Dataset Details:**

**Source**: Breast Cancer Wisconsin Dataset

**Records**: 569

**Features**: 30

---

### 🧮 **Example Execution**

**Sample Output:**
```
Logistic Regression Accuracy: 97.89%
SVM Accuracy: 98.24%
Random Forest Accuracy: 98.60%

Confusion Matrix (Random Forest):
[[70  2]
 [ 3 39]]

Classification Report:
              precision    recall  f1-score   support
           0       0.96      0.97      0.97        72
           1       0.95      0.93      0.94        42
    accuracy                           0.96       114
   macro avg       0.96      0.95      0.96       114
weighted avg       0.96      0.96      0.96       114

```
---

### 📊 **Classification Report (Formatted)**

| Class             | Precision | Recall | F1-Score | Support |
| :---------------- | :-------: | :----: | :------: | :-----: |
| **0 (Malignant)** |    0.96   |  0.97  |   0.97   |    72   |
| **1 (Benign)**    |    0.95   |  0.93  |   0.94   |    42   |
| **Accuracy**      |           |        | **0.96** | **114** |
| **Macro Avg**     |    0.96   |  0.95  |   0.96   |   114   |
| **Weighted Avg**  |    0.96   |  0.96  |   0.96   |   114   |

---

### 🧰 **Required Libraries**

Install the following dependencies before running the program:
```
pip install pandas
pip install numpy
pip install scikit-learn
pip install matplotlib
pip install seaborn

```

### 🎯 **Learning Outcomes**

Learned **EDA** and **data preprocessing** in medical datasets

Implemented **classification algorithms** for prediction

Compared performance using **accuracy** and **F1-score**

Understood real-world application of ML in **healthcare diagnostics**

Improved data visualization and model evaluation skills

---

### ⚙️ **How to Run Program**
```
# Navigate to this folder
cd Assignment34

# Run the main Python file
python BreastCancerPredictor.py
```

### 🧪 **Sample Output:**
```
Predicted Tumor Type: Benign
Model Accuracy: 98.6%
```
---
### 👨‍💻 **Author**

Yash Andhale

---
