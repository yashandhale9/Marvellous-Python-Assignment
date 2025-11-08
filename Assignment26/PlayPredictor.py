import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix

def PlayPredictor(Datapath):
  
    df = pd.read_csv(Datapath)
    print("First 5 rows of dataset:\n", df.head())

    print("Clean the dataset.....")
    df.drop(columns=['Unnamed: 0'],inplace=True)
    print("Updated dataset is:")
    print(df.head())
    
    df.dropna(inplace=True)

    le_weather = LabelEncoder()
    le_temp = LabelEncoder()
    df['Whether'] = le_weather.fit_transform(df['Whether'])
    df['Temperature'] = le_temp.fit_transform(df['Temperature'])

    x = df.drop(columns=['Play'])
    y = df['Play']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

   
    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size=0.2, random_state=42)

    accuracy_scores = []
    k_range = range(1, 21)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_scores.append(accuracy)

    plt.figure(figsize=(8, 5))
    plt.plot(k_range, accuracy_scores, marker='o', linestyle='--', color='b')
    plt.title("Accuracy vs K Value")
    plt.xlabel("K Value")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of K is:", best_k)

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(x_train, y_train)
    y_pred_final = final_model.predict(x_test)
    final_accuracy = accuracy_score(y_test, y_pred_final)

    print(f"Final Best Accuracy: {final_accuracy * 100:.2f}%")

    cm = confusion_matrix(y_test, y_pred_final)
    print("Confusion Matrix:\n", cm)

    test_weather = le_weather.transform(['Sunny'])[0]
    test_temp = le_temp.transform(['Hot'])[0]
    prediction = final_model.predict([[test_weather, test_temp]])
    print(f"Prediction for (Sunny, Hot): {prediction[0]}")

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()
