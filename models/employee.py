# Модель сотрудника. Хранит имя, должность и список смен
class Employee:
    def __init__(self, name: str, position: str):
        self.name = name #имя для сотрудника
        self.position = position #его нынешнаяя должность
        self.shifts = [] #массив отвечающий за смены сотрудника
    #метод для добавления смены
    def add_shift(self, shift):
        self.shifts.append(shift)
    #метод для вывода информации о имени сотрудника и его должности
    def __repr__(self):
        return f"Employee({self.name}, {self.position})"