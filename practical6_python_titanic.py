import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset from a local CSV file
titanic_data = pd.read_csv('/home/simran/titanic/Titanic-Dataset.csv')

# b. Find total number of passengers with age more than 30
passengers_over_30 = titanic_data[titanic_data['Age'] > 30]
total_passengers_over_30 = len(passengers_over_30)
print("\nb. Total number of passengers with age more than 30:", total_passengers_over_30)

# c. Find total fare paid by passengers of second class
total_fare_second_class = titanic_data[titanic_data['Pclass'] == 2]['Fare'].sum()
print("\nc. Total fare paid by passengers of second class:", total_fare_second_class)

# d. Compare the number of survivors of each passenger class
survivors_by_class = titanic_data.groupby('Pclass')['Survived'].sum()
print("\nd. Number of survivors of each passenger class:")
print(survivors_by_class)

# e. Compute descriptive statistics for the age attribute gender-wise
age_stats_by_gender = titanic_data.groupby('Sex')['Age'].describe()
print("\ne. Descriptive statistics for age attribute gender-wise:")
print(age_stats_by_gender)

# f. Draw a scatter plot for passenger fare paid by Female and Male passengers separately
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Fare', y='Sex', data=titanic_data)
plt.title("f. Scatter Plot: Passenger Fare by Gender")
plt.xlabel("Fare")
plt.ylabel("Gender")
plt.show()

# g. Compare density distribution for features age and passenger fare
plt.figure(figsize=(10, 8))
sns.kdeplot(titanic_data['Age'], label='Age', fill=True)
sns.kdeplot(titanic_data['Fare'], label='Fare', fill=True)
plt.title("g. Density Distribution for Age and Passenger Fare")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()

# h. Draw the pie chart for three groups labelled as class 1, class 2, class 3
class_counts = titanic_data['Pclass'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(class_counts, labels=['Class 1', 'Class 2', 'Class 3'], autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title("h. Distribution of Passenger Classes")
plt.show()

# i. Find % of survived passengers for each class
survival_percent_by_class = titanic_data.groupby('Pclass')['Survived'].mean() * 100
print("\ni. Percentage of survived passengers for each class:")
print(survival_percent_by_class)
