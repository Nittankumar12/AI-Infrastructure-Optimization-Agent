import pandas as pd
import random

# Define possible values for categorical columns
industries = ["Finance", "Healthcare", "E-commerce", "Education", "Gaming"]
vm_types = ["Standard_D2s_v3", "Standard_F4s_v2", "Standard_B2ms"]
database_types = ["SQL", "NoSQL", "PostgreSQL", "MySQL"]
security_levels = ["Low", "Medium", "High"]

# Generate synthetic infrastructure data
data = []
for i in range(50):  # 50 organizations
    row = {
        "Org_Name": f"Org_{i+1}",
        "Industry": random.choice(industries),
        "VM_Count": random.randint(1, 50),
        "VM_Type": random.choice(vm_types),
        "Database_Type": random.choice(database_types),
        "Storage_TB": round(random.uniform(1, 100), 2),
        "Network_Bandwidth": round(random.uniform(0.5, 10), 2),
        "Security_Level": random.choice(security_levels),
        "Performance_Score": random.randint(50, 100),
        "Cost_Per_Month": round(random.uniform(500, 50000), 2)  # Added this column
    }
    data.append(row)

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_filename = "organization_data.csv"
df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' generated successfully! Below are a few rows:")
print(df.head())
