import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

import seaborn as sns
import matplotlib.pyplot as plt

def main():
    diabetes = pd.read_csv("diabetes.csv")
    print("Columns:", diabetes.columns.tolist())
    
    print(diabetes.head())
    print("_____________________________________________")
    print("Dataset Shape:", diabetes.shape)

    X = diabetes.drop(columns=['Outcome'])
    Y = diabetes['Outcome']

    print("Feature Shape:", X.shape)
    print("Target Shape:", Y.shape)

    print("_____________________________________________")
    print("\nDiabetes Info")
    print(diabetes.info())
    print("_____________________________________________")
    print("\nNull values in each column:")
    print(diabetes.isnull().sum())
    print("_____________________________________________")
    print("\nRows with missing values:")
    print(diabetes[diabetes.isnull().any(axis=1)])
    print("_____________________________________________")
    print("Description:")
    print(diabetes.describe())
    print("_____________________________________________")
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    accuracy_scores=[]
    k_range=range(1,21)
    
    for k in k_range:
        model=KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train,Y_train)
        y_pred=model.predict(X_test)
        accuracy=accuracy_score(Y_test,y_pred)
    
        accuracy_scores.append(accuracy)
        
    plt.figure(figsize=(8,5))
    plt.plot(k_range,accuracy_scores,marker='o',linestyle='--')
    plt.title("Accuracy vs K value")
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()
    
    best_k=k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value os k is:",best_k)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model= KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, Y_train)

    print("Training Accuracy:", model.score(X_train, Y_train))
    print("Testing Accuracy:", model.score(X_test, Y_test))

    #Plot distribution of Outcome
    sns.countplot(x='Outcome',data=diabetes,palette='coolwarm')
    plt.title("Distribution of Outcome(1:Diabetes,0:No Diabetes)")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.show()
    
    #Outliers visual using boxplot
    plt.figure(figsize=(12,6))
    sns.boxplot(data=diabetes)
    plt.title("BoxPlot to detects Outliers")
    plt.show()
    #Another way to find outliers
    #Q1 = diabetes.quantile(0.25)
    #Q3 = diabetes.quantile(0.75)
    #IQR = Q3 - Q1
    #outliers = ((diabetes < (Q1 - 1.5 * IQR)) | (diabetes > (Q3 + 1.5 * IQR)))
    #print("Number of outliers in each column:")
    #print(outliers.sum())
    
    #confusion matrix
    Y_pred = model.predict(X_test)
    cm=confusion_matrix(Y_test,Y_pred)
    print("\nConfusion Matrix:")
    print(cm)
    
    print("Classification Report:")
    print(classification_report(Y_test,Y_pred))
    
    #Confusion matrix heatmap
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["No Diabetes (0)", "Diabetes (1)"],
            yticklabels=["No Diabetes (0)", "Diabetes (1)"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix Heatmap")
    plt.show()
    
    #Corelatio Heatmap
    plt.figure(figsize=(10,5))
    sns.heatmap(diabetes.corr(),annot=True,cmap='Blues')
    plt.title("Diabetes Correlation HeatMap ")
    plt.show()
    
    #pie chart
    outcome_counts = diabetes['Outcome'].value_counts()
    labels = ['No Diabetes (0)', 'Diabetes (1)']
    plt.figure(figsize=(8,6))
    plt.pie(outcome_counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue','grey'])
    plt.title("Diabetes Outcome Distribution (Percentage)")
    plt.axis('equal')
    plt.show()
    
    # Predict outcomes for the test set
    Y_pred = model.predict(X_test)

# Combine actual vs predicted into a DataFrame
    result = pd.DataFrame({
        'Actual Outcome': Y_test.values,
        'Predicted Outcome': Y_pred
    })

    print("\nPredictions on Test Data:")
    print(result)

# Save results to CSV
    result.to_csv("Diabetes_Test_Predictions.csv", index=False)
    print("\nPredictions saved to 'Diabetes_Test_Predictions.csv'")


    
if __name__ == "__main__":
    main()
