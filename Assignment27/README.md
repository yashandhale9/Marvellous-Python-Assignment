# 🧠 Assignment 27 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains the solution for **Python – Machine Learning Assignment 27** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

The goal of this assignment is to develop a **Machine Learning model** that predicts **Sales growth** based on advertisement spending on **TV**, **Radio**, and **Newspaper** using **Linear Regression**.

---

## 🎯 Objective

To design a **Supervised Learning – Regression Model** that estimates sales performance from advertisement expenditure data.

---

## ⚙️ Steps Performed

### **Step 1: Get Data**
- Load the dataset from `MarvellousAdvertising.csv` into the Python program.
- Inspect data shape, features, and missing values.

### **Step 2: Clean, Prepare, and Manipulate Data**
- Identify independent variables:  
  - `TV`, `Radio`, and `Newspaper`  
- Identify dependent variable:  
  - `Sales`  
- Handle missing values (if any) and prepare the dataset for ML algorithms.

### **Step 3: Train Data**
- Choose the **Linear Regression Algorithm** from `sklearn.linear_model`.
- Split the dataset into **Training** and **Testing** halves (50%-50%).
- Train the model using `fit()` on the training data.

### **Step 4: Test Data**
- Test the model using the remaining half of the dataset.
- Use the `predict()` method to generate predicted sales values.

### **Step 5: Evaluate Results**
- Display both **Predicted** and **Actual** Sales values.
- Compute model accuracy using performance metrics like:
  - Mean Squared Error (MSE)
  - R² Score

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Linear Regression implementation for sales prediction | `AdvertisingPredictor.py` |
| 2 | Input dataset used for training and testing | `MarvellousAdvertising.csv` |

---

## 🧩 Dataset Overview

| TV | Radio | Newspaper | Sales |
|----|--------|------------|-------|
| 230.1 | 37.8 | 69.2 | 22.1 |
| 44.5 | 39.3 | 45.1 | 10.4 |
| 17.2 | 45.9 | 69.3 | 9.3 |
| 151.5 | 41.3 | 58.5 | 18.5 |
| ... | ... | ... | ... |

---

## 🧮 Example Execution

**Output:**

Predicted Sales: [21.4, 10.2, 9.5, 18.1, ...]

Actual Sales: [22.1, 10.4, 9.3, 18.5, ...]

Mean Squared Error: 1.12

R2 Score: 0.91


---

## 🧰 Required Libraries

Install the following Python libraries before executing the code:

```bash
pip install pandas
pip install numpy
pip install scikit-learn
```
---
### 🎯 **Learning Outcomes**

Learned how to perform Linear Regression in Python

Understood how advertisement spending impacts sales

Practiced data splitting, training, and prediction

Calculated and interpreted model accuracy metrics

Strengthened knowledge of Supervised Regression techniques

---

### ⚙️ **How to Run Program**
```
# Navigate to this folder
cd Assignment27

# Run the main file
python AdvertisingPredictor.py


🧪 Sample Output:

Enter test sample data manually or use dataset
Predicted Sales: [21.4, 10.2, 9.5, 18.1]
Actual Sales:    [22.1, 10.4, 9.3, 18.5]
Model Accuracy (R2 Score): 0.91
```
---

### 👨‍💻 **Author**

Yash Andhale

---
