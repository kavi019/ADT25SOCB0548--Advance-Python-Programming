import pandas as pd

# Read the original CSV file
df = pd.read_csv('students_all_data.csv')

# Extract only the required columns
extracted_df = df[['Student Name', 'Roll Number', 'Marks']]

# Save the extracted data into a new CSV file
extracted_df.to_csv('students_extracted.csv', index=False)

print("Selected columns successfully extracted using Pandas.")