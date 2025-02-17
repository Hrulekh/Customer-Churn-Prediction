import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Drop unnecessary columns (like Customer ID if present)
    if 'customerID' in df.columns:
        df.drop(columns=['customerID'], inplace=True)

    # Convert 'TotalCharges' to numeric (handling errors)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.fillna(0, inplace=True)  # Fill missing values

    # Convert categorical columns to numeric using Label Encoding
    label_encoders = {}
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le  # Store encoders if needed later

    return df, label_encoders

if __name__ == "__main__":
    df, label_encoders = load_and_preprocess_data("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    df.to_csv("processed_churn.csv", index=False)  # Save cleaned data
    print(df.head())  # Check output
