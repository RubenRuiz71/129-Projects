
# Code to write grades to a plain text file
grades = []

print("Enter grades one by one (type 'done' when finished):")
while True:
    user_input = input("Enter a grade: ")
    if user_input.lower() == 'done':
        break
    try:
        grade = float(user_input)
        grades.append(grade)
    except ValueError:
        print("Invalid input. Please enter a numeric grade or 'done'.")

# Save grades to a text file
file_path_grades = "/mnt/data/grades.txt"
with open(file_path_grades, "w") as file:
    for grade in grades:
        file.write(f"{grade}\n")

file_path_grades


import csv

# Predefined student records for simulation
students = [
    ("John", "Doe", 85, 90, 78),
    ("Jane", "Smith", 92, 88, 94),
    ("Emily", "Johnson", 76, 84, 80),
    ("Michael", "Brown", 89, 91, 87),
    ("Sarah", "Davis", 95, 93, 96)
]

# Path to the CSV file
file_path_csv = "/mnt/data/grades.csv"

# Write student records to a CSV file
with open(file_path_csv, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write header
    csvwriter.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])
    # Write student data
    csvwriter.writerows(students)

file_path_csv
