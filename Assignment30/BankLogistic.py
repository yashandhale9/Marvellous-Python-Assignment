import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve
import seaborn as sns
import matplotlib.pyplot as plt

def main():
  
    df = pd.read_csv("bank-full.csv", sep=';')
    print("Dataset Shape:", df.shape)
    print("First 5 rows:\n", df.head())


    print("\nNull values per column:\n", df.isnull().sum())
    df = df[df['contact'] != 'unknown']  # Remove unimportant 'unknown'
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

    df['y'] = df['y'].map({'yes': 1, 'no': 0})  # Target encoding
    df_encoded = pd.get_dummies(df, drop_first=True)  # One-hot for categorical

    X = df_encoded.drop('y', axis=1)
    Y = df_encoded['y']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000, solver='liblinear')
    model.fit(X_train, Y_train)

    print("\nTraining Accuracy:", model.score(X_train, Y_train))
    print("Testing Accuracy:", model.score(X_test, Y_test))

    Y_pred = model.predict(X_test)
    Y_prob = model.predict_proba(X_test)[:, 1]  # Probability of class 1 (yes)

    cm = confusion_matrix(Y_test, Y_pred)
    print("\nConfusion Matrix:\n", cm)
    print("\nClassification Report:\n", classification_report(Y_test, Y_pred))

    # ROC-AUC Score
    auc = roc_auc_score(Y_test, Y_prob)
    print("\nROC-AUC Score:", auc)

   
    # Confusion Matrix Heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['No (0)', 'Yes (1)'],
                yticklabels=['No (0)', 'Yes (1)'])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Logistic Regression - Confusion Matrix")
    plt.show()

    # ROC Curve
    fpr, tpr, _ = roc_curve(Y_test, Y_prob)
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc:.2f})", color='darkorange')
    plt.plot([0, 1], [0, 1], 'k--', label="Random Guess")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Logistic Regression - ROC Curve")
    plt.legend()
    plt.show()

    # Feature Importance (Coefficients)
    feature_importance = np.abs(model.coef_[0])
    importance_series = pd.Series(feature_importance, index=X.columns).sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    importance_series.head(15).plot(kind='bar', title='Top 15 Feature Importance (Logistic Regression)')
    plt.show()

    #  Save Predictions
    results = pd.DataFrame({
        'Actual': Y_test.values,
        'Predicted': Y_pred,
        'Probability (Yes)': Y_prob
    })
    results.to_csv("Bank_Logistic_Predictions.csv", index=False)
    print("\nPredictions saved to 'Bank_Logistic_Predictions.csv'")

if __name__ == "__main__":
    main()
