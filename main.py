
expenses = []
import calculations
import expense

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Exit")
    print("4. Delete Expenses")
    print("5. View Total Expenses")
    print("6. View Expenses by Category")
    print("7. Sort Expenses by Amount")

    choice = input("Enter your choice: ")


    if choice == "1":
        try:
            amount = float(input("Enter the expense amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
            continue    # <-- skips everything below, goes back to menu

        category = input("Enter the category (e.g. Food, Travel): ")
        description = input("Enter a short description: ")
        val = input("Is this a recurring expense? (yes/no): ").strip().lower()
        
        if val == "yes":
            frequency = input("Enter the frequency (e.g. weekly, monthly): ")
            new_expense = expense.recurringExpense(amount, category, description, frequency)
        else:
            new_expense = expense.expense(amount, category, description)
        expenses.append(new_expense)
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses have been recorded yet.")
        else:
            print("\n===== All Expenses =====")
            for exp in expenses:
                print(exp)
    elif choice == "3":
        print("Goodbye!")
        break
    elif choice == "4":
        try:
            print("\n===== Delete Expenses =====")
            if not expenses:
                print("No expenses to delete.")
            else:
                for i, exp in enumerate(expenses):
                    print(f"{i + 1}. {exp}")
                delete_choice = input("Enter the number of the expense you want to delete (or 'cancel' to go back): ")
                if delete_choice.lower() == 'cancel':
                    continue
                delete_index = int(delete_choice) - 1
                if 0 <= delete_index < len(expenses):
                    deleted_expense = expenses.pop(delete_index)
                    print(f"Deleted expense: {deleted_expense}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")        
            
    
    elif choice == "5":
        total = calculations.get_total(expenses)
        print(f"Total Expenses: {total}")

    elif choice == "6":
            category = input("Enter the category to view expenses for: ")
            filtered_expenses = calculations.filter_by_category(expenses, category)
            if filtered_expenses:
                print(f"\n===== Expenses in Category: {category} =====")
                for exp in filtered_expenses:
                    print(f"Amount: {exp.amount}, Description: {exp.description}")
            else:
                print(f"No expenses found for category: {category}")


    elif choice == "7":
        if not expenses:
         print("No expenses have been recorded yet.")
        else:
            print("\n===== Expenses Sorted by Amount =====")
            sort=input("Enter 'asc' for ascending or 'desc' for descending order: ").strip().lower()
            if sort == 'asc':
                sorted_expenses = sorted(expenses, key=lambda exp: exp.amount)
            elif sort == 'desc':
                sorted_expenses = sorted(expenses, key=lambda exp: exp.amount, reverse=True)
            else:
                print("Invalid sort order. Please enter 'asc' or 'desc'.")
                continue

            print("\n===== Sorted Expenses =====")
            for exp in sorted_expenses:
                print(exp)
        
           
    else:
        print("Invalid choice, try again.")