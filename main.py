import tkinter as tk
from gui.app import App

# Запуск программы

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()