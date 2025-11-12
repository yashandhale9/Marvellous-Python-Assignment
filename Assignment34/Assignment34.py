import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

cancer = load_breast_cancer()
X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
y = pd.Series(cancer.target)

print("Checking for missing values:\n", X.isnull().sum())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nSummary statistics:")
print(X.describe())

plt.figure(figsize=(12, 10))
correlation_matrix = pd.DataFrame(X_scaled, columns=cancer.feature_names).corr()
sns.heatmap(correlation_matrix, cmap='coolwarm', linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=cancer.target_names))

importances = pd.Series(model.feature_importances_, index=cancer.feature_names)
importances.nlargest(10).plot(kind='barh')
plt.title("Top 10 Important Features")
plt.show()
