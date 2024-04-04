import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import time

df = pd.DataFrame({
    'crimeID': np.random.randint(1, 1000, 100),
    'incidentDate': pd.date_range(start='1/1/2022', periods=100, freq='D'),
    'primViolat': np.random.choice(['Theft', 'Assault', 'Burglary', 'Vandalism'], 100),
    'severityLevel': np.random.randint(1, 6, 100),
    'locationId': np.random.randint(1, 20, 100),
    'X': np.random.random(100),
    'Y': np.random.random(100)
})

# Aggregate crime data by locationId
aggregated_data = df.groupby('locationId').agg({
    'severityLevel': 'mean',  # Average severity level per location
    'crimeID': 'count'  # Count of crimes per location
}).reset_index().rename(columns={'crimeID': 'crimeCount'})

# Creating a binary classification label based on average severityLevel
# Adjust thresholds as needed
aggregated_data['safety_label'] = np.where(aggregated_data['severityLevel'] > 6, 'unsafe', 'safe')

# Preparing dataset for modeling
X = aggregated_data[['severityLevel', 'crimeCount']]
y = aggregated_data['safety_label']

# Encode the target variable
y_encoded = pd.get_dummies(y, drop_first=True)

# Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# Scaling features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42)
}

# Training and evaluating models
results = {}

for name, model in models.items():
    start_time = time.time()
    model.fit(X_train_scaled, y_train.values.ravel())  # y_train needs to be ravel() for scikit-learn
    y_pred = model.predict(X_test_scaled)
    
    elapsed_time = time.time() - start_time
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    
    results[name] = {
        "Time to Train (s)": elapsed_time,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall
    }

# Displaying the results
results_df = pd.DataFrame(results).T
print(results_df)
