import pandas as pd

# Read your TSV file
file_path = input("Enter the full path of your TSV file: ")

df = pd.read_csv(file_path, sep="\t", dtype=str)

print("Original dataset shape:", df.shape)

# Clean column names
df.columns = df.columns.str.strip()

# Remove completely empty rows
df = df.dropna(how="all")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove extra spaces from text
for col in df.columns:
    df[col] = df[col].str.strip()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Cleaning completed!")
print("Cleaned dataset shape:", df.shape)
print("Saved as cleaned_data.csv")