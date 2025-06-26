import csv

def fetch_expenses(category=None, date=None):
    with open('Expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        results = []

        for row in reader:
            if (category is None or row['Category'] == category) and \
               (date is None or row['Date'] == date):
                results.append(row)

    return results

def view_expense():
    is_stop = False
    while not is_stop:
        print("""
        How do you want to fetch expense records?
        Press 'C' to fetch records by Category
        Press 'D' to fetch records by Date
        Press 'X' to Exit.
        """)
        try:
            choice = input("Please enter your choice:   ").upper()
            
            if choice == 'C':
                print("Fetching Records By Category:\n")
                input_category = input("Enter the category:   ")
                results = fetch_expenses(category=input_category)
                if results:
                    for record in results:
                        print(record)
                else:
                    print("No records found for this category.")

            elif choice == 'D':
                print("Fetching Records By Date:\n")
                input_date = input("Enter the date (YYYY-MM-DD):   ")
                results = fetch_expenses(date=input_date)
                if results:
                    for record in results:
                        print(record)
                else:
                    print("No records found for this date.")

            elif choice == 'X':
                print("Exiting...")
                is_stop = True

            else:
                raise ValueError("Invalid Input! Please enter 'C', 'D', or 'X'.")

        except ValueError as e:
            print(e)
