import csv
def view_all_expenses():
    try:
        with open('Expenses.csv',mode='r') as Expenses_data:
            Reader=csv.DictReader(Expenses_data)
            print(f"{'S.No.':<15} {'Amount (₹)':<15} {'Category':<15} {'Date':<15} {'Note':<15}")
            print("*" * 80)
            for idx, row in enumerate(Reader, start=1):
                    print(f"{idx:<15}  {row['Amount']:<15} {row['Category']:<15}  {row['Date']:<15} {row['Note']:<15}")
    except FileNotFoundError:
        print("The file 'Expenses.csv' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
