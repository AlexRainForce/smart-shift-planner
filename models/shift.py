from enum import Enum

# перечисление состояний смен

class ShiftState(Enum):
    PLANNED = "запланирована"
    CONFIRMED = "подтверждена"
    CANCELLED = "отменена"

# Модель смены. Паттерн State - смена меняет состояние через методы confirm/cancel

class Shift:
    def __init__(self, date: str, start: str, end: str):
        self.date = date  # дата смены
        self.start = start  # начало смены
        self.end = end  # конец смены
        self.state = ShiftState.PLANNED  # состояние - запланированно
        self.employee = None  # cотрудники

    # подтвердить

    def confirm(self):
        self.state = ShiftState.CONFIRMED 

    # отменить

    def cancel(self):
        self.state = ShiftState.CANCELLED

    # возвращаем значение

    def __repr__(self):
        return f"Shift({self.date}, {self.start}-{self.end}, {self.state.value})"