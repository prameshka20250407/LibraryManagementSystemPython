import os.path
from validations import validate_book_id, validate_isbn_no
import csv

#All book functions(add, edit, search)

def add_book():
    book_id = ""
    isbn_no = ""
    title = ""
    no_of_copies = 0
    available_amount = 0
    price = 0
    while True:
        book_id = validate_book_id()
        if book_id is None:
            return
        is_unique = True
        try:
            with open("book.csv", "r") as books:
                reader = csv.reader(books)
                for row in reader:
                    if row and row[0] == book_id:
                        is_unique = False
                        break
        except FileNotFoundError:
            is_unique = True
        if not is_unique:
            print("\nError: Book ID already exists.")
            continue
        break
    isbn_no = validate_isbn_no()
    if isbn_no is None:
        return

    while True:
        title = str(input("Enter Title: "))
        if len(title) > 20:
            print("\nError: Enter only 20 characters")
            continue
        if not title.replace(" ", "").isalpha():
            print("\nError: Enter only letters")
            continue
        print("\nValid title")
        break

    while True:
        no_of_copies_input = (input("Enter Number of copies: "))
        if not (no_of_copies_input.isdigit()):
            print("\nError: Enter only digits")
            continue
        no_of_copies = int(no_of_copies_input)
        if no_of_copies > 2:
            print("\nError: Maximum can only be 2")
            continue
        print("\nValid no of copies")
        break
    available_amount = no_of_copies

    while True:
        price_input = (input("Enter Price: "))
        try:
            price = float(price_input)
        except ValueError:
            print("\nError: Enter only numerics")
            continue
        if "." not in price_input or len(price_input.split(".")[1]) != 2:
            print("\nError: Price must have 2 decimal digits")
            continue
        print("\nValid price")
        break

    with open('book.csv', 'a', newline='') as books:
        writer = csv.writer(books)
        writer.writerow([book_id, isbn_no, title, no_of_copies, available_amount, price])
    print("\nRecord saved successfully")


def search_book():
    book_id = validate_book_id()
    if book_id is None:
        return
    if not os.path.exists("book.csv"):
        print("\nError: No records found")
        return
    found = False
    try:
        with open('book.csv', mode='r', newline='') as books:
            reader = csv.reader(books)
            for row in reader:
                if not row:
                    continue
                if row[0] == book_id:
                    found = True
                    print("\n--- Book Details ---")
                    print(f"Book ID:            {row[0]}")
                    print(f"ISBN:               {row[1]}")
                    print(f"Title:              {row[2]}")
                    print(f"No of Copies:       {row[3]}")
                    print(f"Available amount:   {row[4]}")
                    print(f"Price:             ${row[5]}")
                    break
            if not found:
                print("\nError: Book not found")
                return
    except Exception as e:
        print(f"\nAn error occurred: {e}")


def edit_book():
    while True:
        book_id = validate_book_id()
        if book_id is None:
            return

        records = []
        header = []
        book_record = None

        try:
            with open('book.csv', mode='r', newline='') as books:
                reader = csv.reader(books)
                header = next(reader)

                if header is None:
                    print("\nError: No records found")
                    return

                for row in reader:
                    if row and row[0] == book_id:
                        book_record = row
                    records.append(row)
        except FileNotFoundError:
            print("\nError: No records found")
            return

        if book_record is None:
            print("\nError: No records found. Please try again.")
            continue
        break

    while True:
        print("\n--- Edit Book Menu ---")
        print("1. Edit ISBN")
        print("2. Edit Title")
        print("3. Edit Copies")
        print("4. Edit Price")
        print("5. Exit")
        userchoice = input("Please select what you want to edit: ")
        edited = False

        if userchoice == "1":
            new_isbn = validate_isbn_no()
            if new_isbn is None:
                continue
            book_record[1] = new_isbn
            edited = True

        elif userchoice == "2":
            while True:
                new_title = input("Enter New Title: ")
                if len(new_title) > 20:
                    print("\nError: Maximum only 20 characters")
                    continue
                if not new_title.replace(" ", "").isalpha():
                    print("\nError: Enter only letters")
                    continue
                book_record[2] = new_title
                edited = True
                break

        elif userchoice == "3":
            while True:
                new_copies_input = input("Enter New no of copies: ")

                if not (new_copies_input.isdigit()):
                    print("\nError: Enter only digits")
                    continue

                new_copies = int(new_copies_input)
                if new_copies > 2:
                    print("\nError: Maximum can only be 2")
                    continue

                current_copies = int(book_record[3])
                current_available = int(book_record[4])
                issued_count = current_copies - current_available
                if new_copies < issued_count:
                    print("\nError: Cannot reduce copies below issued amount")
                    continue

                book_record[3] = str(new_copies)
                book_record[4] = str(new_copies - issued_count)
                edited = True
                break

        elif userchoice == "4":
            while True:
                price_input = input("Enter new Price: ")

                try:
                    float(price_input)
                except ValueError:
                    print("\nError: Enter only numerics")
                    continue

                if "." not in price_input or len(price_input.split(".")[1]) != 2:
                    print("\nError: Price must have 2 decimal places")
                    continue

                book_record[5] = price_input
                edited = True
                break

        elif userchoice == "5":
            print("\nExiting edit menu...")
            return

        else:
            print("\nError: Invalid input")
            continue

        if edited:
            with open('book.csv', 'w', newline='') as books:
                writer = csv.writer(books)
                writer.writerow(header)
                for row in records:
                    if row and row[0] == book_id:
                        writer.writerow(book_record)
                    else:
                        writer.writerow(row)
            print("\nBook record saved successfully")














