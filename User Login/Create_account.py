from getpass import getpass
import pickle

class Cred:
    def __init__(self):
        self.pass_dict = {}
        
    def Create_data(self):
        with open('emp_data.pickle', 'wb') as file:
            for i in range(2):
                email = input(f"Enter email for user {i+1}: ")
                password = getpass(f"Enter password for user {i+1}: ")
                self.pass_dict[email] = password
            pickle.dump(self.pass_dict, file)
    
    def Cred_check(self):
        with open('emp_data.pickle', 'rb') as file:
            data = pickle.load(file)
        while True:
            search = input("Enter your email: ")
            if search in data:
                password = getpass('Enter your password: ')
                if password == data[search]:
                    print("You're logged in successfully!")
                    break
                else:
                    print('Password is incorrect!')
            else:
                print("Email is incorrect")
            
emp = Cred()
emp.Create_data()
emp.Cred_check()
