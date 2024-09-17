import pandas as pd

# Load data from a CSV file
data = pd.read_csv('data.csv')

# View the first few rows of the data
print("First 5 rows of the data:")
print(data.head())

# Get information about the dataset (columns, types, non-null counts)
print("\nDataset info:")
print(data.info())

# Check for missing values in each column
print("\nMissing values in each column:")
print(data.isnull().sum())

# Fill missing values with the mean of the respective column (for numerical columns)
data.fillna(data.mean(), inplace=True)

# Filter data (e.g., rows where column 'age' is greater than 30)
filtered_data = data[data['age'] > 30]

# Perform some analysis - e.g., calculate the average of 'salary' column
average_salary = data['salary'].mean()
print(f"\nAverage salary: {average_salary}")

# Group data by a column and calculate aggregate statistics (e.g., average salary by department)
grouped_data = data.groupby('department')['salary'].mean()
print("\nAverage salary by department:")
print(grouped_data)

# Save the cleaned and processed data to a new CSV file
data.to_csv('cleaned_data.csv', index=False)
