# Import the pandas library
import pandas as pd

# 1. Creating a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Salary": [50000, 60000, 70000, 80000]
}

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# 2. Reading and Writing Data
# Writing the DataFrame to a CSV file
df.to_csv("data.csv", index=False)  # index=False prevents writing row numbers

# Reading the CSV file back into a DataFrame
df_csv = pd.read_csv("data.csv")

print("DataFrame read from CSV:")
print(df_csv)
print("\n")

# 3. Selecting Columns and Rows
print("Selecting the 'Name' column:")
print(df["Name"])
print("\n")

print("Selecting rows where Age > 30:")
print(df[df["Age"] > 30])
print("\n")

# 4. Adding a New Column
df["Experience"] = [2, 5, 8, 10]
print("DataFrame after adding 'Experience' column:")
print(df)
print("\n")

# 5. Updating a Column
df["Salary"] = df["Salary"] * 1.1  # Increase salary by 10%
print("DataFrame after updating 'Salary' column:")
print(df)
print("\n")

# 6. Deleting a Column
df.drop(columns=["City"], inplace=True)
print("DataFrame after deleting 'City' column:")
print(df)
print("\n")

# 7. Sorting the DataFrame by Age
df_sorted = df.sort_values(by="Age", ascending=False)
print("DataFrame sorted by Age in descending order:")
print(df_sorted)
print("\n")

# 8. Filtering Data
filtered_df = df[df["Experience"] > 5]
print("Filtered DataFrame (Experience > 5):")
print(filtered_df)
print("\n")

# 9. Grouping and Aggregation
grouped = df.groupby("Experience")["Salary"].mean().to_frame(name="Avg Salary")
print("Average Salary by Experience:")
print(grouped)
print("\n")

# 10. Handling Missing Values
df_missing = df.copy()
df_missing.loc[1, "Salary"] = None  # Introduce a missing value
print("DataFrame with a missing value:")
print(df_missing)
print("\n")

# Fill missing values with the average salary
df_missing["Salary"].fillna(df_missing["Salary"].mean(), inplace=True)
print("DataFrame after filling missing values:")
print(df_missing)



# Sample Data
data = {
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance"],
    "Salary": [60000, 50000, 80000, 70000, 55000, 90000]
}

df = pd.DataFrame(data)

# Fix column names (remove spaces)
df.columns = df.columns.str.strip()

# Ensure 'Department' exists before pivoting
if "Department" in df.columns:
    pivot_table = df.pivot_table(values="Salary", index="Department", aggfunc=["mean", "max", "min", "sum"])
    print(pivot_table)
else:
    print("Error: Column 'Department' not found in DataFrame!")
