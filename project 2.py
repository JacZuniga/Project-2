import pandas as pd
from scipy.stats import f_oneway
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Video Games Sales.csv')

# Group the data by Platform and calculate the sum of Global sales for each platform
platform_sales = data.groupby('Platform')['Global'].sum().reset_index()

# Perform ANOVA test
platforms = data['Platform'].unique()
grouped_data = [data[data['Platform'] == platform]['Global'] for platform in platforms]

# Perform ANOVA test
f_statistic, p_value = f_oneway(*grouped_data)

# Output the results
print(f"F-Statistic: {f_statistic}")
print(f"P-Value: {p_value}")

# Interpret the results
if p_value < 0.05:
    print("There is a significant correlation between platform and number of copies shipped.")
else:
    print("There is no significant correlation between platform and number of copies shipped.")

# 1. Bar Plot: Total Global Sales by Platform
plt.figure(figsize=(12, 6))
sns.barplot(x='Platform', y='Global', data=platform_sales, palette='viridis')
plt.title('Total Global Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Total Global Sales (in millions)')
plt.xticks(rotation=45)
plt.show()

# 2. Box Plot: Distribution of Global Sales by Platform
plt.figure(figsize=(12, 6))
sns.boxplot(x='Platform', y='Global', data=data, palette='viridis')
plt.title('Distribution of Global Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Global Sales (in millions)')
plt.xticks(rotation=45)
plt.show()