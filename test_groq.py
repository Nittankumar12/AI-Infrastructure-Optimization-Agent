import os
import pandas as pd
import groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    print("Error: GROQ_API_KEY is not set. Check your .env file.")
    exit(1)

# Initialize Groq client
client = groq.Client(api_key=API_KEY)

# Function to load and merge infrastructure + usage data
def load_and_merge_data(infra_file, usage_file):
    df_infra = pd.read_csv(infra_file)
    df_usage = pd.read_csv(usage_file)

    # Ensure required columns exist
    if "Org_Name" not in df_infra.columns or "Org_Name" not in df_usage.columns:
        raise ValueError("Both CSV files must contain 'Org_Name' column.")

    # Merge both datasets on 'Org_Name'
    merged_df = pd.merge(df_infra, df_usage, on="Org_Name", how="inner")
    
    return merged_df

# Function to get AI recommendations from Groq API
def get_ai_recommendations(org_name, org_data, usage_data):
    prompt = f"""
    You are an AI cloud optimization assistant. 
    The organization **{org_name}** has the following cloud infrastructure:
    {org_data.to_dict()}
    
    Here is their past **3-month usage data**:
    {usage_data.to_dict()}

    The user wants to optimize their resources for cost reduction and performance improvement. 
    Compare this setup with similar organizations and suggest:
    - Cost savings opportunities
    - Better VM or database choices
    - Security enhancements
    - Performance improvements
    - Storage and bandwidth optimizations

    Provide a **detailed and actionable report**.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# Example CSV files
infra_file = "cleaned_organization_data.csv"
usage_file = "cleaned_usage_data.csv"
org_name = "Org_1"  # Change this to test different organizations

# Load and process data
try:
    merged_df = load_and_merge_data(infra_file, usage_file)

    # Get specific organization data
    org_data = merged_df[merged_df["Org_Name"] == org_name].drop(columns=["Org_Name"], errors="ignore")

    if org_data.empty:
        print(f"No data found for organization: {org_name}")
        exit(1)

    # Get AI recommendations
    recommendations = get_ai_recommendations(org_name, org_data, org_data)

    # Display results
    print("\n=== AI Optimization Recommendations ===\n")
    print(recommendations)

except Exception as e:
    print("Error:", e)
