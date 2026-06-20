import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

print("Original Dataset:")
print(df)

# Store original row count
original_rows = len(df)

# Fill missing Name values
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing Sales values with average sales
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

# Count duplicates
duplicate_count = df.duplicated().sum()

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Generate statistics
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
maximum_sales = df["Sales"].max()
minimum_sales = df["Sales"].min()

# Create report file
with open("summary_report.txt", "w") as file:
    file.write("DATA CLEANING & REPORTING AUTOMATION\n")
    file.write("===================================\n\n")
    file.write(f"Original Rows: {original_rows}\n")
    file.write(f"Duplicates Removed: {duplicate_count}\n")
    file.write(f"Final Rows: {len(df)}\n\n")

    file.write("SALES SUMMARY\n")
    file.write("-------------\n")
    file.write(f"Total Sales: {total_sales:.2f}\n")
    file.write(f"Average Sales: {average_sales:.2f}\n")
    file.write(f"Maximum Sales: {maximum_sales:.2f}\n")
    file.write(f"Minimum Sales: {minimum_sales:.2f}\n")

# Create Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Sales"])
plt.title("Sales Report")
plt.xlabel("Employees")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_chart.png")

print("\nData Cleaning Completed Successfully!")
print("Files Generated:")
print("1. cleaned_data.csv")
print("2. summary_report.txt")
print("3. sales_chart.png")