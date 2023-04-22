class Library:
    
    def __init__(self, book_list):
        
        self.book_list = book_list
        
    def display_books(self):
        
        print("=====AVAILABLE BOOKS=====")
        for books in self.book_list:
            print(books)
            
    def lend_book(self, book_name):
        
        if book_name in self.book_list:
            self.book_list.remove(book_name)
            print("Thank you, your request has been fulfilled! \n")
        else:
            print("Book is not available \n")
            
    def return_book(self, lended_book_name, returned_book_name):
        if lended_book_name == returned_book_name:
            if returned_book_name not in self.book_list:
                self.book_list.append(returned_book_name)
                print("Thanks for returning the book! \n")
            else:
                print("Book is already available in the library! \n")
        else:
            print("Book doesn't match, Please check the book! \n")
        
      
class Student:
    
    def request_book(self):
        search = input("Enter the book you want to barrow: \n")
        return search
                   
def main():
    Books = Library(["Python", "SQL", "NoSQL", "Pandas", "NumPy"])
    Student_Praveen = Student()
    
    while True:
        
        print("\nEnter 1 to display the available books")
        print("Enter 2 to request a book")
        print("Enter 3 to return a book")
        print("Enter 4 to exit")
        
        choice = input()
        
        if choice == "1":
            Books.display_books()
            
        elif choice == "2":
            book_name = Student_Praveen.request_book()
            Books.lend_book(book_name)
            
        elif choice == "3":
            lend_book = input("Enter the book you want to return: \n")
            Books.return_book(lend_book, book_name)
        
        elif choice == "4":
            print("Thanks for visiting, See you again! \n")
            break
        
        else:
            print("Invalid input")
            
                        
if __name__ == "__main__":
    main()
    
