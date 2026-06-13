from core.command import AssignShiftCommand
from core.iterators import ActiveEmployeeIterator
# Планировщик смен. Паттерн Command - каждое назначение можно откатить через undo_last
class Scheduler:
    def __init__(self):
        self.history = [] # история смен
                     
    
    def assign(self, employee, shift):
        cmd = AssignShiftCommand(employee, shift)  # создание объекта класса который принмает два объекта = СОТРУДНИК и СМЕНА
        cmd.execute()  # добавить смену
        self.history.append(cmd)  # добавить смену в историю
    
    def undo_last(self):                
        if self.history:  # если history пустой ничего не делает
            cmd = self.history.pop()  # берёт последний cmd из массива и удаляет его оттуда
            cmd.undo()  # вызывает метод undo того объекта, он сам знает как откатить, убирает смену из сотрудника и очищает employee в смене
    
    def get_schedule(self, employees):  # вызывается в main что бы получаить готовый массив расписания
        result = []                     
        for emp in ActiveEmployeeIterator(employees):  # перебор сотрудников
            for shift in emp.shifts:  # и для каждого сотрудника перебираеются смены дата начало смены и ее состояние
                result.append({
                    "employee": emp.name,
                    "date": shift.date,
                    "start": shift.start,
                    "end": shift.end,
                    "state": shift.state.value
                })


        return result  # метод возвращает свормированный список

