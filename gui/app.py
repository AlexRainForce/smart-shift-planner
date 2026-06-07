import tkinter as tk
from tkinter import filedialog, scrolledtext
from core.file_loader import ExcelLoader
from core.scheduler import Scheduler
from core.exporter import ExcelExporter
from models.employee import Employee
from models.shift import Shift

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Shift Planner")
        self.root.geometry("800x600")
        self.scheduler = Scheduler()
        self.loader = ExcelLoader()
        self.exporter = ExcelExporter()
        self.employees = []
        self.init_gui()

    def init_gui(self):
        pass

    def run(self):
        self.root.mainloop()