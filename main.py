from books import add_book, edit_book, search_book
from students import add_student
from transactions import issue_book, return_book, generate_trend_graph

#Main Python System

def display_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add/Edit/Search/View Books")
    print("2. Add Student")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Generate Trend Graph")
    print("6. Exit")


def main():
    userchoice = 0
    while True:
        display_menu()
        userchoice = input("\nPlease select what you want to do: ")

        if userchoice == "1":
            while True:
                print("\n---Book Details menu---")
                print("1. Add Book details")
                print("2. Edit Book details")
                print("3. Search Book details")
                print("4. View all Books")
                print("5. Go back to main menu")
                subchoice = input("Please select what you want to do next: ")
                if subchoice == "1":
                    add_book()

                elif subchoice == "2":
                    edit_book()

                elif subchoice == "3":
                    search_book()

                elif subchoice == "4":
                    import os
                    import csv

                    # Read book.csv
                    if not os.path.exists("book.csv"):
                        print("File empty")

                    elif os.stat("book.csv").st_size == 0:
                        print("File empty")

                    else:
                        with open("book.csv", mode='r', newline='') as file:
                            reader = csv.reader(file)
                            rows = list(reader)

                            if len(rows) == 0:
                                print("File empty")
                            else:
                                print("\n===== BOOK LIST =====")
                                print(f"Book ID | ISBN | Title | No of Copies | Available amount | Price")
                                print("------------------------------------------------------")

                                for row in rows:
                                    print(" | ".join(row))
                elif subchoice == "5":
                    break
                else:
                    print("Invalid choice")

        elif userchoice == "2":
            add_student()
        elif userchoice == "3":
            issue_book()
        elif userchoice == "4":
            return_book()
        elif userchoice == "5":
            generate_trend_graph()
        elif userchoice == "6":
            print("Exiting Program...")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()










