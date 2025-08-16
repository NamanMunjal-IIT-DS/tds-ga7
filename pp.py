import numpy as np
import pandas as pd

# This script demonstrates how to:
# 1. Load data from a CSV file.
# 2. Compute a correlation matrix.
# 3. Save the correlation matrix to a new CSV file.

# --- Step 1: Load your data from a CSV file ---
# Replace 'your_data.csv' with the actual name of your file.
# If the file is not in the same directory as the script, provide the full path.
df = pd.read_excel('q-excel-correlation-heatmap.xlsx')

# Print a preview of the DataFrame to show what you're working with.
print("--- Sample DataFrame Head ---")
print(df.head())
print("\n")


# --- Step 2: Calculate the Correlation Matrix ---
correlation_matrix = df.corr()*100

# Print the resulting correlation matrix to the console.
print("--- Calculated Correlation Matrix ---")
print(correlation_matrix)
print("\n")


# --- Step 3: Save the Correlation Matrix to a CSV file ---
file_name = 'correlation_matrix.csv'
correlation_matrix.to_csv(file_name)

# Provide a confirmation message to the user.
print(f"Success! The correlation matrix has been saved to '{file_name}'.")