import pandas as pd
import seaborn as sns

# Load dataset
df = sns.load_dataset("titanic")

print("Original Data:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop rows where 'age' is missing
df = df.dropna(subset=['age'])

# Fill missing 'embarked' with most common value
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# Fill missing 'deck' with 'Unknown'
df['deck'] = df['deck'].fillna('Unknown')

# Convert 'survived' to int
df['survived'] = df['survived'].astype(int)

# Print cleaned data info
print("\nCleaned Data Info:")
print(df.info())

# Save cleaned file
df.to_csv("cleaned_titanic.csv", index=False)

print("\nCleaned dataset saved as cleaned_titanic.csv")