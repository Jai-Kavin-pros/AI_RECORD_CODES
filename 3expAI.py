student_records = {}

def add_student():
    roll_no = input("Enter Roll No: ")
    student_name = input("Enter Name: ")
    department = input("Enter Department: ")
    student_records[roll_no] = {"Name": student_name, "Department": department}
    print("Student added successfully.")

def view_students():
    if not student_records:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for roll_number, student_data in student_records.items():
        print("Roll No:", roll_number,
              "| Name:", student_data["Name"],
              "| Department:", student_data["Department"])

def search_student():
    roll_no = input("Enter Roll No to search: ")
    if roll_no in student_records:
        print(student_records[roll_no])
    else:
        print("Student not found.")

def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    if roll_no in student_records:
        del student_records[roll_no]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        add_student()
    elif user_choice == "2":
        view_students()
    elif user_choice == "3":
        search_student()
    elif user_choice == "4":
        delete_student()
    elif user_choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")