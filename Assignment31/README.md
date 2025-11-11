# 🧠 Assignment 31 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains the solution for **Python – Machine Learning Assignment 31** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

The objective of this assignment is to build and compare **Ensemble Learning Models** for **Breast Cancer Classification** using the **Breast Cancer Wisconsin Dataset** from `sklearn.datasets`.  
You will analyze the performance of **Decision Tree**, **Random Forest**, and **Gradient Boosting** algorithms.

---

## 🎯 Objective

To design, train, and evaluate classification models that can accurately predict whether a **tumor** is  
**Malignant (Cancerous)** or **Benign (Non-Cancerous)** based on medical diagnostic data.

---

## ⚙️ Steps Performed

### **Step 1: Load the Dataset**
- Import the **Breast Cancer Wisconsin Dataset** using `sklearn.datasets.load_breast_cancer()`.
- Display dataset shape, feature names, and target labels.

---

### **Step 2: Data Exploration**
- Convert the dataset into a **Pandas DataFrame** for easier visualization.
- Display:
  - Basic statistics using `.describe()`
  - Missing values (if any)
  - Distribution of target classes
- The dataset contains **30 input features** and **1 target column**.

---

### **Step 3: Train-Test Split**
- Split the data into:
  - **Training Set (80%)**
  - **Testing Set (20%)**
- Use `train_test_split()` from `sklearn.model_selection`.

---

### **Step 4: Train Models**
Train and compare three machine learning models:
1. **Decision Tree Classifier**
2. **Random Forest Classifier**
3. **Gradient Boosting Classifier**

Each model is trained on the training set and evaluated on the test set.

---

### **Step 5: Model Evaluation**
Evaluate the models using the following metrics:
- ✅ **Accuracy Score**
- 📊 **Confusion Matrix**
- 🧮 **Classification Report**
- 📈 **ROC-AUC Curve**

Visualize results using `matplotlib` and `seaborn`.

---

### **Step 6: Feature Importance**
- Display the **top 10 most important features** contributing to the model’s decision-making.
- Visualize feature importances using a horizontal bar chart.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Breast Cancer classification using Decision Tree, Random Forest, and Gradient Boosting | `CancerClassifier.py` |
| 2 | Automatically loaded dataset from scikit-learn | *(built-in dataset)* |

---

## 🧩 Dataset Overview

**Dataset:** Breast Cancer Wisconsin Dataset (from sklearn)

| Class | Meaning |
|:------|:--------|
| **0** | Malignant (Cancerous) |
| **1** | Benign (Non-Cancerous) |

**Number of Samples:** 569  
**Number of Features:** 30  

Key Features include:
- mean radius  
- mean texture  
- mean perimeter  
- mean area  
- mean smoothness  
- mean compactness  
- mean symmetry  
- fractal dimension, etc.

---

## 🧮 Example Execution

**Sample Output:**

Decision Tree Accuracy: 93.85%

Random Forest Accuracy: 97.36%

Gradient Boosting Accuracy: 98.24%

```
Confusion Matrix (Gradient Boosting):
[[70 2]
[ 3 39]]
```

### 📊 Classification Report

| Class | Precision | Recall | F1-Score | Support |
|:------|:----------:|:-------:|:---------:|:--------:|
| **0 (Malignant)** | 0.96 | 0.97 | 0.97 | 72 |
| **1 (Benign)** | 0.95 | 0.93 | 0.94 | 42 |
| **Accuracy** |  |  | **0.96** | **114** |
| **Macro Avg** | 0.96 | 0.95 | 0.96 | 114 |
| **Weighted Avg** | 0.96 | 0.96 | 0.96 | 114 |

---


## 📊 ROC-AUC Comparison

| Model | ROC-AUC Score |
|:------|:--------------:|
| Decision Tree | 0.95 |
| Random Forest | 0.98 |
| Gradient Boosting | 0.99 |

---

## 🧰 Required Libraries

Install the following Python libraries before running the code:

```
pip install pandas
pip install numpy
pip install scikit-learn
pip install matplotlib
pip install seaborn

```
---

### 🎯 **Learning Outcomes**

Learned to use Ensemble Learning Algorithms

Understood Random Forest and Gradient Boosting concepts

Compared multiple models using evaluation metrics

Visualized model performance and feature importance

Strengthened understanding of classification problems in healthcare

---

### ⚙️ **How to Run Program**
```
# Navigate to this folder
cd Assignment31

# Run the main file
python CancerClassifier.py


🧪 Sample Output:

Random Forest Accuracy: 97.36%
Gradient Boosting Accuracy: 98.24%
Top Features:
1. mean concavity
2. mean radius
3. mean perimeter
...
```
---

### 👨‍💻 **Author**

Yash Andhale

---
