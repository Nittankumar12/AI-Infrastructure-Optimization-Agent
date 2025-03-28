import pandas as pd

# Load the CSV file
csv_filename = "demo_azure_infra.csv"
df = pd.read_csv(csv_filename)


# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check data types
print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())
