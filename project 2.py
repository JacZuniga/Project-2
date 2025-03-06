import os 
import scipy
import seaborn as sns
import joypy
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import chi2_contingency, ttest_ind
# Opening file
file_name = "vgchartz.csv"
vgchartz_df = pd.read_csv(file_name)
print(vgchartz_df.head())

file_name2 = "Video Games Sales.csv"
gs_df = pd.read_csv(file_name2)
print(gs_df.head())

# Chi-Square Test: Creating a contingency table
contingency_table = pd.crosstab(vgchartz_df["platform"], vgchartz_df["shipped"].notna())  
chi2_stat, p_chi2, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-Square Statistic: {chi2_stat}, p-value: {p_chi2}")

# T-Test: Comparing shipments between PC and NS
pc_shipments = vgchartz_df[vgchartz_df["platform"] == "PC"]["shipped"].dropna()
ns_shipments = vgchartz_df[vgchartz_df["platform"] == "NS"]["shipped"].dropna()

t_stat, p_ttest = ttest_ind(pc_shipments, ns_shipments, equal_var=False)  # Welch's t-test
print(f"T-Test Statistic: {t_stat}, p-value: {p_ttest}")

# Set style
sns.set_style("whitegrid")

# Bar Chart: Total Shipments by Platform
plt.figure(figsize=(12, 6))
platform_shipment_totals = vgchartz_df.groupby("platform")["shipped"].sum().dropna().sort_values(ascending=False)
sns.barplot(x=platform_shipment_totals.index, y=platform_shipment_totals.values, palette="viridis")
plt.xticks(rotation=90)
plt.xlabel("Platform")
plt.ylabel("Total Shipments (in millions)")
plt.title("Total Game Shipments by Platform")
plt.show()

# Box Plot: Distribution of Shipments for PC vs. NS
plt.figure(figsize=(8, 6))
sns.boxplot(data=vgchartz_df[vgchartz_df["platform"].isin(["PC", "NS"])], x="platform", y="shipped", palette="pastel")
plt.xlabel("Platform")
plt.ylabel("Shipments (in millions)")
plt.title("Comparison of Shipments: PC vs. NS")
plt.show()
