import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load the infrastructure data
csv_filename = "organization_data.csv"
df = pd.read_csv(csv_filename)
print("Infrastructure dataset loaded.")

# Step 1: Remove Duplicates
df = df.drop_duplicates()
print("Duplicate rows removed.")

# Step 2: Normalize Numerical Columns
num_cols = ["VM_Count", "Storage_TB", "Network_Bandwidth", "Cost_Per_Month", "Performance_Score"]
scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])
print("Numerical columns normalized.")

# Step 3: Convert Categorical Columns to Numeric (Encoding)
cat_cols = ["Industry", "VM_Type", "Database_Type", "Security_Level"]
encoder = LabelEncoder()
for col in cat_cols:
    df[col] = encoder.fit_transform(df[col])
print("Categorical columns encoded.")

# Step 4: Remove Outliers from 'Cost_Per_Month' using IQR
Q1 = df["Cost_Per_Month"].quantile(0.25)
Q3 = df["Cost_Per_Month"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df["Cost_Per_Month"] >= lower_bound) & (df["Cost_Per_Month"] <= upper_bound)]
print("Outliers removed from 'Cost_Per_Month'.")

# Step 5: Save Cleaned Data
df.to_csv("cleaned_organization_data.csv", index=False)
print("Cleaned infrastructure dataset saved as 'cleaned_organization_data.csv'.")
