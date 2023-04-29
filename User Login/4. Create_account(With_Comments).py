# Import the getpass module to hide the password input
from getpass import getpass
# Import the pickle module for data serialization and deserialization
import pickle

# Define a class named Cred
class Cred:
    # Define the constructor method that initializes an empty dictionary to store email and password data
    def __init__(self):
        self.pass_dict = {}
        
    # Define a method named Create_data that allows the user to input email and password data and saves it in a pickle file named emp_data.pickle
    def Create_data(self):
        # Open the file in write binary mode using the 'wb' flag
        with open('emp_data.pickle', 'wb') as file:
            # Use a for loop to iterate over the range of 2 employees to input email and password data for each employee
            for i in range(2):
                # Ask the user to input the email address for the current employee using the input() function and store it in the email variable
                email = input(f"Enter email for user {i+1}: ")
                # Ask the user to input the password for the current employee using the getpass() function and store it in the password variable
                password = getpass(f"Enter password for user {i+1}: ")
                # Add the email and password data to the pass_dict dictionary
                self.pass_dict[email] = password
            # Use the pickle.dump() function to save the pass_dict dictionary to the emp_data.pickle file
            pickle.dump(self.pass_dict, file)
    
    # Define a method named Cred_check that allows the user to check if their email and password combination is valid
    def Cred_check(self):
        # Open the emp_data.pickle file in read binary mode using the 'rb' flag and load the data into the data variable using the pickle.load() function
        with open('emp_data.pickle', 'rb') as file:
            data = pickle.load(file)
        # Use a while loop with a True condition to allow the user to repeatedly enter their email and password until they get it right
        while True:
            # Ask the user to enter their email using the input() function and store it in the search variable
            search = input("Enter your email: ")
            # Check if the email entered by the user is in the data dictionary
            if search in data:
                # If the email is in the dictionary, ask the user to enter their password using the getpass() function and store it in the password variable
                password = getpass('Enter your password: ')
                # Check if the password entered by the user matches the password in the dictionary for the email entered by the user
                if password == data[search]:
                    # If the password matches, print a success message and break out of the while loop using the break statement
                    print("You're logged in successfully!")
                    break
                else:
                    # If the password doesn't match, print an error message and continue with the while loop using the continue statement
                    print('Password is incorrect!')
            else:
                # If the email entered by the user is not in the dictionary, print an error message and continue with the while loop using the continue statement
                print("Email is incorrect")
            
# Create an instance of the Cred class
emp = Cred()
# Call the Create_data() method to allow the user to input email and password data and save it to the emp_data.pickle file
emp.Create_data()
# Call the Cred_check() method to allow the user to check if their email and password combination is valid
emp.Cred_check()
