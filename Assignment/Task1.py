import pandas as pd
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris(as_frame=True)
df = iris.frame

# 1. Select specific columns (sepal length & petal length)
selected = df[["sepal length (cm)", "petal length (cm)"]]
print("Selected Columns:")
print(selected.head())

# 2. Filter rows where petal length > 4
filtered = df[df["petal length (cm)"] > 4]
print("\nRows where petal length > 4:")
print(filtered.head())

# 3. Perform a calculation: Add a new column 'sepal_ratio' = sepal length / sepal width
df["sepal_ratio"] = df["sepal length (cm)"] / df["sepal width (cm)"]
print("\nDataFrame with new column 'sepal_ratio':")
print(df.head())
