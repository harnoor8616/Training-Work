import pwinput
import string
import user

class Welcome_to_Inventory_System():
    def __init__(self):
        self.name=""
        self.is_file_based=False
    def welcome_art(self):
        print("""
     ___                 _____               _    
    |_ _|_ ____   ___   |_   _| __ __ _  ___| | __
     | || '_ \ \ / / | | || || '__/ _` |/ __| |/ /
     | || | | \ V /| |_| || || | | (_| | (__|   < 
    |___|_| |_|\_/  \__, ||_||_|  \__,_|\___|_|\_\ 
                    |___/                         
""")
    def description_text(self):
        print("""Welcome to InvyTrack — Your Smart Inventory Partner.\n
This Inventory Management System, built using Python, is a robust and scalable solution designed to help businesses effectively monitor, manage, and optimize their stock. It is Perfect for small businesses, warehouses, and retail environments.\n"""
        )
    def intro(self):
        while True:
            try:
                self.name=input("Welcome User!!! May i know your Name!?   ").title()

                if not self.name:
                    raise ValueError("Name Field can not be empty. Please Enter Your Name")
                if (self.name.isalpha()==False):
                    raise ValueError("Invalid Input!!! Please enter a valid input.")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                print(f"\nHello {self.name}!!! Ready to manage your inventory like a pro?\n")
                break
    def system_preference(self):
        while True:
            try:
                print("\nDo you want your system storage to be:\n")
                print("1. File-Based i.e using .csv file")
                print("2. Database-Based i.e using MYSQL database [Recommended]\n")
                choice = input("Enter 1 or 2: \n").strip()

                if not choice:
                    raise ValueError("Input cannot be empty. Please enter 1 or 2.")

                if choice not in ['1', '2']:
                    raise ValueError("Invalid input. Please enter 1 or 2 only.")

                if choice == '1':
                    print("\nYou chose File-Based storage.\n")
                    self.is_file_based=True
                else:
                    print("\nYou chose Database based storage.\n")
                    self.is_file_based=False
                break  
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")

class Signup(Welcome_to_Inventory_System):
    def __init__(self):
        super().__init__()
        self.username=""
        self.password=""
        self.length=0

    def get_signup_details(self):
        print(f"""📝 SIGN UP FOR YOUR INVYTRACK ACCOUNT
Please enter your credentials:\n""")
        while True:
            try:
                self.username = input("Please enter your username: ").strip()
                self.length=len(self.username)
                if not self.username:
                    raise ValueError("Username cannot be empty.")
                if self.length < 4:
                    raise ValueError("Username must be at least 4 characters long.")
                if not self.username.isalnum():
                    raise ValueError("Username can only contain letters and numbers (no special characters or spaces).")
            except ValueError as e:
                print(f"Error: {e}\n")
            else:
                break
        while True:
            try:
                self.password = pwinput.pwinput("Please enter your password: ", mask="*")
                print(self.password)
                if len(self.password) < 8:
                    raise ValueError("Password must be at least 8 characters long.")

                if not any(char.isupper() for char in self.password):
                    raise ValueError("Password must contain at least one uppercase letter.")

                if not any(char.islower() for char in self.password):
                    raise ValueError("Password must contain at least one lowercase letter.")

                if not any(char in string.punctuation for char in self.password):
                    raise ValueError("Password must contain at least one special character (!@#$ etc.).")
            except ValueError as e:
                print(f"Error: {e}\n")
            else:
                break
    
obj1=Welcome_to_Inventory_System()
obj1.welcome_art()
obj1.description_text()
obj1.intro()
obj1.system_preference()
obj2=Signup()
obj2.get_signup_details()
obj3=user.Manage_user(obj2.username,obj2.password,obj1.is_file_based)
if obj1.is_file_based:
    obj3.save_to_csv()
else:
    obj3.save_to_database()