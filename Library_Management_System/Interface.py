
def bookInput():
    print("Book Input")
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter Number of Copies: "))
    return book_id, title, author, copies


def displayBooks(library):
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
