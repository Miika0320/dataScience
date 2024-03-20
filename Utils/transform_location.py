import pandas as pd

# Assuming your CSV file has no header, and you're naming the columns 'Neighborhood' and 'ID'
# Adjust the `names` parameter based on your actual CSV structure
# If your CSV has a header row, you can remove the `names` parameter and header=None
df = pd.read_csv('../Data/location.csv', header=None, names=['Neighborhood', 'ID'])

# Drop duplicate rows
df_unique = df.drop_duplicates()

# Print the unique rows
print(df_unique)

# Optionally, save the unique rows back to a new CSV file
df_unique.to_csv('../Data/location_cleaned.csv', index=False, header=False)