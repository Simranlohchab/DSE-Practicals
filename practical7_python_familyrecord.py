import pandas as pd

# Sample data
data = {'FamilyName': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats', 'Kumar', 'Shah', 'Shah', 'Kumar', 'Vats'],
        'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
        'MonthlyIncome': [44000.00, 65000.00, 43150.00, 66500.00, 255000.00, 103000.00, 55000.00, 112400.00, 81030.00, 71900.00]}

df = pd.DataFrame(data)

# a. Calculate and display familywise gross monthly income.
familywise_income = df.groupby('FamilyName')['MonthlyIncome'].sum()
print("a. Familywise Gross Monthly Income:")
print(familywise_income)

# b. Display the highest and lowest monthly income for each family name
highest_lowest_income = df.groupby('FamilyName')['MonthlyIncome'].agg(['max', 'min'])
print("\nb. Highest and Lowest Monthly Income for Each Family Name:")
print(highest_lowest_income)

# c. Calculate and display monthly income of all members earning income less than Rs. 80000.00.
low_income_members = df[df['MonthlyIncome'] < 80000.00]
print("\nc. Monthly Income of Members Earning Less than Rs. 80000.00:")
print(low_income_members[['FamilyName', 'MonthlyIncome']])

# d. Display total number of females along with their average monthly income
female_stats = df[df['Gender'] == 'Female'].groupby('Gender').agg({'MonthlyIncome': ['count', 'mean']})
print("\nd. Total Number of Females and Their Average Monthly Income:")
print(female_stats)

# e. Delete rows with Monthly income less than the average income of all members
average_income = df['MonthlyIncome'].mean()
df = df[df['MonthlyIncome'] >= average_income]
print("\ne. DataFrame after Deleting Rows with Monthly Income Less than Average:")
print(df)
