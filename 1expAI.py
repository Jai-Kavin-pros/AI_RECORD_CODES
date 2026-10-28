
student_name = input("Enter student name: ")
num_subjects = int(input("Enter number of subjects: "))
total_marks = 0
for subject_num in range(1, num_subjects + 1):
    subject_mark = float(input(f"Enter mark for Subject {subject_num}: "))
    total_marks += subject_mark
student_percentage = total_marks / num_subjects
if student_percentage >= 90:
    student_grade = "A+"
    performance_level = "Outstanding"
elif student_percentage >= 80:
    student_grade = "A"
    performance_level = "Excellent"
elif student_percentage >= 70:
    student_grade = "B"
    performance_level = "Very Good"
elif student_percentage >= 60:
    student_grade = "C"
    performance_level = "Good"
elif student_percentage >= 50:
    student_grade = "D"
    performance_level = "Average"
else:
    student_grade = "F"
    performance_level = "Needs Improvement"
print("\n--- Academic Performance ---")
print("Student Name :", student_name)
print("Total Marks :", total_marks)
print("Percentage :", round(student_percentage, 2), "%")
print("Grade :", student_grade)
print("Performance :", performance_level)