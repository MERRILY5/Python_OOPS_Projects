import Book
import Students
import Library
import time
library = Library.library()

print("_____________________Library Management System_____________________")


def bookInput():
    print("---------------------------Book Input---------------------------")
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter Number of Copies: "))
    book = Book.book(book_id, title, author, copies)
    return book

def studentInput():
    print("---------------------------Student Input---------------------------")
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    student = Students.student(student_id, name)
    return student

def displayBooks():
    print("-"*30)
    count = 1
    for d in library.books:
        print(f"S.no: {count} |  Book id: {d} | Book Copies: {library.books[d]}")
        count += 1
        print("-"*30)

def displayStudent():
    print("-"*30)
    count = 1
    for d in library.students:
        print(f"S.no: {count} | Student id: {d} | Student Name: {library.students[d]}")
        count += 1
        print("-"*30)


def issuing():
    student_id = int(input("Enter Student ID: "))
    book_id = int(input("Enter Book ID: "))
    copies = int(input("Enter Number of Copies: "))
    library.issue_book(book_id, student_id, copies)

def returning():
    student_id = int(input("Enter Student ID: "))
    book_id = int(input("Enter Book ID: "))
    copies = int(input("Enter Number of Copies: "))
    library.return_book(book_id, student_id, copies)


X=True
while X:
    try:
        choice = int(input("Press 1 to add books\nPress 2 to add students\nPress 3 To issue books\nPress 4 for return book\nPress 5 to display infromation of Library\nPress 6 to exit\nEnter your choice: "))
        if choice == 1:
            times_book = int(input("Enter how many book you want to add book in the library: "))
            for i in range(times_book):
                library.add_book(bookInput())
            print("----------------------Books added successfully----------------------")

        elif choice == 2:
            times_student = int(input("Enter how many times you want to add students in the library: "))
            for i in range(times_student):
                library.add_student(studentInput())
            print("----------------------Students added successfully----------------------")
        elif choice == 3:
            print("---------------------------Issue Book---------------------------")
            issuing()
        elif choice == 4:
            print("---------------------------Return Book---------------------------")
            returning()
        elif choice == 5:
            displayBooks()
            displayStudent()
        elif choice == 6:
            exit()
        else:
            print("Invalid Choice! Try again")
            continue
    except ValueError as e:
        print("----------------------------------------------------------------")
        print("Invalid input! Please enter a number.")
        print("----------------------------------------------------------------")
        time.sleep(1)
