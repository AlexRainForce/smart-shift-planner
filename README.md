# smart-shift-planner
![Smart Shift Planner](assets/banner.png)
Python desktop app for employee shift planning. Uses Command, Strategy and State design patterns. Built with openpyxl.
# Smart Shift Planner

Desktop app for employee shift planning built with Python.

## Features
- Load historical data from Excel
- Add employees and shifts manually
- Confirm shifts with color indicators (gray / green / red)
- Search employees by name
- Undo last action
- Export schedule to Excel
- Status bar showing total employees and shifts

## Architecture
- **Command** pattern — every action can be undone
- **Strategy** pattern — flexible file loading and export
- **State** pattern — shift states: planned, confirmed, cancelled

## Stack
- Python 3.14
- openpyxl
- tkinter (coming soon)

## Run
```
python main.py
```
