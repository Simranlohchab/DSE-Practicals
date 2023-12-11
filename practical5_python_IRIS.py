import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy import stats

plt.ion()

# Define the conf_interval function
def conf_interval(x):
    return stats.t.interval(0.95, len(x)-1, loc=np.mean(x), scale=stats.sem(x))

# Download the Iris dataset from sklearn
iris = datasets.load_iris()
iris_data = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

# a. Load data into pandas data frame. Use pandas.info() method to look at the info on datatypes in the dataset.
print("a. Info on Datatypes in the Dataset:")
print(iris_data.info())

# b. Find the number of missing values in each column
missing_values = iris_data.isnull().sum()
print("\nb. Number of Missing Values in Each Column:")
print(missing_values)

# c. Plot bar chart to show the frequency of each class label in the data.
plt.figure(figsize=(8, 6))
sns.countplot(x='target', data=iris_data)
plt.title("c. Frequency of Each Class Label")
plt.xlabel("Class Label")
plt.ylabel("Frequency")
plt.savefig('frequency.png')
plt.show()
plt.show(block=True)


# d. Draw a scatter plot for Petal Length vs Sepal Length and fit a regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='sepal length (cm)', y='petal length (cm)', data=iris_data)
plt.title("d. Scatter Plot: Petal Length vs Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.savefig('petal length and sepal length.png')
plt.show()
plt.show(block=True)


# e. Plot density distribution for feature Petal width.
plt.figure(figsize=(8, 6))
sns.kdeplot(iris_data['petal width (cm)'], fill=True)
plt.title("e. Density Distribution for Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Density")
plt.savefig('plot density distribution.png')
plt.show()
plt.show(block=True)


# f. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset.
plt.figure(figsize=(10, 8))
sns.pairplot(iris_data, hue='target')
plt.suptitle("f. Pairwise Bivariate Distribution in the Iris Dataset")
plt.savefig('pairwise bivariate distribution.png')
plt.show()
plt.show(block=True)


# g. Draw heatmap for any two numeric attributes
plt.figure(figsize=(8, 6))
sns.heatmap(iris_data[['sepal length (cm)', 'sepal width (cm)']].corr(), annot=True, cmap='coolwarm')
plt.title("g. Heatmap for Sepal Length and Sepal Width")
plt.savefig('heatmap.png')
plt.show()
plt.show(block=True)

# h. Compute mean, mode, median, standard deviation, confidence interval, and standard error for each numeric feature
numeric_features = iris_data.drop('target', axis=1)
numeric_stats = pd.DataFrame(index=numeric_features.columns)

numeric_stats['Mean'] = numeric_features.mean()
numeric_stats['Mode'] = numeric_features.mode().iloc[0]
numeric_stats['Median'] = numeric_features.median()
numeric_stats['Standard Deviation'] = numeric_features.std()

# Apply the confidence interval function
conf_interval_columns = numeric_features.apply(conf_interval)

# Separate the result into lower and upper bounds
numeric_stats['Confidence Interval Lower'] = conf_interval_columns.apply(lambda x: x[0])
numeric_stats['Confidence Interval Upper'] = conf_interval_columns.apply(lambda x: x[1])

numeric_stats['Standard Error'] = numeric_features.sem()

print("\nh. Descriptive Statistics for Each Numeric Feature:")
print(numeric_stats)


# i. Compute correlation coefficients between each pair of features and plot heatmap
correlation_matrix = numeric_features.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("i. Correlation Coefficients Between Each Pair of Features")
plt.savefig('correlation coefficient.png')
plt.show()
plt.show(block=True)

