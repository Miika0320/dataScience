import pandas as pd
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

def upload_csv_to_supabase_in_batches(csv_file_path, table_name, supabase_url, supabase_key, batch_size=100):
    supabase = create_client(supabase_url, supabase_key)
    df = pd.read_csv(csv_file_path)
    data = df.to_dict(orient='records')

    # Insert data in batches
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        response = supabase.table(table_name).insert(batch).execute()
        if response.error:
            print(f"Failed to upload batch: {response.error.message}")
        else:
            print(f"Successfully uploaded batch {i//batch_size + 1}")



supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

if not supabase_url or not supabase_key:
    print("Supabase URL or key not set in environment variables.")
else:
    # Path to your CSV file
    csv_file_path = '../Data/Criminal_Offences_Cleaned.csv'

    # Your Supabase table name
    table_name = 'Criminal Offences'

    # Call the function to upload the CSV data to Supabase
    upload_csv_to_supabase_in_batches(csv_file_path, table_name, supabase_url, supabase_key)
