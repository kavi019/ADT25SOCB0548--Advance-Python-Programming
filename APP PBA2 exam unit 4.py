import pandas as pd
import matplotlib.pyplot as plt

# 1. Read employee details from the CSV file
df = pd.read_csv('employee.csv')

# 2. Display employee names, departments, and salaries
print(df[['Name', 'Department', 'Salary']])

# 3. Calculate the average salary for each department
avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)

# Plot using Matplotlib
avg_salary.plot(kind='bar')
plt.show()