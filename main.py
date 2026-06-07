from models.employee import Employee
from models.shift import Shift
from core.scheduler import Scheduler
from core.exporter import ExcelExporter

# создаём сотрудников
emp1 = Employee("Иванов", "продавец") 
emp2 = Employee("Петров", "кассир")

# создаём смены
shift1 = Shift("2026-06-10", "09:00", "18:00")
shift2 = Shift("2026-06-10", "12:00", "21:00")
shift3 = Shift("2026-06-11", "09:00", "18:00")

# планировщик
scheduler = Scheduler()
#передаем сотрудников и смены методу assign объекту класса scheduler
scheduler.assign(emp1, shift1) 
scheduler.assign(emp2, shift2)
scheduler.assign(emp1, shift3)

# получаем расписание
schedule = scheduler.get_schedule([emp1, emp2])
print(schedule)

# экспорт
exporter = ExcelExporter()
exporter.export(schedule, "schedule.xlsx")
print("сохранено")