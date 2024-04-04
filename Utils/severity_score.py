import pandas as pd
import re

def add_severity_level_and_crimeID(df, crime_code_col):
    severity_mapping = {
        11: 10,    # Violations Causing Death
        12: 8,     # Attempting the Commission of a Capital Crime
        13: 9,     # Sexual Violations
        14: 6.5,   # Assaults
        15: 8,     # Violations Resulting in the Deprivation of Freedom (e.g., kidnapping)
        16: 7,     # Other Violations Involving Violence or Threat (e.g., Robbery)
        17: 7,
        214: 2,    # Petty Crimes Against Property
        21: 4.5,   # Crimes Against Property
        31: 5,
        33: 4,     # Offensive Weapons
        34: 2,     # Misdemeanors I (e.g., counterfeit currency, trespassing) 
        35: 3,     # Misdemeanors II (e.g., Fail to attend court, probation breach)
        37: 3,     # Misdemeanors II (e.g., Fail to attend court, probation breach)
        377: 5.5,  # Offences Against the Person and Reputation
        374: 7,    # Sexual Offences, Public Morals and Disorderly Conduct
        378: 4.5,  # Offences Against the Rights of Property
        38: 4,
        40: 6      # Controlled Drugs and Substances Act
    }

    def extract_code(s):
        # Adjusts the regex to capture the first numeric sequence before any potential slash
        match = re.search(r'\((\d+)(?:/\d+)?\)', s)
        return int(match.group(1)) if match else None

    def map_severity(code):
        # Attempt to find an exact match first
        if (severity := severity_mapping.get(code)) is not None:
            return severity
        # Then try matching based on code length
        if len(str(code)) > 3 and (severity := severity_mapping.get(int(str(code)[:3]))) is not None:
            return severity
        # Lastly, fall back to matching the first two digits
        return severity_mapping.get(int(str(code)[:2]), 0)
    
    def clean_description(s):
        # Removes the numeric code and parentheses from the description, including handling slashes
        return re.sub(r'\s*\(\d+(?:/\d+)?\)', '', s).strip()

    # Apply the function to extract the codes
    df['CrimeID'] = df[crime_code_col].apply(extract_code)
    # Fill missing values with a placeholder and convert to integers
    df['CrimeID'] = df['CrimeID'].fillna(-1).astype(int)
    # Map to severity level
    df['SeverityLevel'] = df['CrimeID'].apply(map_severity)
    # Clean up the crime description by removing the code and parentheses, including any slashes within them
    df[crime_code_col] = df[crime_code_col].apply(clean_description)
    
    return df