import pandas as pd
from severity_score import add_severity_level_and_crimeID

input_csv_path = '../Data/Criminal_Offences.csv'
output_csv_path = '../Data/Criminal_Offences_Cleaned.csv'

columns_to_remove = ['FID', 'ReportDate', 'Year', 'ReportTime', 'Occur_Time', 'OffSummary', 'Weekday', 'Sector', 'Division', 'CensusTra']

# Read the CSV file into a DataFrame, addressing potential DtypeWarning with low_memory=False
df = pd.read_csv(input_csv_path, low_memory=False)

# Remove the specified columns
df.drop(columns=columns_to_remove, inplace=True, errors='ignore')

# Format OccurDate as a PostgreSQL-compatible date string (YYYY-MM-DD)
df['OccurDate'] = pd.to_datetime(df['OccurDate']).dt.date

# Generate a unique ID for each location in the Neighbourh column
df['locationID'], _ = pd.factorize(df['Neighbourh'])

# Call the function to add the severity level and CrimeID columns
df = add_severity_level_and_crimeID(df, 'PrimViolat')

# Save the modified DataFrame back to a new CSV file
df.to_csv(output_csv_path, index=False)

print(f'CSV file has been processed and saved to {output_csv_path}.')