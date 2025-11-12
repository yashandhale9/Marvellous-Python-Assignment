# 🧠 Assignment 32 – Marvellous Infosystems

---

## 📘 About the Assignment

This folder contains the solution for **Python – Machine Learning Assignment 32** from  
**Marvellous Infosystems – Python Automation & Machine Learning** course conducted by **Piyush Khairnar Sir**.  

This assignment implements a **Fake News Detection Model** using **Ensemble Learning (Voting Classifier)** that predicts whether a news article is **Fake (0)** or **Real (1)** based on its text content.

---

## 🎯 Objective

To build a **Text Classification Model** that determines the authenticity of a news article  
using **Natural Language Processing (NLP)** and **Machine Learning techniques**.

---

## ⚙️ Steps Performed

### **Step 1: Data Loading**
- Load datasets `fake.csv` and `true.csv` using Pandas.
- Add a **label** column:
  - `0` → Fake News  
  - `1` → Real News
- Combine both datasets into a single DataFrame.

---

### **Step 2: Data Preprocessing**
- Drop unnecessary or null columns.
- Select relevant features such as:
  - `title`
  - `text`
- Clean and normalize text data by:
  - Lowercasing
  - Removing special characters, punctuation, and stopwords
- Shuffle and reset the dataset for randomness.

---

### **Step 3: Feature Extraction**
- Convert text data into numerical form using **TF-IDF Vectorization**.
- Split data into:
  - **Training Set (80%)**
  - **Testing Set (20%)**

---

### **Step 4: Model Building**
Train the following models:
1. **Logistic Regression**  
2. **Decision Tree Classifier**

Then combine them using **Voting Classifier**:
- **Hard Voting** → based on majority rule  
- **Soft Voting** → based on average predicted probabilities

---

### **Step 5: Model Evaluation**
- Compare accuracies of individual and ensemble models.
- Generate:
  - ✅ **Confusion Matrix**
  - 📊 **Classification Report**
  - 📈 **Accuracy Scores**

Evaluate the performance difference between **Hard Voting** and **Soft Voting** approaches.

---

## 📁 Files Included

| No | Description | Filename |
|----|--------------|-----------|
| 1 | Fake News Detection using Logistic Regression & Decision Tree | `FakeNewsPredictor.py` |
| 2 | Fake news dataset | `fake.csv` |
| 3 | Real news dataset | `true.csv` |
| 4 | Combined preprocessed dataset | `merged_news.csv` |

---

## 🧩 Dataset Overview

| Column | Description |
|:--------|:-------------|
| **title** | Title of the news article |
| **text** | Main content of the article |
| **label** | 0 → Fake, 1 → Real |

Each dataset (`fake.csv` and `true.csv`) contains multiple news records with titles and full text.  
After merging and labeling, the combined dataset is used for model training.

---

## 🧮 Example Execution

**Sample Output:**

Training Logistic Regression Model...

Training Decision Tree Model...

Combining models using Voting Classifier...

Accuracy (Logistic Regression): 98.1%

Accuracy (Decision Tree): 94.5%

Accuracy (Voting Classifier – Hard): 97.6%

Accuracy (Voting Classifier – Soft): 98.4%

---


### 📊 Classification Report

| Model | Precision | Recall | F1-Score | Accuracy |
|:------|:----------:|:-------:|:---------:|:---------:|
| Logistic Regression | 0.98 | 0.98 | 0.98 | 98.1% |
| Decision Tree | 0.94 | 0.95 | 0.94 | 94.5% |
| Voting Classifier (Hard) | 0.97 | 0.98 | 0.97 | 97.6% |
| Voting Classifier (Soft) | 0.98 | 0.99 | 0.98 | 98.4% |

---

## 🧰 Required Libraries

Install the following Python libraries before executing the program:

```
pip install pandas
pip install numpy
pip install scikit-learn
pip install nltk
pip install matplotlib
pip install seaborn
```

---

### 🎯 **Learning Outcomes**

Understood Text Classification and Natural Language Processing basics

Learned to use TF-IDF Vectorization for text-to-numeric conversion

Implemented Logistic Regression and Decision Tree Classifiers

Combined models using Voting Ensemble (Hard & Soft)

Evaluated models with Accuracy, Confusion Matrix, and Classification Reports

Gained hands-on experience in Fake News Detection Systems

---

### ⚙️ **How to Run Program**
```
# Navigate to this folder
cd Assignment32

# Run the main Python file
python FakeNewsPredictor.py


🧪 Sample Output:

Soft Voting Accuracy: 98.4%
The article is classified as: REAL
```

---

### 👨‍💻 **Author**

Yash Andhale

---
