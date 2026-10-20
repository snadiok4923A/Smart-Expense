# Smart Expense Tracker 🐍

A lightweight command-line Python application for recording daily expenses and reviewing spending habits.

## Features

- Add daily expenses with category and description
- View all recorded transactions
- Calculate total spending and transaction count
- Identify the highest expense
- Summarize spending by category
- Persist data locally in JSON

## Requirements

- Python 3.9 or newer
- No third-party packages required

## Run the project

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python expense_tracker.py
   ```

   On some systems, use `python3 expense_tracker.py`.

The application creates `expenses.json` automatically when you add your first expense.

## Project structure

```text
Smart-Expense-Tracker/
├── expense_tracker.py
├── README.md
├── .gitignore
└── expenses.json   # created automatically; not included by default
```

## Future improvements

- Monthly spending reports
- Export transactions to CSV
- Charts with Matplotlib
- Budget limits and alerts
- Desktop or web interface

## License

This project is available under the MIT License. See `LICENSE`.
