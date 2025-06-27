from datetime import date
import csv

def add_new_expense():
    try:
        print(f"Please enter the details:\n")
        amount_input = input("Enter the Amount (in rupees):  ").strip()
        if not amount_input:
            raise ValueError("Amount cannot be empty.")
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        category = input("Enter the category of the Expense:   ").strip().title()
        if not category:
            raise ValueError("Category cannot be empty.")
        entered_date = input("Enter the Date of Expense (YYYY-MM-DD) [Leave empty for today]:  ").strip()
        if entered_date == "":
            Date = date.today()
        else:
            Date = date.fromisoformat(entered_date)  
        note = input("Enter Additional Text:  ").strip()
        with open(f'Expenses.csv',mode='a') as expense_data:
            writer=csv.writer(expense_data)
            expense_data.seek(0)
            if(expense_data.tell()==0):
                 writer.writerow(["Amount", "Category", "Date", "Note"])
            writer.writerow([amount,category,Date,note])
        print("\n✅ Expense Recorded Successfully:")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
