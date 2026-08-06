# Expense Tracker (CLI)

A simple command-line Python application to track personal expenses — built as a final project after completing a 15-day Python fundamentals course.

## Features
- Add one-time or recurring expenses
- View all recorded expenses
- Delete an expense
- View total spending
- Filter expenses by category

## Concepts Demonstrated
- f-strings & `.format()` method
- Core data types, string indexing & methods
- Lists, tuples, dictionaries, sets
- Control structures & loops
- Exception handling (`try`/`except`) for input validation
- Custom Python modules (`calculations.py`, `expense.py`) and imports
- `lambda`, `map()`, `filter()`
- Object-Oriented Programming: classes, inheritance (`Expense` → `RecurringExpense`), `super()`, `__str__`

## Project Structure

expense-tracker/
├── main.py # Menu loop and user interaction
├── expense.py # Expense and RecurringExpense classes
├── calculations.py # Totals, filtering, and calculation logic
└── README.md


## How to Run
```bash
python main.py
```

## Status
🚧 In progress — NumPy and Pandas integration (statistics + CSV save/load) coming next.