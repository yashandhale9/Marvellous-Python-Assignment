# 🧠 Assignment 28 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains the solution for **Python – Machine Learning Assignment 28** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment implements a **Machine Learning Classification Model** that classifies wines into three categories  
based on their **chemical composition** using the **Wine Dataset** provided by scikit-learn.

The task is to analyze 13 chemical constituents and classify each wine into one of the three cultivars.

---

## 🎯 Objective

To design and implement a **Classification-based Machine Learning Model** capable of predicting the **class of wine**  
based on its physical and chemical properties.

---

## ⚙️ Steps Performed

### **Step 1: Get Data**
- Import the **Wine Dataset** from `sklearn.datasets`.
- Extract features (`X`) and target labels (`y`).
- Display dataset shape and feature names.

### **Step 2: Clean, Prepare, and Manipulate Data**
- Split data into **Training** and **Testing** sets (70%-30%).
- Normalize/scale features if required for model performance.
- Identify the 13 input features:
  1. Alcohol  
  2. Malic acid  
  3. Ash  
  4. Alcalinity of ash  
  5. Magnesium  
  6. Total phenols  
  7. Flavanoids  
  8. Nonflavanoid phenols  
  9. Proanthocyanins  
  10. Color intensity  
  11. Hue  
  12. OD280/OD315 of diluted wines  
  13. Proline  

### **Step 3: Train Data**
- Use **K-Nearest Neighbour (KNN)** or **Decision Tree Classifier** algorithm from `sklearn`.
- Train the model using the training set with `.fit()`.

### **Step 4: Test Data**
- Test the model with unseen data using `.predict()`.
- Compare predicted vs actual labels.

### **Step 5: Calculate Accuracy**
- Evaluate model accuracy using `.score()` or `accuracy_score()` from `sklearn.metrics`.
- Display final accuracy percentage.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Python script implementing Wine Classification | `WineClassifier.py` |
| 2 | Dataset (automatically loaded from scikit-learn) | *(built-in dataset)* |

---

## 🧩 Dataset Overview

| Feature | Description |
|----------|-------------|
| Alcohol | Alcohol content in wine |
| Malic acid | Amount of malic acid |
| Ash | Mineral residue |
| Alcalinity of ash | Alkaline level |
| Magnesium | Magnesium content |
| Total phenols | Total phenolic compounds |
| Flavanoids | Flavonoid concentration |
| Nonflavanoid phenols | Non-flavonoid phenol content |
| Proanthocyanins | Pigment compounds |
| Color intensity | Depth of color |
| Hue | Hue of wine |
| OD280/OD315 | Optical density ratio |
| Proline | Amino acid concentration |

**Target Classes:**
- 🍷 Class 1  
- 🍇 Class 2  
- 🍾 Class 3  

---

## 🧮 Example Execution

**Output Example:**
Training dataset size: 124
Testing dataset size: 54
Accuracy of the model: 97.22%


---

## 🧰 Required Libraries

Install the following Python libraries before executing the code:

```
pip install pandas
pip install numpy
pip install scikit-learn

```
---

### 🎯 **Learning Outcomes**

Learned to import and explore the Wine Dataset

Understood classification concepts with multiple features

Implemented KNN / Decision Tree for multiclass prediction

Practiced data splitting, training, testing, and evaluation

Interpreted model accuracy for real-world dataset

---

### ⚙️ **How to Run Program**

```

# Navigate to this folder
cd Assignment28

# Run the Python file
python WineClassifier.py


🧪 Sample Output:

Accuracy of Wine Classification Model: 97.22%
Predicted Labels: [0 1 2 ...]
Actual Labels:    [0 1 2 ...]

```

---

## 👨‍💻 **Author**

Yash Andhale

---
