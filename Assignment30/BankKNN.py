import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    
    df = pd.read_csv("bank-full.csv", sep=';')
    print("Dataset Shape:", df.shape)
    print("First 5 rows:\n", df.head())

   
    print("\nNull values per column:\n", df.isnull().sum())
    df = df[df['contact'] != 'unknown']
    print("\nShape after removing 'unknown' contact:", df.shape)

 
    plt.figure(figsize=(6, 4))
    sns.countplot(x='y', data=df, palette='coolwarm')
    plt.title("Term Deposit Subscription Distribution")
    plt.xlabel("y (no=0, yes=1)")
    plt.ylabel("Count")
    plt.show()

    plt.figure(figsize=(6, 6))
    df['y'].value_counts().plot.pie(autopct='%1.1f%%', labels=['No', 'Yes'], colors=['skyblue', 'salmon'])
    plt.title("Subscription Distribution (Percentage)")
    plt.ylabel("")
    plt.show()

  
    df['y'] = df['y'].map({'yes': 1, 'no': 0})
    df_encoded = pd.get_dummies(df, drop_first=True)

    X = df_encoded.drop('y', axis=1)
    Y = df_encoded['y']


    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

   
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    
    accuracy_scores = []
    k_range = range(1, 21)
    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test, y_pred)
        accuracy_scores.append(accuracy)

    plt.figure(figsize=(8, 5))
    plt.plot(k_range, accuracy_scores, marker='o', linestyle='--')
    plt.title("Accuracy vs K value")
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is:", best_k)

    knn = KNeighborsClassifier(n_neighbors=best_k)
    knn.fit(X_train, Y_train)

    print("\nTraining Accuracy:", knn.score(X_train, Y_train))
    print("Testing Accuracy:", knn.score(X_test, Y_test))


    Y_pred = knn.predict(X_test)
    Y_prob = knn.predict_proba(X_test)[:, 1]

    cm = confusion_matrix(Y_test, Y_pred)
    print("\nConfusion Matrix:\n", cm)
    print("\nClassification Report:\n", classification_report(Y_test, Y_pred))

    auc = roc_auc_score(Y_test, Y_prob)
    print("\nROC-AUC Score:", auc)

    # Confusion Matrix Heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['No (0)', 'Yes (1)'],
                yticklabels=['No (0)', 'Yes (1)'])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("KNN - Confusion Matrix")
    plt.show()

    fpr, tpr, _ = roc_curve(Y_test, Y_prob)
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc:.2f})", color='darkorange')
    plt.plot([0, 1], [0, 1], 'k--', label="Random Guess")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("KNN - ROC Curve")
    plt.legend()
    plt.show()

    results = pd.DataFrame({
        'Actual': Y_test.values,
        'Predicted': Y_pred,
        'Probability (Yes)': Y_prob
    })
    results.to_csv("Bank_KNN_Predictions.csv", index=False)
    print("\nPredictions saved to 'Bank_KNN_Predictions.csv'")

if __name__ == "__main__":
    main()
