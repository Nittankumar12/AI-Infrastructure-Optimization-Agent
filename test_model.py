import pandas as pd
import joblib

# Load the trained model
model = joblib.load("azure_infra_model.pkl")

# Function to preprocess new input data
def preprocess_new_data(new_data):
    # Load the original cleaned dataset to get feature columns
    df = pd.read_csv("cleaned_organization_data.csv")  # Load infra data
    usage_df = pd.read_csv("cleaned_usage_data.csv")  # Load usage data

    # Merge datasets to get the original structure
    df = pd.merge(df, usage_df, on="Org_Name", how="inner")

    # Drop unnecessary columns
    df = df.drop(columns=["Org_Name"], errors="ignore")

    # Get feature columns (excluding target variable)
    feature_columns = df.drop(columns=["Cost_Per_Month"]).columns

    # Convert new data into a DataFrame
    new_df = pd.DataFrame([new_data])

    # Ensure all columns exist
    new_df = new_df.reindex(columns=feature_columns, fill_value=0)

    return new_df

# Example new organization data (infrastructure + recent usage)
new_org_data = {
    "Industry": 2,  # (Example: E-commerce)
    "VM_Count": 20,
    "VM_Type": 1,  # (Encoded Value)
    "Database_Type": 3,  # (Encoded Value)
    "Storage_TB": 10.5,
    "Network_Bandwidth": 2.5,
    "Security_Level": 1,  # (Encoded Value)
    "Performance_Score": 80,
    "Last_Month_VM_Cost": 5000,  # Example usage data
    "Last_Month_Storage_Cost": 1200,
    "Last_Month_Network_Cost": 800
}

# Preprocess input data
processed_data = preprocess_new_data(new_org_data)

# Make prediction
predicted_cost = model.predict(processed_data)[0]

print(f"Predicted Monthly Cost: ${predicted_cost:.2f}")
