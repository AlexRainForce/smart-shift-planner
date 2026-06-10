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
    #добавить смены
    def add_shift(self):
        name = self.entry_name.get()
        position = self.entry_position.get()
        date = self.entry_date.get()
        start = self.entry_start.get()
        end = self.entry_end.get()
        
        if not name or not date or not start or not end:
            return
        
        emp = Employee(name, position)
        shift = Shift(date, start, end)
        self.scheduler.assign(emp, shift)
        self.employees.append(emp)
        
        self.listbox.insert(tk.END, f"{name} | {date} | {start}-{end}")
    #метод загрузки файла
    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if path:
            data = self.loader.load(path)
            self.listbox.delete(0, tk.END)
            for row in data:
                self.listbox.insert(tk.END, str(row))
    #метод сохранения файла
    def export_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".xlsx")
        if path:
            schedule = self.scheduler.get_schedule(self.employees)
            self.exporter.export(schedule, path)
    #метод отмены
    def undo(self):
        self.scheduler.undo_last()


    #метод инициализации интерфейса

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

        self.right_frame = tk.Frame(self.list_frame)
        self.right_frame.pack(side=tk.LEFT, padx=10, fill=tk.Y)

        tk.Label(self.right_frame, text="Имя сотрудника").pack()
        self.entry_name = tk.Entry(self.right_frame, width=20)
        self.entry_name.pack()

        tk.Label(self.right_frame, text="Должность").pack()
        self.entry_position = tk.Entry(self.right_frame, width=20)
        self.entry_position.pack()

        tk.Label(self.right_frame, text="Дата смены").pack()
        self.entry_date = tk.Entry(self.right_frame, width=20)
        self.entry_date.pack()

        tk.Label(self.right_frame, text="Начало").pack()
        self.entry_start = tk.Entry(self.right_frame, width=20)
        self.entry_start.pack()

        tk.Label(self.right_frame, text="Конец").pack()
        self.entry_end = tk.Entry(self.right_frame, width=20)
        self.entry_end.pack()

        self.btn_add = tk.Button(self.right_frame, text="Добавить смену", command=self.add_shift)
        self.btn_add.pack(pady=5)


    def run(self):
        self.root.mainloop()