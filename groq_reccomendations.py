import os
import pandas as pd
import joblib
from groq import Groq

# Load the trained model
model = joblib.load("azure_infra_model.pkl")

# Initialize the Groq Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Function to load and merge infrastructure + usage data
def load_and_merge_data(infra_file, usage_file):
    df_infra = pd.read_csv(infra_file)
    df_usage = pd.read_csv(usage_file)

    # Debug: Print column names
    print("Infra CSV Columns:", df_infra.columns)
    print("Usage CSV Columns:", df_usage.columns)

    # Ensure 'Org_Name' exists
    if "Org_Name" not in df_infra.columns:
        raise ValueError("Infra CSV is missing 'Org_Name' column.")
    if "Org_Name" not in df_usage.columns:
        raise ValueError("Usage CSV is missing 'Org_Name' column.")

    # Merge both datasets on 'Org_Name'
    merged_df = pd.merge(df_infra, df_usage, on="Org_Name", how="inner")

    # Debug: Check after merging
    print("Merged DataFrame Columns:", merged_df.columns)

    return merged_df

# Function to preprocess new input data
def preprocess_new_data(merged_df, org_name):
    if "Org_Name" not in merged_df.columns:
        raise ValueError("'Org_Name' column is missing after merging!")

    # Filter for the specific organization
    org_data = merged_df[merged_df["Org_Name"] == org_name]

    if org_data.empty:
        raise ValueError(f"No data found for organization: {org_name}")

    # Drop Org_Name but keep other columns
    org_data = org_data.drop(columns=["Org_Name"], errors="ignore")

    return org_data

# Example Usage
infra_file = "cleaned_organization_data.csv"
usage_file = "cleaned_usage_data.csv"
org_name = "Org_1"  # Organization to analyze

# Load and process data
merged_df = load_and_merge_data(infra_file, usage_file)
processed_data = preprocess_new_data(merged_df, org_name)

# Debug: Check processed data
print("Processed Data Sample:\n", processed_data.head())
