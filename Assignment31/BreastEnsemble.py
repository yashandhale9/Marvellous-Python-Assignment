import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

def main():
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target)

    print("Dataset Shape:", X.shape)
    print(data)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    dt = DecisionTreeClassifier(max_depth=5, random_state=42)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    gb = GradientBoostingClassifier(n_estimators=100, random_state=42)

    dt.fit(X_train, y_train)
    rf.fit(X_train, y_train)
    gb.fit(X_train, y_train)

    models = {'Decision Tree': dt, 'Random Forest': rf, 'Gradient Boosting': gb}
    results = {}

    
    for name, model in models.items():
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
        cm = confusion_matrix(y_test, y_pred)

        results[name] = {'Accuracy': acc, 'ROC-AUC': roc_auc, 'Confusion Matrix': cm}

        print(f"\n{name} Results:")
        print(f"Accuracy: {acc:.3f}")
        print(f"ROC-AUC: {roc_auc:.3f}")
        print("Confusion Matrix:\n", cm)
        print("Classification Report:\n", classification_report(y_test, y_pred))

    # ROC Curves
    plt.figure(figsize=(8, 6))
    for name, model in models.items():
        y_prob = model.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc_score(y_test, y_prob):.3f})")

    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curves")
    plt.legend()
    plt.show()

   
    #You cn use this for feature importance for any case study
    importance=pd.Series(model.feature_importances_,index=X.columns)
    importance=importance.sort_values(ascending=False)
    importance.plot(kind='bar',figsize=[10,8],title="Feature Importance")
    plt.show()

    #Accuracy comparison 
    AccDf= pd.DataFrame({k: [v['Accuracy']] for k, v in results.items()})
    AccDf.plot(kind='bar', figsize=(8, 5))
    plt.title("Model Accuracy Comparison")
    plt.ylabel("Accuracy")
    plt.xticks([])
    plt.show()

if __name__ == "__main__":
    main()
