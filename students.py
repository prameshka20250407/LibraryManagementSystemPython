import csv
from validations import validate_student_id

#add student function

def add_student():
    while True:
        student_id = validate_student_id()
        if student_id is None:
            return
        exists = False
        try:
            with open("student.csv", "r", newline="") as students:
                reader = csv.reader(students)
                for row in reader:
                    if row and row[0] == student_id:
                        exists = True
                        break
        except FileNotFoundError:
            pass
        if exists:
            print("\nError: Student ID already exists.")
            continue

        while True:
            first_name = input("\nFirst Name: ").strip()
            if len(first_name) > 10:
                print("\nError: Enter only 10 characters")
                continue
            if not first_name.isalpha():
                print("\nError: Enter only one name with only letters")
                continue
            break
        with open("student.csv", "a", newline="") as students:
            writer = csv.writer(students)
            writer.writerow([student_id, first_name])
        print("\nRecord saved successfully")
        break





