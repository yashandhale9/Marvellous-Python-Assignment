# 🧠 Assignment 26 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains the solution for **Python – Machine Learning Assignment 26** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment demonstrates the creation of a **Machine Learning Classification Model**  
that predicts whether to **Play or Not Play** based on weather conditions.  
The algorithm used here is **K-Nearest Neighbour (KNN)**.

The dataset used: `MarvellousInfosystems_PlayPredictor.csv`

---

## 🎯 Objective

To design and implement a **classification-based ML model** capable of predicting outcomes  
based on categorical input features (`Weather` and `Temperature`).

---

## ⚙️ Steps Performed

### **Step 1: Get Data**
- Load dataset from `MarvellousInfosystems_PlayPredictor.csv`
- Inspect the structure and values of the data

### **Step 2: Clean, Prepare and Manipulate Data**
- The dataset contains **two categorical features**:
  - `Weather`: Sunny, Overcast, Rainy  
  - `Temperature`: Hot, Mild, Cold  
- The **target label** is `Play` → Yes / No  
- Apply **Label Encoding** to convert string data into numeric form using  
  `LabelEncoder` from `sklearn.preprocessing`.

### **Step 3: Train Data**
- Select **K-Nearest Neighbour (KNN)** algorithm from `sklearn.neighbors`.
- Use the `.fit()` method to train the model with the entire dataset.

### **Step 4: Test Data**
- Test the trained model by passing new input values for  
  `Weather` and `Temperature`.  
- Use **K = 3** for prediction.  
- Display whether the output is **“Yes”** (Play) or **“No”** (Don’t Play).

### **Step 5: Calculate Accuracy**
- Write a function `CheckAccuracy()` that:
  - Splits the dataset into **Training** and **Testing** sets (50%-50%).
  - Calculates accuracy using `.score()` method.  
  - Compares accuracy for different values of **K** to determine the best one.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Main Python script implementing KNN | `PlayPredictor.py` |
| 2 | Input dataset used for model training and testing | `MarvellousInfosystems_PlayPredictor.csv` |

---

## 🧩 Dataset Overview

| Weather | Temperature | Play |
|----------|--------------|------|
| Sunny    | Hot          | No   |
| Overcast | Mild         | Yes  |
| Rainy    | Cold         | Yes  |
| Sunny    | Mild         | No   |
| ...      | ...          | ...  |

---

## 🧮 Example Execution

**Input:**

Enter Weather: Sunny

Enter Temperature: Mild


**Output:**


Predicted Result: No


**Accuracy Check:**


For K = 3 → Accuracy = 91.6%

For K = 5 → Accuracy = 89.7%


---

## 🧰 Required Libraries

Install the following Python libraries before running the program:

```bash
pip install pandas
pip install numpy
pip install scikit-learn

```
---

### 🎯 **Learning Outcomes**

Understood the concept of Supervised Learning and Classification

Implemented KNN Algorithm for categorical prediction

Applied Label Encoding to handle text-based features

Practiced model training, testing, and evaluation

Learned to compute accuracy metrics and tune the parameter K

---

### ⚙️ **How to Run Program**
```
# Navigate to this folder
cd Assignment26

# Run the main Python file
python PlayPredictor.py


🧪 Sample Output:

Enter Weather: Rainy
Enter Temperature: Cold
Predicted Result: Yes
Accuracy of model: 92.4%
```

---

### 👨‍💻 **Author**

Yash Andhale

---
