import pandas as pd

# Load student dataset
data = pd.read_csv("students.csv")

print("===== Student Performance Dataset =====")
print(data)

# Calculate average marks
data["Average"] = (
    data["Maths"] + data["Science"] + data["English"]
) / 3

print("\n===== Average Marks =====")
print(data[["Name", "Average"]])

# Filter students with average above 80
high_performers = data[data["Average"] > 80]

print("\n===== Students with Average Above 80 =====")
print(high_performers[["Name", "Average"]])

# Find highest performer
top_student = data.loc[data["Average"].idxmax()]

print("\n===== Top Performer =====")
print("Name:", top_student["Name"])
print("Average:", round(top_student["Average"], 2))
