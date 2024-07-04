class student:
    def __init__(self,student_id,name):
        self.student_id = student_id
        self.name = name
    
    def books_borrowed(self,book_id,student_id,copies):
        self.book_list.append({student_id:{book_id:copies}})
        self.books[book_id]-= copies
    
    def books_returned(self,book_id,student_id,copies):
        self.book_list.remove({student_id:{book_id:copies}})
        self.books[book_id] += copies

    def __str__(self):
        return f"Student[Student ID: {self.student_id}\nName: {self.name}\nBook Borrowed: {len(self.book_list)}]"