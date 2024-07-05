from Book import book
from Students import student

class library:
    def __init__(self):
        self.books = {}
        self.students = {}
        self.issue_requests = []
        self.book_list= []

    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id] += book.copies
        else:
            self.books[book.book_id] = book.copies

    def add_student(self, student):
        if student not in self.students:
            self.students[student.student_id] = student.name

    def issue_book(self, book_id, student_id,copies):
        if book_id in self.books and self.books[book_id] > 0:

            if student_id in self.students:
                student.books_borrowed(self,book_id,student_id,copies)
            else:
                print(f"Student ID: {student_id} not found.")
        else:
            print(f"Book ID: {book_id} not available or out of stock.")
    

    def return_book(self, book_id, student_id,copies):
        keys = []
        if student_id in self.students:
            for d in self.book_list:
                for inner_dict in d.values():
                    keys.extend(inner_dict.keys())
            if book_id in keys:
                student.books_returned(self,book_id,student_id,copies)
            else:
                print(f"Book ID {book_id} not borrowed by Student ID {student_id}.")
        else:
            print(f"Student ID {student_id} not found.")