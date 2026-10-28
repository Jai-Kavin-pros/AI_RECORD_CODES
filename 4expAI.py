import csv

student_records = [
    {"RollNo": "KY04", "Name": "Jai Kavin", "Department": "CSE", "Mark": 94},
    {"RollNo": "DE48", "Name": "Siddharthan", "Department": "Mech", "Mark": 91},
    {"RollNo": "UE54", "Name": "Rahul", "Department": "ECE", "Mark": 78}
]

# Tuple example: fixed course details
course_details = ("Python", 4)
print("Course Tuple:", course_details)

# Write text file
with open("students.txt", "w") as text_file:
    for student_data in student_records:
        text_file.write(str(student_data) + "\n")

# Write CSV file
with open("students.csv", "w", newline="") as csv_file:
    field_names = ["RollNo", "Name", "Department", "Mark"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(student_records)

# Read CSV file
print("\n--- Records from CSV ---")
with open("students.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for student_row in csv_reader:
        print(student_row["RollNo"], student_row["Name"],
              student_row["Department"], student_row["Mark"])