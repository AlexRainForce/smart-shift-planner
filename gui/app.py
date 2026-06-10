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

    
    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if path:
            data = self.loader.load(path)
            print(data)

    def export_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".xlsx")
        if path:
            schedule = self.scheduler.get_schedule(self.employees)
            self.exporter.export(schedule, path)

    def undo(self):
        self.scheduler.undo_last()

    def init_gui(self):
    # верхняя панель
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.btn_load = tk.Button(self.top_frame, text="Загрузить файл", command=self.load_file)
        self.btn_load.pack(side=tk.LEFT)

        self.btn_export = tk.Button(self.top_frame, text="Экспорт", command=self.export_file)
        self.btn_export.pack(side=tk.LEFT, padx=5)

        self.btn_undo = tk.Button(self.top_frame, text="Отменить", command=self.undo)
        self.btn_undo.pack(side=tk.LEFT)

        # список сотрудников
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.listbox = tk.Listbox(self.list_frame, width=40)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def run(self):
        self.root.mainloop()