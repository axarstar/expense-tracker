# Expense Tracker (CLI)

A command-line Python application to track personal expenses — built as a final project after completing a 15-day Python fundamentals course. It supports adding, viewing, deleting, sorting, and analyzing expenses, plus saving/loading data to a CSV file.

## Features

1. **Add Expense** — log a one-time or recurring expense (recurring expenses store a frequency, e.g. Monthly, Weekly)
2. **View All Expenses** — display every recorded expense
3. **Exit** — close the program
4. **Delete Expense** — remove an expense by its number, with safe handling of invalid input
5. **View Total Expenses** — sum of all recorded amounts
6. **View Expenses by Category** — filter expenses (e.g. show only "Food")
7. **Sort Expenses by Amount** — ascending or descending order
8. **View Statistics** — average, maximum, and minimum expense (calculated with NumPy)
9. **Save Expenses to CSV** — export all expenses to `expenses.csv` using Pandas
10. **Load Expenses from CSV** — reload previously saved expenses back into the program

## Concepts Demonstrated

- f-strings & `.format()` method
- Core data types, string indexing & methods
- Lists, tuples, dictionaries, sets
- Operator precedence, control structures & loops
- Exception handling (`try`/`except`) for input validation and file errors
- Custom Python modules (`calculations.py`, `expense.py`) and imports
- `lambda`, `map()`, `filter()`
- Sorting with a custom `key` function
- Object-Oriented Programming: classes, `__init__`, `self`, inheritance (`Expense` → `RecurringExpense`), `super()`, `__str__`, polymorphism
- NumPy — statistical calculations (`np.mean`, `np.max`, `np.min`)
- Pandas — DataFrames, CSV read/write (`to_csv`, `read_csv`)

## Project Structure

```
expense-tracker/
├── main.py            # Menu loop and user interaction
├── expense.py          # Expense and RecurringExpense classes
├── calculations.py      # Totals, filtering, sorting, and statistics logic
├── expenses.csv         # Saved expense data (created after using "Save to CSV")
└── README.md
```

## How to Run

```bash
python main.py
```

Requires `numpy` and `pandas` installed in your Python environment.

## Status

✅ Complete — all planned features implemented and tested.