import json
from datetime import datetime
from pathlib import Path

FILE = Path("expenses.json")


def load_expenses():
    if FILE.exists():
        try:
            with FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read expenses.json. Starting with an empty list.")
    return []


def save_expenses(expenses):
    with FILE.open("w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)


def add_expense(expenses):
    try:
        amount = float(input("Enter amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        category = input("Category: ").strip()
        note = input("Description: ").strip()

        if not category:
            print("Category cannot be empty!")
            return

        expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d"),
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- ALL EXPENSES ---")
    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']:.2f} | "
            f"{expense['category']} | {expense['note']} | {expense['date']}"
        )


def show_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(float(e["amount"]) for e in expenses)
    highest = max(expenses, key=lambda e: float(e["amount"]))

    print("\n--- EXPENSE SUMMARY ---")
    print(f"Total expenses: ₹{total:.2f}")
    print(f"Number of transactions: {len(expenses)}")
    print(f"Highest expense: ₹{float(highest['amount']):.2f}")
    print(f"Category: {highest['category']}")

    print("\nSpending by category:")
    categories = {}
    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + float(expense["amount"])

    for category, amount in sorted(categories.items()):
        print(f"{category}: ₹{amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== SMART EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Thank you for using Smart Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
