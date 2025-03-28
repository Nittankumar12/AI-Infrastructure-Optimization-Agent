import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the usage data
csv_filename = "usage_data.csv"
df = pd.read_csv(csv_filename)
print("Usage dataset loaded.")

# Step 1: Remove Duplicates
df = df.drop_duplicates()
print("Duplicate rows removed.")

# Step 2: Normalize Numerical Columns
num_cols = [
    "VM_Cost_Month_1", "VM_Cost_Month_2", "VM_Cost_Month_3",
    "Storage_Cost_Month_1", "Storage_Cost_Month_2", "Storage_Cost_Month_3",
    "Network_Cost_Month_1", "Network_Cost_Month_2", "Network_Cost_Month_3"
]
scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])
print("Numerical columns normalized.")

# Step 3: Save Cleaned Data
df.to_csv("cleaned_usage_data.csv", index=False)
print("Cleaned usage dataset saved as 'cleaned_usage_data.csv'.")
