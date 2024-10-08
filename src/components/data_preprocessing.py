

import pandas as pd
import os
from src.utils import connect_to_db, close_connection
from sklearn.preprocessing import LabelEncoder, StandardScaler

def fetch_data_from_db(query):
    """Fetch data from PostgreSQL database using the provided query."""
    connection = connect_to_db()
    if connection is None:
        print("Failed to connect to the database.")
        return None
    
    try:
        df = pd.read_sql(query, connection)
        print("Data fetched successfully from the database.")
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        df = None
    finally:
        close_connection(connection)
    
    return df


def preprocess_data(df):
    """Preprocess the dataset: handle missing values, encode features, scale features."""
    
    
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].median())
    
    
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
   
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    
   
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    return df


def main():
    
    query = "SELECT * FROM transactions LIMIT 1000;"  # Adjust the query as needed
    
    
    df = fetch_data_from_db(query)
    if df is None:
        return
    
    print(f"Data fetched successfully. Shape: {df.shape}")
    
   
    df = preprocess_data(df)
    print(f"Data preprocessing complete. Shape: {df.shape}")

if __name__ == "__main__":
    main()

