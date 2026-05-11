# ==========================================
# TASK-1 : DATA PIPELINE DEVELOPMENT
# ETL Pipeline using Pandas & Scikit-Learn
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# ==========================================
# STEP 1 : EXTRACT
# ==========================================

# Load Dataset
# Make sure 'data.csv' exists in the same folder

try:
    dataset = pd.read_csv(r"C:\Users\User\Desktop\Codtech Internship\data.csv")
    print("Dataset Loaded Successfully!\n")

except FileNotFoundError:
    print("ERROR: data.csv file not found.")
    exit()

# Display first 5 rows
print("Original Dataset:\n")
print(dataset.head())

# ==========================================
# STEP 2 : TRANSFORM
# ==========================================

# -------- Handle Missing Values --------

# Select numerical columns
numerical_cols = dataset.select_dtypes(include=["int64", "float64"]).columns

# Fill missing values with mean
imputer = SimpleImputer(strategy="mean")

dataset[numerical_cols] = imputer.fit_transform(
    dataset[numerical_cols]
)

print("\nDataset After Handling Missing Values:\n")
print(dataset.head())

# -------- Encode Categorical Columns --------

label_encoder = LabelEncoder()

categorical_cols = dataset.select_dtypes(include=["object"]).columns

for col in categorical_cols:
    dataset[col] = label_encoder.fit_transform(dataset[col])

print("\nDataset After Encoding:\n")
print(dataset.head())

# -------- Separate Features and Target --------

# Features
X = dataset.iloc[:, :-1]

# Target Column
y = dataset.iloc[:, -1]

# -------- Feature Scaling --------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nScaled Features:\n")
print(X_scaled[:5])

# ==========================================
# STEP 3 : TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# ==========================================
# STEP 4 : LOAD
# ==========================================

# Save processed datasets

pd.DataFrame(X_train).to_csv("X_train.csv", index=False)
pd.DataFrame(X_test).to_csv("X_test.csv", index=False)

pd.DataFrame(y_train).to_csv("y_train.csv", index=False)
pd.DataFrame(y_test).to_csv("y_test.csv", index=False)

# ==========================================
# PIPELINE COMPLETED
# ==========================================

print("\nETL Pipeline Completed Successfully!")
print("Processed files saved:")
print("1. X_train.csv")
print("2. X_test.csv")
print("3. y_train.csv")
print("4. y_test.csv")