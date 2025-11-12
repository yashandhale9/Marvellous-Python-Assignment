import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

fake_df = pd.read_csv('fake.csv')
true_df = pd.read_csv('true.csv')

fake_df['label'] = 0
true_df['label'] = 1

# Combine datasets
df = pd.concat([fake_df, true_df], ignore_index=True)

df.dropna(subset=['text'], inplace=True)


X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


log_reg = LogisticRegression(max_iter=1000, random_state=42)
dec_tree = DecisionTreeClassifier(random_state=42)

log_reg.fit(X_train_tfidf, y_train)
dec_tree.fit(X_train_tfidf, y_train)


voting_hard = VotingClassifier(
    estimators=[('lr', log_reg), ('dt', dec_tree)],
    voting='hard'
)
voting_hard.fit(X_train_tfidf, y_train)

voting_soft = VotingClassifier(
    estimators=[('lr', log_reg), ('dt', dec_tree)],
    voting='soft'
)
voting_soft.fit(X_train_tfidf, y_train)


models = {
    'Logistic Regression': log_reg,
    'Decision Tree': dec_tree,
    'Hard Voting': voting_hard,
    'Soft Voting': voting_soft
}


fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()

for i, (name, model) in enumerate(models.items()):
    y_pred = model.predict(X_test_tfidf)
    acc = accuracy_score(y_test, y_pred)
    print(f'{name} Accuracy: {acc:.4f}')
   
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', ax=axes[i], cmap='Blues', 
                xticklabels=['Fake', 'Real'], yticklabels=['Fake', 'Real'])
    axes[i].set_title(f'{name} Confusion Matrix')
    axes[i].set_xlabel('Predicted')
    axes[i].set_ylabel('Actual')

plt.tight_layout()
plt.show()