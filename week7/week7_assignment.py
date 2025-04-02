import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target  # Add target column (0, 1, 2)
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})  # Map to names

# Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Check data types and missing values
print("\nData types and missing values:")
print(df.info())

# Clean missing values (if any)
df.dropna(inplace=True)  # Drop rows with missing values (if present)
print("\nMissing values after cleaning:", df.isnull().sum())