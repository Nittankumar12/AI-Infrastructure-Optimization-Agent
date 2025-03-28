import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load Infrastructure Data
csv_filename = "cleaned_organization_data.csv"
df = pd.read_csv(csv_filename)

# Set plot style
sns.set_theme()

# Plot VM Count Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["VM_Count"], bins=10, kde=True)
plt.title("VM Count Distribution")
plt.xlabel("Number of VMs")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Cost vs Performance Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Cost_Per_Month"], y=df["Performance_Score"], hue=df["Industry"], palette="Set1")
plt.title("Cost vs Performance Score")
plt.xlabel("Cost Per Month ($)")
plt.ylabel("Performance Score")
plt.legend(title="Industry", bbox_to_anchor=(1, 1))
plt.show()

# Bar Plot: Average Storage Usage per Industry
plt.figure(figsize=(8, 5))
sns.barplot(x="Industry", y="Storage_TB", data=df, estimator=sum, ci=None, palette="coolwarm")
plt.title("Total Storage Usage by Industry")
plt.xlabel("Industry")
plt.ylabel("Total Storage (TB)")
plt.xticks(rotation=45)
plt.show()

print("Infrastructure data visualization completed.")
