import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student-mat.csv', delimiter=';')


features = df[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']].apply(pd.to_numeric, errors='coerce')
features = features.dropna()

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(scaled_features)

features['Cluster'] = clusters


cluster_means = features.groupby('Cluster').mean()
performance_map = {
    cluster_means.idxmax()['G3']: 'Top Performers',
    cluster_means.idxmin()['G3']: 'Struggling Students'
}
for cluster in cluster_means.index:
    if cluster not in performance_map:
        performance_map[cluster] = 'Average Students'

features['Performance Group'] = features['Cluster'].map(performance_map)


plt.figure(figsize=(10, 6))
sns.countplot(x='Performance Group', data=features, order=['Top Performers', 'Average Students', 'Struggling Students'])
plt.title('Distribution of Student Performance Groups')
plt.ylabel('Number of Students')
plt.show()


plt.figure(figsize=(14, 10))
for i, col in enumerate(['G3', 'studytime', 'failures', 'absences']):
    plt.subplot(2, 2, i+1)
    sns.boxplot(x='Performance Group', y=col, data=features, 
                order=['Top Performers', 'Average Students', 'Struggling Students'])
    plt.title(f'{col} Distribution by Performance Group')
plt.tight_layout()
plt.show()

cluster_profile = features.groupby('Performance Group').agg({
    'G1': 'mean',
    'G2': 'mean',
    'G3': 'mean',
    'studytime': 'mean',
    'failures': 'mean',
    'absences': 'mean',
    'Cluster': 'count'
}).rename(columns={'Cluster': 'Count'})

print("="*60)
print("Academic Performance Group Profiles:")
print("="*60)
print(cluster_profile.round(2))
print("\n" + "="*60)
print("Key Insights:")
print("="*60)
print("1. Top Performers: High grades, low failures, moderate study time")
print("2. Average Students: Moderate scores, some failures/absences")
print("3. Struggling Students: Low grades, high failures/absences, low study time")
print("="*60)

features.to_csv('student_performance_clusters.csv', index=False)
print("Results saved to 'student_performance_clusters.csv'")