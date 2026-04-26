import csv

def validate_book_id():
    attempts = 0
    while attempts < 3:
        print("\nEnter book ID (Only 3 invalid format attempts are allowed)")
        book_id = input("Book ID: ")
        if len(book_id) != 4:
            print("\nError: Length should be 4.")
            attempts = attempts + 1
            continue
        if not book_id[:2].isalpha():
            print("\nError: 1st 2 characters should be letters")
            attempts = attempts + 1
            continue
        if not book_id[2:].isdigit():
            print("\nError: last 2 characters should be digits")
            attempts = attempts + 1
            continue
        print("\nBook ID format is valid.")
        return book_id
    print("\nToo many invalid attempts. Returning to menu.")
    return None


def validate_isbn_no():
    attempts = 0
    while attempts < 3:
        print("\nEnter ISBN No (Only 3 invalid format attempts are allowed)")
        isbn_no = input("ISBN No: ")
        if len(isbn_no) != 13:
            print("\nError: Length should be only 13.")
            attempts = attempts + 1
            continue
        if not isbn_no.isdigit():
            print("\nError: Only digits can be entered.")
            attempts = attempts + 1
            continue
        total_sum = 0
        position = 0
        while position <= 11:
            digit = int(isbn_no[position])
            if (position + 1) % 2 != 0:
                total_sum += digit *1
            else:
                total_sum += digit *3
            position += 1
        check_digit = (10 - (total_sum % 10)) % 10
        thirteenth_digit = int(isbn_no[12])
        if thirteenth_digit != check_digit:
            print("\nError: Invalid ISBN No.")
            attempts = attempts + 1
            continue
        else:
            print("\nISBN No is valid.")
            return isbn_no
    print("\nToo many invalid attempts. Returning to menu.")
    return None


def validate_student_id():
    attempts = 0
    while attempts < 3:
        print("\nEnter Student ID (Only 3 invalid format attempts are allowed)")
        student_id = input("Student ID: ")
        if len(student_id) != 8:
            print("\nError: Length should be 8.")
            attempts = attempts + 1
            continue
        if not student_id.isdigit():
            print("\nError: Characters should be numeric.")
            attempts = attempts + 1
            continue
        print("\nStudent ID format is valid.")
        return student_id
    print("\nToo many invalid attempts. Returning to menu.")
    return None

