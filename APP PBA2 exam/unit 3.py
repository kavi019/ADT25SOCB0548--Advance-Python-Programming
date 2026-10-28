import pandas as pd

df = pd.read_csv('students_all_data.csv')

extracted_df = df[['Student Name', 'Roll Number', 'Marks']]

extracted_df.to_csv('students_extracted.csv', index=False)

print("Selected columns successfully extracted using Pandas.")
