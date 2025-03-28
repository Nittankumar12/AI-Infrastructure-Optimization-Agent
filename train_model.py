import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load the cleaned infrastructure and usage datasets
infra_df = pd.read_csv("cleaned_organization_data.csv")
usage_df = pd.read_csv("cleaned_usage_data.csv")

# Ensure both datasets have a common key (Org_Name) for merging
if "Org_Name" not in infra_df.columns or "Org_Name" not in usage_df.columns:
    raise ValueError("Missing 'Org_Name' column in one of the datasets. Ensure both datasets have a common key.")

# Merge infrastructure and usage data on 'Org_Name'
df = pd.merge(infra_df, usage_df, on="Org_Name", how="inner")

# Drop Org_Name after merging, as it is non-numeric
df = df.drop(columns=["Org_Name"], errors="ignore")

# Define features (X) and target (y)
X = df.drop(columns=["Cost_Per_Month"])  # Features (independent variables)
y = df["Cost_Per_Month"]  # Target variable (dependent variable)

# Ensure all categorical columns are numeric (they should be encoded in preprocessing)
if X.select_dtypes(include=["object"]).shape[1] > 0:
    raise ValueError("Some categorical columns are still in text format. Check preprocessing.")

# Split data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print(f"Model trained successfully. Mean Absolute Error: {mae:.2f}")

# Save the trained model
joblib.dump(model, "azure_infra_model.pkl")
print("Model saved as 'azure_infra_model.pkl'.")
