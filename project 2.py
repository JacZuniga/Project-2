import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Video Games Sales.csv')

# One-hot encode the 'Platform' column
data_encoded = pd.get_dummies(data, columns=['Platform'], drop_first=True)

# Define the independent variables (X) and dependent variable (y)
X = data_encoded.drop(columns=['Global', 'Game Title', 'Year', 'Genre', 'Publisher', 'North America', 'Europe', 'Japan', 'Rest of World', 'Review'])
y = data_encoded['Global']

# Add a constant to the independent variables (for the intercept term)
X = sm.add_constant(X)

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print the regression summary
print(model.summary())

# Visualize the relationship between platform and global sales
plt.figure(figsize=(12, 6))
sns.boxplot(x='Platform', y='Global', data=data, palette='viridis')
plt.title('Global Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Global Sales (in millions)')
plt.xticks(rotation=45)
plt.show()