import json
import os
def calculate_total(expenses):
    total = 0
    for category, amount in expenses.items():
        total += amount
    return total
balance = 500
def calculate_remaining(balance, total):
    return balance - total
def get_expenses(expenses):
    
    while True:
        category = input("Category (or 'done' to finish): ")

        if category.lower() == "done":
            break
        while True:
            try:
                amount = float(input("Amount: $"))
            except ValueError:
                print("Please enter a valid number")
                continue
            if amount < 0:
                print("Please enter a non-negative number")
                continue
            break
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

    return expenses
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            print("Saved expenses loaded from file.")
    else:   
        expenses = {}
    return expenses
expenses = load_expenses()
while True:
    print("\n--- Finance Tracker ---")
    print("1. Add expenses")
    print("2. View expenses and totals")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        expenses = get_expenses(expenses)
        
    elif choice == "2":
       if not expenses:
            print("No expenses recorded yet")
       else:
            for category, amount in expenses.items():
                print(f"{category}: ${amount:.2f}")
            total = calculate_total(expenses)
            remaining = calculate_remaining(balance, total)
            print(f"Total spent: ${total:.2f}")
            print(f"Remaining balance: ${remaining:.2f}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)



