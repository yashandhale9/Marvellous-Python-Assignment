# 🧠 Assignment 30 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains the solution for **Python – Machine Learning Assignment 30** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment focuses on building a **classification model** to predict whether a client will **subscribe to a term deposit** (Yes/No) using the **Bank Marketing Dataset** from the **UCI Machine Learning Repository**.

---

## 🎯 Objective

To predict the likelihood of a customer subscribing to a **bank term deposit** based on client details and marketing campaign interactions.  
This problem applies **supervised learning classification algorithms** and demonstrates **data preprocessing**, **model comparison**, and **evaluation metrics**.

---

## 🏦 Domain

**Banking and Marketing Analytics**

---

## ⚙️ Steps Performed

### **Step 1: Load and Explore Dataset**
- Load the **Bank Marketing Dataset** using Pandas.
- Display:
  - Dataset shape and info.
  - Class distribution for target column `y` (Yes/No).
- Handle **missing or unknown values** in categorical variables.
- Display **basic statistics** using `.describe()`.

---

### **Step 2: Data Preprocessing**
- Encode categorical variables using:
  - `LabelEncoder()` or  
  - `OneHotEncoder()` for multi-category features.
- Scale numerical features using **StandardScaler** to normalize values.

---

### **Step 3: Split the Data**
- Split dataset into **training (80%)** and **testing (20%)** sets using `train_test_split()`.
- Separate **features (X)** and **target (y)**.

---

### **Step 4: Train Classification Models**
Train the following machine learning models:
- **Logistic Regression**
- **K-Nearest Neighbours (KNN)**
- **Random Forest Classifier**

Use `.fit()` to train models on the training data.

---

### **Step 5: Evaluate the Models**
Compare models based on the following metrics:
- ✅ **Accuracy**
- 📊 **Confusion Matrix**
- 📋 **Classification Report**
- 🧮 **ROC–AUC Score**

Each model’s predictions are tested and compared on the same test dataset.

---

### **Step 6: Visualize Results**
Use **Matplotlib** and **Seaborn** to visualize:
- Confusion Matrices
- ROC Curves for all models
- Class distribution plots

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Main Python script for Bank Term Deposit prediction | `BankDepositPredictor.py` |
| 2 | Input dataset (UCI Bank Marketing Data) | `bank.csv` |
| 3 | Output visualizations and reports | `results/` |

---

## 🧩 Dataset Overview

**Target Variable:** `y` →  
`yes`: client subscribed to term deposit  
`no`: client did not subscribe  

| Feature | Description |
|----------|-------------|
| age | Age of the client |
| job | Job type (admin., technician, etc.) |
| marital | Marital status |
| education | Education level |
| default | Has credit in default? |
| balance | Average yearly account balance |
| housing | Has housing loan? |
| loan | Has personal loan? |
| contact | Contact communication type |
| day | Last contact day of month |
| month | Last contact month of year |
| duration | Duration of last contact |
| campaign | Number of contacts during campaign |
| previous | Number of contacts before this campaign |
| poutcome | Outcome of previous campaign |

---

## 🧮 Example Execution

**Output Example:**

Logistic Regression Accuracy: 89.2%

KNN Accuracy: 86.7%

Random Forest Accuracy: 91.5%

ROC-AUC Score (Random Forest): 0.94

---

```
Confusion Matrix (Random Forest):

[[780 35]
[ 45 140]]

```
### 📊 Classification Report

| Class | Precision | Recall | F1-Score | Support |
|:------|:----------:|:-------:|:---------:|:--------:|
| **0** | 0.95 | 0.96 | 0.96 | 815 |
| **1** | 0.80 | 0.76 | 0.78 | 185 |
| **Accuracy** |  |  | **0.92** | **1000** |
| **Macro Avg** | 0.88 | 0.86 | 0.87 | 1000 |
| **Weighted Avg** | 0.91 | 0.92 | 0.91 | 1000 |


---

## 🧰 Required Libraries

Install the following dependencies before running the program:

```
pip install pandas
pip install numpy
pip install scikit-learn
pip install matplotlib
pip install seaborn

```

### 🎯 **Learning Outcomes**
Understood data preprocessing and feature encoding

Trained and compared multiple classification algorithms

Evaluated performance using confusion matrix, ROC-AUC, and classification report

Gained insights into bank marketing campaign analysis

Improved skills in model selection and evaluation

---

### ⚙️ **How to Run Program**

```
# Navigate to this folder
cd Assignment30

# Run the main Python file
python BankDepositPredictor.py

🧪 Sample Output:

Random Forest Accuracy: 91.5%
ROC-AUC Score: 0.94
Predicted: ['no', 'yes', 'no', 'no', 'yes']

```

---

### 👨‍💻 **Author**

Yash Andhale

---
