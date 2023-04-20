# Importing the getpass module to hide the password while it is being entered by the user
from getpass import getpass
# Importing the pickle module for serialization and deserialization of Python objects
import pickle

# Defining a class Cred
class Cred:
    
    # Defining the constructor method and initializing four instance variables
    def __init__(self, pass_1, pass_2, pass_3, pass_4):
        self.pass_1 = pass_1
        self.pass_2 = pass_2
        self.pass_3 = pass_3
        self.pass_4 = pass_4
    
    # Defining a method to create a dictionary and serialize it using pickle
    def Create_data(self):
        # Opening the 'emp_data.pickle' file in write bytes mode
        with open('emp_data.pickle', 'wb') as file:
            
            # Creating a dictionary with four key-value pairs of email-password
            data = {"admin1@gmail.com": emp.pass_1, 
                    "admin2@gmail.com": emp.pass_2, 
                    "admin3@gmail.com": emp.pass_3, 
                    "admin4@gmail.com": emp.pass_4
                   }
            
            # Serializing the dictionary object and writing it to the file
            pickle.dump(data, file)
            
    
    # Defining a method to read the serialized dictionary and check for email-password authentication
    def Cred_check(self):
        # Opening the 'emp_data.pickle' file in read bytes mode
        with open('emp_data.pickle', 'rb') as file:
            # Deserializing the dictionary object from the file
            data = pickle.load(file)
        # Asking the user to enter their email
        search = input("Enter your email: ")
        # Looping through the dictionary items to check for the entered email
        for email, password in data.items():
            # If the entered email matches with an email in the dictionary, ask for password authentication
            if email == search:
                # Hiding the password while the user enters it
                if password == getpass("Enter your password: "):
                    # If the entered password matches with the password in the dictionary, print a success message
                    print("You're logged in successfully")
                    break
                else:
                    # If the entered password doesn't match with the password in the dictionary, print an error message
                    print("Password entered is incorrect")
                    break
        else:
            # If the entered email doesn't match with any email in the dictionary, print an error message
            print("Email is incorrect")

# Creating an instance of the Cred class with four passwords as arguments
emp = Cred("Admin@123", "Admin@456", "Admin@789", "Admin@987")
# Calling the Create_data method on the emp object to serialize the dictionary
emp.Create_data()
# Calling the Cred_check method on the emp object to authenticate the user's email and password
emp.Cred_check()
