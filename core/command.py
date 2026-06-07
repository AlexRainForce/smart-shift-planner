from abc import ABC, abstractmethod
# Паттерн Command - абстрактный интерфейс для всех команд
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass
# Класс реализующий интерфейс Command который служит оберткой для сотрудников и смен
class AssignShiftCommand(Command):
    def __init__(self, employee, shift):
        self.employee = employee    #Конструктор принимает объект сотрудника
        self.shift = shift          # и его смену
    
    def execute(self):                          #метод добавляет сотруднику смену а в смену записывает данного сотрудника
        self.employee.add_shift(self.shift)     
        self.shift.employee = self.employee     
    
    def undo(self):                            #метод удаляет данную смену у сотрудника и в самой смене уберает сотрудника внутри смены
        self.employee.shifts.remove(self.shift)
        self.shift.employee = None      