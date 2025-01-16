
import pandas as pd

# Load the claims data
df = pd.read_csv("claims_data.csv")

# Clean the data (handling missing and duplicate entries)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Validate Diagnosis Codes
valid_codes = ['A01', 'B02', 'C03']
df['Valid Diagnosis'] = df['Diagnosis Code'].apply(lambda x: x in valid_codes)

# Output invalid diagnosis codes
invalid_codes = df[df['Valid Diagnosis'] == False]
print(f"Invalid diagnosis codes: {len(invalid_codes)}")
