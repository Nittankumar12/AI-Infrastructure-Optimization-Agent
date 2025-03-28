import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load Usage Data
csv_filename = "cleaned_usage_data.csv"
df = pd.read_csv(csv_filename)

# Reshape the Data (Wide to Long Format)
df_long = df.melt(id_vars=["Org_Name"], 
                  var_name="Cost_Type", 
                  value_name="Cost")

# Extract Cost Category & Month Number
df_long["Category"] = df_long["Cost_Type"].apply(lambda x: x.split("_")[0])  # Extract cost category (VM, Storage, Network)
df_long["Month"] = df_long["Cost_Type"].apply(lambda x: x.split("_")[-1])  # Extract month number

# Convert Month to Integer for Correct Sorting
df_long["Month"] = df_long["Month"].str.replace("Month_", "").astype(int)

# Set plot style
sns.set_theme()

# Line Plot: Monthly Cost Trend for VM, Storage, and Network
plt.figure(figsize=(10, 5))
sns.lineplot(x="Month", y="Cost", hue="Category", style="Org_Name", data=df_long, marker="o")
plt.title("Monthly Cost Trend (VM, Storage, Network)")
plt.xlabel("Month")
plt.ylabel("Cost ($)")
plt.xticks([1, 2, 3])  # Ensure only the 3 months appear on x-axis
plt.legend(title="Cost Category")
plt.show()

# Box Plot: Distribution of Costs Across Categories
plt.figure(figsize=(10, 5))
sns.boxplot(x="Category", y="Cost", data=df_long, palette="Set2")
plt.title("Cost Distribution by Category")
plt.xlabel("Cost Category")
plt.ylabel("Cost ($)")
plt.show()

# Bar Plot: Average Cost Per Organization
plt.figure(figsize=(12, 5))
sns.barplot(x="Org_Name", y="Cost", hue="Category", data=df_long, estimator=sum, ci=None, palette="coolwarm")
plt.title("Total Cost Per Organization")
plt.xlabel("Organization")
plt.ylabel("Total Cost ($)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Cost Category")
plt.show()

print("Usage data visualization completed.")
