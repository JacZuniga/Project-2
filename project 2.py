import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Load the data
df = pd.read_csv('vgchartz.csv')

# Clean the data: Remove rows where 'shipped' is NaN
df = df.dropna(subset=['shipped'])

# Group by platform and calculate the mean number of copies shipped
platform_shipped = df.groupby('platform')['shipped'].mean().sort_values(ascending=False)

# Visualize the data
plt.figure(figsize=(12, 6))
sns.barplot(x=platform_shipped.index, y=platform_shipped.values)
plt.title('Average Number of Copies Shipped by Platform')
plt.xlabel('Platform')
plt.ylabel('Average Copies Shipped (Millions)')
plt.xticks(rotation=45)
plt.show()

# Perform ANOVA test to check for significant differences between platforms
platforms = df['platform'].unique()
grouped_data = [df[df['platform'] == platform]['shipped'] for platform in platforms]

f_statistic, p_value = f_oneway(*grouped_data)

print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

# Interpret the results
if p_value < 0.05:
    print("There is a statistically significant difference in the number of copies shipped across platforms.")
else:
    print("There is no statistically significant difference in the number of copies shipped across platforms.")
    
# Plot a boxplot to visualize the distribution of copies shipped across platforms
plt.figure(figsize=(14, 6))
sns.boxplot(x=df['platform'], y=df['shipped'], showfliers=False)  # Exclude outliers for better visualization
plt.title('Distribution of Copies Shipped by Platform')
plt.xlabel('Platform')
plt.ylabel('Copies Shipped (Millions)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()