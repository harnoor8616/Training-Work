from Adding_Expense import add_new_expense

def welcome():
    print(f""" 
         ____       __  __                          
        |  _ \ _   _\ \/ /_ __   ___ _ __  ___  ___ 
        | |_) | | | |\  /| '_ \ / _ \ '_ \/ __|/ _ \\
        |  __/| |_| |/  \| |_) |  __/ | | \__ \  __/
        |_|    \__, /_/\_\ .__/ \___|_| |_|___/\___|
               |___/     |_|                        

WELCOME TO PyXpense - Because Every Rupee Counts !!!
Ready to Track Your Finances
    """)
    name = input("Please enter your name:   ").strip().title()
    print(f"\nHello {name}! Let's get started with managing your expenses.\n")

welcome()
is_stop = False
while not is_stop:
    print("""
    Type 'N' to Add New Expenses
    Type 'V' to View an Existing Expense
    Type 'A' to View All Expenses
    Type 'S' to Get a Summary Report
    Type 'X' to Exit
    """)   
    try:
        choice = input("Please Enter Your Choice: ").upper()
        if choice not in ["N", "V", "A", "S", "X"]:
            raise ValueError("Invalid Value! Please choose a valid option.")
        
        if choice == "N":
            print("Adding a new Expense:\n\n\n")
            add_new_expense()
            pass
        elif choice == "V":
            print("Viewing an Existing Expense:\n\n\n")
            # view_expense()
            pass
        elif choice == "A":
            print("Displaying All Expenses:\n\n\n")
            # view_all_expenses()
            pass
        elif choice == "S":
            print("Generating Summary Report:\n\n\n")
            # show_summary()
            pass
        elif choice == "X":
            print("Exiting the application. Goodbye!")
            is_stop = True

    except ValueError as e:
        print(e)