# titanic_eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set seaborn style
sns.set(style="whitegrid")

# Load dataset
df = pd.read_csv('Titanic_Data.csv')

# 1. Basic Info
print("✅ First 5 Rows:\n", df.head())
print("\nℹ️ Data Info:")
df.info()
print("\n🔍 Missing Values:\n", df.isnull().sum())

# 2. Visualize Missing Values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.tight_layout()
plt.savefig('images/missing_values.png')
plt.show()

# 3. Describe Numerical Columns
print("\n📊 Statistical Summary:\n", df.describe())

# 4. Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'].dropna(), kde=True, bins=30, color='skyblue')
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('images/age_distribution.png')
plt.show()

# 5. Countplot of Survival
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Survived', palette='pastel')
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.tight_layout()
plt.savefig('images/survival_count.png')
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig('images/correlation_heatmap.png')
plt.show()

# 7. Age vs Survived
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Survived', y='Age', palette='Set2')
plt.title("Age Distribution by Survival")
plt.tight_layout()
plt.savefig('images/age_vs_survived.png')
plt.show()

# 8. Sex vs Survival
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Sex', hue='Survived', palette='Set1')
plt.title("Survival Count by Gender")
plt.tight_layout()
plt.savefig('images/sex_vs_survival.png')
plt.show()

print("✅ All visualizations saved in the 'images/' folder.")
