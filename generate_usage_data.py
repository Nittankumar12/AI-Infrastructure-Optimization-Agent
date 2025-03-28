import pandas as pd
import random

# Load organization data to get existing organizations
org_df = pd.read_csv("organization_data.csv")
org_names = org_df["Org_Name"].tolist()  # Get the list of organization names

# Generate synthetic usage data for these organizations
usage_data = []
for org in org_names:
    row = {
        "Org_Name": org,
        "VM_Cost_Month_1": round(random.uniform(500, 5000), 2),
        "VM_Cost_Month_2": round(random.uniform(500, 5000), 2),
        "VM_Cost_Month_3": round(random.uniform(500, 5000), 2),
        "Storage_Cost_Month_1": round(random.uniform(100, 2000), 2),
        "Storage_Cost_Month_2": round(random.uniform(100, 2000), 2),
        "Storage_Cost_Month_3": round(random.uniform(100, 2000), 2),
        "Network_Cost_Month_1": round(random.uniform(50, 1000), 2),
        "Network_Cost_Month_2": round(random.uniform(50, 1000), 2),
        "Network_Cost_Month_3": round(random.uniform(50, 1000), 2),
    }
    usage_data.append(row)

# Create a DataFrame
usage_df = pd.DataFrame(usage_data)

# Save to CSV
csv_filename = "usage_data.csv"
usage_df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' generated successfully! Below are few rows")
print(usage_df.head())
