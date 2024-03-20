import pandas as pd
import re

def add_severity_level_and_crimeID(df, crime_code_col):
    severity_mapping = {
        11: 10,  # Violations Causing Death
        12: 9,   # Attempting the Commission of a Capital Crime
        13: 8,   # Sexual Violations
        14: 7,   # Assaults
        15: 9,   # Violations Resulting in the Deprivation of Freedom (e.g., kidnapping)
        16: 8,   # Other Violations Involving Violence or Threat (e.g., Robbery)
        21: 6,   # Crimes Against Property
        33: 5,   # Offensive Weapons
        34: 4,   # Misdemeanors I (e.g., counterfeit currency, trespassing)
        35: 3,   # Misdemeanors II (e.g., Fail to attend court, probation breach)
        377: 8,  # Offences Against the Person and Reputation
        374: 8,  # Sexual Offences, Public Morals and Disorderly Conduct
        378: 6,  # Offences Against the Rights of Property.
        40: 7    # Controlled Drugs and Substances Act
    }
    
    def extract_code(s):
        # Extracts the numeric part from the crime description string
        match = re.search(r'\((\d+)\)', s)
        return int(match.group(1)) if match else None
    
    def map_severity(code):
        # If the code can't be extracted, default to 0
        if code is None:
            return 0
        # Try with the first two digits
        if (severity := severity_mapping.get(code // 100)) is not None:
            return severity
        # Fallback to the first three digits
        return severity_mapping.get(code, 0)
    
    # Apply the function to extract the codes
    df['CrimeID'] = df[crime_code_col].apply(extract_code)
    # Fill missing values with a placeholder and convert to integers
    df['CrimeID'] = df['CrimeID'].fillna(-1).astype(int)
    # Map to severity level
    df['SeverityLevel'] = df['CrimeID'].apply(map_severity)
    
    return df
