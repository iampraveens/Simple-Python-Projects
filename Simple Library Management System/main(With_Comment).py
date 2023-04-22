# Define a class Library
class Library:
    
    # Define the constructor of the class with book_list as input parameter
    def __init__(self, book_list):
        
        # Assign the input parameter to an instance variable called book_list
        self.book_list = book_list
    
    # Define a method to display the available books
    def display_books(self):
        
        # Print a header for the available books section
        print("=====AVAILABLE BOOKS=====")
        
        # Iterate through the book_list instance variable and print each book
        for books in self.book_list:
            print(books)
    
    # Define a method to lend a book
    def lend_book(self, book_name):
        
        # Check if the requested book is available in the library's book_list instance variable
        if book_name in self.book_list:
            
            # If the book is available, remove it from the book_list
            self.book_list.remove(book_name)
            
            # Print a message to confirm that the book has been lent
            print("Thank you, your request has been fulfilled! \n")
        
        # If the requested book is not available, print a message to inform the user
        else:
            print("Book is not available \n")
    
    # Define a method to return a book
    def return_book(self, lended_book_name, returned_book_name):
        
        # Check if the lended_book_name matches the returned_book_name
        if lended_book_name == returned_book_name:
            
            # Check if the returned book is already available in the library's book_list instance variable
            if returned_book_name not in self.book_list:
                
                # If the returned book is not already available, add it to the book_list
                self.book_list.append(returned_book_name)
                
                # Print a message to confirm that the book has been returned
                print("Thanks for returning the book! \n")
            
            # If the returned book is already available, print a message to inform the user
            else:
                print("Book is already available in the library! \n")
        
        # If the lended_book_name does not match the returned_book_name, print a message to inform the user
        else:
            print("Book doesn't match, Please check the book! \n")
        
# Define a class Student
class Student:
    
    # Define a method to request a book
    def request_book(self):
        
        # Prompt the user to enter the name of the book they want to borrow
        search = input("Enter the book you want to borrow: \n")
        
        # Return the name of the book that the user wants to borrow
        return search

# Define a main function
def main():
    # Creates an instance of the Library class with a list of books.
    Books = Library(["Python", "SQL", "NoSQL", "Pandas", "NumPy"])
    
    # Creates an instance of the Student class.
    Student_Praveen = Student()
    
    # The main loop of the program.
    while True:
        
        # Displays a menu of options for the user.
        print("\nEnter 1 to display the available books")
        print("Enter 2 to request a book")
        print("Enter 3 to return a book")
        print("Enter 4 to exit")
        
        # Gets the user's choice from the input.
        choice = input()
        
        # Executes the user's choice.
        if choice == "1":
            # Calls the display_books method of the Library instance.
            Books.display_books()
            
        elif choice == "2":
            # Gets the name of the book to borrow from the user using the request_book method of the Student instance.
            book_name = Student_Praveen.request_book()
            # Calls the lend_book method of the Library instance with the requested book name.
            Books.lend_book(book_name)
            
        elif choice == "3":
            # Gets the name of the book to return from the user using input.
            lend_book = input("Enter the book you want to return: \n")
            # Calls the return_book method of the Library instance with the borrowed book name and the returned book name.
            Books.return_book(lend_book, book_name)
        
        elif choice == "4":
            # Exits the program.
            print("Thanks for visiting, See you again! \n")
            break
        
        else:
            # Displays an error message if the user enters an invalid choice.
            print("Invalid input")
            
# Calls the main function if this file is run as the main program.
if __name__ == "__main__":
    main()
    
