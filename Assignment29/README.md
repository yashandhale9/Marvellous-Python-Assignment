# 🧠 Assignment 29 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains the solution for **Python – Machine Learning Assignment 29** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

The objective of this assignment is to build a **Machine Learning model** that predicts whether a patient is **diabetic (1)** or **non-diabetic (0)** based on various **medical attributes** such as Glucose, Blood Pressure, BMI, and more.

---

## 🎯 Objective

To perform **end-to-end data analysis** and build a **classification model** using multiple algorithms to predict diabetes outcomes.

---

## ⚙️ Steps Performed

### **Step 1: Exploratory Data Analysis (EDA)**
- Load the dataset using **Pandas**
- Display the first 5 rows using `.head()`
- Show dataset information using `.info()` and check for missing/null values
- Display summary statistics using `.describe()`
- Visualize the distribution of the **Outcome** variable (0 = Non-Diabetic, 1 = Diabetic)
- Use visualizations like:
  - Histogram (`hist()`)
  - Boxplot (`boxplot()`)
  - Pairplot (`seaborn.pairplot()`)

---

### **Step 2: Data Preprocessing**
- Identify and handle missing or **zero values** in critical columns (Glucose, BloodPressure, Insulin, BMI)
- Perform **feature scaling** using:
  - `StandardScaler()` or  
  - `MinMaxScaler()`  
- Split the dataset into:
  - **Features (X)**
  - **Target (y)**

---

### **Step 3: Model Building**
Train and compare at least **two or more algorithms** on the dataset:
- Logistic Regression  
- K-Nearest Neighbours (KNN)  
- Decision Tree Classifier  

Use `train_test_split()` to divide the dataset into:
- **Training Set** (e.g., 80%)
- **Testing Set** (e.g., 20%)

---

### **Step 4: Model Evaluation**
Evaluate each model using:
- **Accuracy Score**
- **Confusion Matrix**
- **Precision, Recall, and F1 Score**
  
Visualize the **Confusion Matrix** using `seaborn.heatmap()` for better understanding of true/false classifications.

---

### **Step 5: Final Output**
- Predict whether a patient is **Diabetic (1)** or **Non-Diabetic (0)** based on test data.
- Display predictions on screen.
- Save predictions into a **CSV file** for further analysis.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Diabetes prediction model with multiple ML algorithms | `DiabetesPredictor.py` |
| 2 | Input dataset used for training and testing | `diabetes.csv` |
| 3 | Output predictions stored as CSV file | `PredictedResults.csv` |

---

## 🧩 Dataset Overview

The dataset contains medical diagnostic measurements for **768 patients**, including features like:

| Feature | Description |
|----------|-------------|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | Serum insulin (mu U/ml) |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Genetic influence indicator |
| Age | Age in years |
| Outcome | 1 = Diabetic, 0 = Non-Diabetic |

---

## 🧮 Example Execution

**Sample Output:**

Accuracy (Logistic Regression): 78.4%

Accuracy (KNN): 76.3%

Accuracy (Decision Tree): 74.1%
```
Confusion Matrix (KNN):

[[85 15]
[25 45]]

Precision: 0.75
Recall: 0.64
F1 Score: 0.69
```

---

## 🧰 Required Libraries

Install the following dependencies before running the program:

```
pip install pandas
pip install numpy
pip install scikit-learn
pip install seaborn
pip install matplotlib
```
---
### 🎯 **Learning Outcomes**

Performed Exploratory Data Analysis (EDA) on medical data

Learned data cleaning and preprocessing techniques

Built and compared multiple classification models

Evaluated models using accuracy, precision, recall, and F1-score

Visualized model performance using confusion matrix heatmaps

Strengthened understanding of end-to-end ML workflow

---
### ⚙️ **How to Run Program**
```

# Navigate to this folder
cd Assignment29

# Run the main file
python DiabetesPredictor.py


🧪 Sample Output:

Enter test sample (Glucose, BP, BMI...): 120 70 25.6 35
Predicted Result: Non-Diabetic (0)
Results saved successfully in PredictedResults.csv
```
---

### 👨‍💻 **Author**

Yash Andhale

---
