import Book
import Students
import Library
import Interface as inter
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


times_book = int(input("Enter how many book you want to add book in the library: "))
for i in range(times_book):
    library.add_book(bookInput())


# Create members
times_student = int(input("Enter how many times you want to add students in the library: "))
for i in range(times_student):
    library.add_student(studentInput())


# Issue books
library.issue_book(123, 202204044, 1)
library.issue_book(233, 202204045, 1)


# Return book
library.return_book(123, 202204044,1)

# Display information after returning the book
print("Display Information after returing book")




displayBooks()
displayStudent()