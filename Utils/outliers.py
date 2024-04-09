import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("dataMartId.csv")

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Standardize the features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[numeric_columns])

# Fit the one-class SVM model
svm_model = OneClassSVM(nu=0.05)  # Adjust nu parameter as needed
svm_model.fit(scaled_data)

# Predict outliers
outlier_prediction = svm_model.predict(scaled_data)

# Extract outliers
outliers = df[outlier_prediction == -1]

# Print outliers
print("Outliers:")
print(outliers)

outliers.to_csv("outliers.csv", index = False)
