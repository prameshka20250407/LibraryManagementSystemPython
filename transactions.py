import csv
from validations import validate_book_id, validate_student_id
import os
import pandas as pd
import plotly.express as px

#issue and return functions
#Trend Graph function

def issue_book():
    while True:
        book_id = validate_book_id()
        if book_id is None:
            return

        book_records = []
        header = []
        book_record = None

        try:
            with open('book.csv', mode='r', newline='') as books:
                reader = csv.reader(books)
                book_header = next(reader)

                if book_header is None:
                    print("\nError: No records found")
                    return

                for row in reader:
                    if row and row[0] == book_id:
                        book_record = row
                    book_records.append(row)
        except FileNotFoundError:
            print("\nError: No records found")
            return

        if book_record is None:
            print("\nError: Book not available, enter another book.")
            continue
        break

    while True:
        student_id = validate_student_id()
        if student_id is None:
            return

        student_records = []
        header = []
        student_record = None

        try:
            with open('student.csv', mode='r', newline='') as students:
                reader = csv.reader(students)
                student_header = next(reader)

                if student_header is None:
                    print("\nError: No records found")
                    return

                for row in reader:
                    if row and row[0] == student_id:
                        student_record = row
                    student_records.append(row)
        except FileNotFoundError:
            print("\nError: No records found")
            return

        if student_record is None:
            print("\nError: Student doesn't exist. Please try again.")
            continue
        break

    while True:
        date = input("Please input the date (DD/MM/YYYY): ").strip()

        if len(date) != 10:
            print("\nError: Invalid date length. Please try again.")
            continue

        if date[2] != '/' or date[5] != '/':
            print("\nError: Invalid format of date. Please try again (DD/MM/YYYY).")
            continue

        day_str = date[:2]
        month_str = date[3:5]
        year_str = date[6:]

        if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
            print("\nError: Date must contain numbers only. Please try again.")
            continue

        day = int(day_str)
        month = int(month_str)
        year = int(year_str)

        if month < 1 or month > 12:
            print("\nError: Invalid month. Please try again.")
            continue
        if day < 1 or day > 31:
            print("\nError: Invalid day. Please try again.")
            continue

        if month in [4, 6, 9, 11] and day > 30:
            print("\nError: Invalid day for the given month. Please try again.")
            continue

        if month == 2 and day > 29:
            print("\nError: Invalid day for February. Please try again.")
            continue
        break

    active_issue = 0
    try:
        with open('transactions.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row:
                    t_date, t_book_id, t_student_id, t_type = row
                    if t_book_id == book_id and t_student_id == student_id:
                        if t_type == '1':
                            active_issue += 1
                        elif t_type == '2':
                            active_issue -= 1

    except FileNotFoundError:
        pass

    if active_issue > 0:
        print("\nError: Book already issued to this student")
        return

    available_copies = int(book_record[4])
    if available_copies <= 0:
        print("\nError: Book is not available for issuing")
        return

    book_record[4] = str(available_copies -1)

    new_transactions = [date, book_id, student_id, "1"]
    try:
        with open('transactions.csv', mode='a', newline='') as transactions:
            writer = csv.writer(transactions)
            writer.writerow(new_transactions)

    except Exception as e:
        print(f"\nError: Failed to save transaction. {e}")
        return

    try:
        with open('book.csv', mode='w', newline='') as books:
            writer = csv.writer(books)
            writer.writerow(book_header)
            for row in book_records:
                if row[0] == book_id:
                    writer.writerow(book_record)
                else:
                    writer.writerow(row)
    except Exception as e:
        print(f"\nError: Failed to update book records. {e}")
        return
    print(f"\nSuccess: Book '{book_record[2]}' issued to student '{student_record[1]}' on {date}.")


def return_book():
    while True:
        book_id = validate_book_id()
        if book_id is None:
            return

        book_records = []
        header = []
        book_record = None

        try:
            with open('book.csv', mode='r', newline='') as books:
                reader = csv.reader(books)
                book_header = next(reader)

                if book_header is None:
                    print("\nError: No records found")
                    return

                for row in reader:
                    if row and row[0] == book_id:
                        book_record = row
                    book_records.append(row)
        except FileNotFoundError:
            print("\nError: No records found")
            return

        if book_record is None:
            print("\nError: No records found. Please try again.")
            continue
        break

    while True:
        student_id = validate_student_id()
        if student_id is None:
            return

        student_records = []
        header = []
        student_record = None

        try:
            with open('student.csv', mode='r', newline='') as students:
                reader = csv.reader(students)
                student_header = next(reader)

                if student_header is None:
                    print("\nError: No records found")
                    return

                for row in reader:
                    if row and row[0] == student_id:
                        student_record = row
                    student_records.append(row)
        except FileNotFoundError:
            print("\nError: No records found")
            return

        if student_record is None:
            print("\nError: Student doesn't exist. Please try again.")
            continue
        break

    active_issue = 0
    try:
        with open('transactions.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row:
                    t_date, t_book_id, t_student_id, t_type = row
                    if t_book_id == book_id and t_student_id == student_id:
                        if t_type == '1':
                            active_issue += 1
                        elif t_type == '2':
                            active_issue -= 1
    except FileNotFoundError:
        pass

    if active_issue <= 0:
        print("\nError: Book already returned or not issued")
        return

    while True:
        date = input("Please input the date (DD/MM/YYYY): ").strip()

        if len(date) != 10:
            print("\nError: Invalid date length. Please try again.")
            continue

        if date[2] != '/' or date[5] != '/':
            print("\nError: Invalid format of date. Please try again (DD/MM/YYYY).")
            continue

        day_str = date[:2]
        month_str = date[3:5]
        year_str = date[6:]

        if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
            print("\nError: Date must contain numbers only. Please try again.")
            continue

        day = int(day_str)
        month = int(month_str)
        year = int(year_str)

        if month < 1 or month > 12:
            print("\nError: Invalid month. Please try again.")
            continue
        if day < 1 or day > 31:
            print("\nError: Invalid day. Please try again.")
            continue

        if month in [4, 6, 9, 11] and day > 30:
            print("\nError: Invalid day for the given month. Please try again.")
            continue

        if month == 2 and day > 29:
            print("\nError: Invalid day for February. Please try again.")
            continue
        break

    available_copies = int(book_record[4])
    book_record[4] = str(available_copies + 1)

    new_transaction = [date, book_id, student_id, "2"]

    try:
        with open('transactions.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_transaction)
    except Exception as e:
        print(f"\nError: Failed to save transaction. {e}")
        return

    try:
        with open('book.csv', mode='w', newline='') as books:
            writer = csv.writer(books)
            writer.writerow(book_header)
            for row in book_records:
                if row[0] == book_id:
                    writer.writerow(book_record)
                else:
                    writer.writerow(row)
    except Exception as e:
        print(f"\nError: Failed to update book records. {e}")
        return

    print(f"\nSuccess: Book '{book_record[2]}' returned by student '{student_record[1]}' on {date}.")


def generate_trend_graph():
    print("\nGenerating trend graph...")

    if not os.path.exists("transactions.csv"):
        print("\nError: No transaction file found")
        return

    try:
        df = pd.read_csv("transactions.csv")
    except Exception as e:
        print(f"\nError: Failed to load transaction file. {e}")
        return

    if df.empty:
        print("\nError: No transaction data available.")
        return

    required_columns = ["date", "book_id", "student_id", "type"]
    for col in required_columns:
        if col not in df.columns:
            print("\nError: Invalid transactions file format")
            return

    df["type"] = df["type"].astype(int)
    issued_df = df[df["type"] == 1]
    if issued_df.empty:
        print("\nError: No issued books to display")
        return

    try:
        issued_df = issued_df.copy()
        issued_df["date"] = pd.to_datetime(issued_df["date"], format="%d/%m/%Y")
    except Exception:
        print("\nError: Invalid date format in transactions")
        return

    grouped_data = issued_df.groupby("date").size().reset_index(name="count")
    grouped_data = grouped_data.sort_values(by="date")

    fig = px.line(grouped_data, x="date", y="count", title="Books Issued Trend Over Time", labels={"date":"Date", "count":"Number of Books Issued"})
    fig.show()
    print("\nTrend graph generated successfully!")







