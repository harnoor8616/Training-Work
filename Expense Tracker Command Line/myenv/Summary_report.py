import csv

def show_summary():
    total = 0
    category_totals = {}  

    try: 
        with open("Expenses.csv", mode='r') as expenses_data:
            reader = csv.DictReader(expenses_data)
            for row in reader:
                amount = float(row['Amount'])
                category = str(row['Category'])

                total += amount

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

        print(f"\nTotal Expenses: ₹{total:.2f}")
        print("Expenses spent on different categories:")
        for cat, amt in category_totals.items():
            print(f"  {cat}: ₹{amt:.2f}")

    except KeyError as e:
        print(f"Error: Missing column {e} in the CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
