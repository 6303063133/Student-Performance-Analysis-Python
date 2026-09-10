# Student Performance Analysis
# Author: Supriya Gundepalli

students = [
    {"name": "Rahul", "maths": 85, "science": 78, "english": 82},
    {"name": "Priya", "maths": 92, "science": 88, "english": 90},
    {"name": "Arun", "maths": 70, "science": 75, "english": 68},
    {"name": "Sneha", "maths": 95, "science": 91, "english": 94},
    {"name": "Kiran", "maths": 60, "science": 65, "english": 58}
]

print("===== Student Performance Analysis =====")

for student in students:
    total = student["maths"] + student["science"] + student["english"]
    average = total / 3

    print("\nStudent:", student["name"])
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))

    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 60:
        print("Grade: C")
    else:
        print("Grade: Fail")
