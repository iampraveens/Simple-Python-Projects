from getpass import getpass
import pickle

class Cred:
    def __init__(self, pass_1, pass_2, pass_3, pass_4):
        self.pass_1 = pass_1
        self.pass_2 = pass_2
        self.pass_3 = pass_3
        self.pass_4 = pass_4
        
    def Create_data(self):
        with open('emp_data.pickle', 'wb') as file:
            
            data = {"admin1@gmail.com": emp.pass_1, 
                    "admin2@gmail.com": emp.pass_2, 
                    "admin3@gmail.com": emp.pass_3, 
                    "admin4@gmail.com": emp.pass_4
                   }
            pickle.dump(data, file)
            
    
    def Cred_check(self):
        with open('emp_data.pickle', 'rb') as file:
            data = pickle.load(file)
        search = input("Enter your email: ")
        for email, password in data.items():
            if email == search:
                if password == getpass("Enter your password: "):
                    print("You're logged in successfully")
                    break
                else:
                    print("Password entered is incorrect")
                    break
        else:
            print("Email is incorrect")

    
    
    
    

emp = Cred("Admin@123", "Admin@456", "Admin@789", "Admin@987")
emp.Create_data()
emp.Cred_check()
