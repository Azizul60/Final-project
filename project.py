import os
import json
from datetime import datetime
#Library Management System

def main():
    

    filename='Book selves.json'
    data= load_file(filename)
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Save library data")
        print("3. Search for a book")
        print("4. Issue a book")
        print("5. Return a book")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        try:
            if choice == '1':
                Add_books(data)
            elif choice == '2':
                save_file(filename, data)
            elif choice == '3':
                search_books(data)
            elif choice == '4':
                issue_book(data)
            elif choice == '5':
                return_book(data)
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except Exception as e:
            print(f"An error occurred: {e}")







def load_file(filename):
    if os.path.exists(filename):
        with open (filename , 'r') as file:
            return json.load(file)
    return {"Books":[]}
def save_file(filename ,data):

    with open (filename ,'w') as file:
        return json.dump(data, file , indent=4)

def Add_books(data):
    Titel=input("Write the titel of the book :")
    Author= input("Name of the author : ")
    Genra= input("What is the genra : ")

    data['Books'].append({
        "titel":Titel,
        "author":Author,
        "genra":Genra
    }
        
    )

def search_books(data):
    results=[]
    search=input("search books by(titel,author,genra) : ").lower()
    query=input(f"Enter the {search} of the book :").lower()
    for book in data['Books']:
        if search=='titel' and query in book['titel'].lower():
            results.append(book)
        elif search == 'author' and query in book['author'].lower():
            results.append(book)
        elif search == 'genra' and query in book['genra'].lower():
            results.append(book)

    if results:
        print(f"\nBooks matching your search for {search} '{query}':")
        for book in results:
            print(f"Title: {book['titel']}, Author: {book['author']}, Genre: {book['genra']}")
    else:
        print(f"\nNo books found for {search} '{query}'.")


#this function issue book to students
def issue_book(data):
    student_name = input("Enter student's name: ")
    student_id = input("Enter student ID: ")
    student_department = input("Enter student's department: ")
    book_title = input("Enter the title of the book to be issued: ").lower()

    issued_book=None # initialy no book is issued

    for book in data['Books']:
        if book_title==book['titel'].lower():
            issued_book=book
            break
    if issued_book:
        # Record the issue details with the current date and time
        issue_details = {
            "name": student_name,
            "id": student_id,
            "department": student_department,
            "book_title": issued_book['titel'],
            "issued_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Add the issue details to the 'IssuedBooks' list in the JSON data
        if 'IssuedBooks' not in data:
            data['IssuedBooks'] = []
        data['IssuedBooks'].append(issue_details)

        # Remove the issued book from the available books
        data['Books'].remove(issued_book)

        print(f"Book '{issued_book['titel']}' has been issued to {student_name}.")
    else:
        print(f"The book '{book_title}' is not available in the library.")

def return_book(data):
    student_name = input("Enter student's name: ")
    student_id = input("Enter student ID: ")
    book_title = input("Enter the title of the book to return: ").lower()

    returned_book = None

    # Search for the issued book in the 'IssuedBooks' list
    for issued in data.get('IssuedBooks', []):
        if (issued['name'].lower() == student_name.lower() and
            issued['id'] == student_id and
            issued['book_title'].lower() == book_title):
            returned_book = issued
            break

    if returned_book:
        # Add the returned book back to the 'Books' list
        book_to_return = {
            "titel": returned_book['book_title'],
            "author": "Unknown",  # Modify this if you have more details stored
            "genra": "Unknown"    # Modify this if you have more details stored
        }
        data['Books'].append(book_to_return)

        # Remove the book from the 'IssuedBooks' list
        data['IssuedBooks'].remove(returned_book)

        print(f"Book '{returned_book['book_title']}' has been returned by {student_name}.")
    else:
        print(f"No record found for '{book_title}' issued to {student_name}.")
    


    


if __name__=='__main__':
    main()



