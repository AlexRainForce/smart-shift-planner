from abc import ABC, abstractmethod
import openpyxl
# Паттерн Strategy - интерфейс экспорта, можно добавить CSVExporter по той же схеме
class BaseExporter(ABC):
    @abstractmethod
    def export(self, data: list, path: str):
        pass
# Реализация экспорта в xlsx
class ExcelExporter(BaseExporter):
    def export(self, data: list, path: str):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Сотрудник", "Дата", "Начало", "Конец", "Статус"])
        
        for row in data:
            ws.append([
                row["employee"],
                row["date"],
                row["start"],
                row["end"],
                row["state"]
            ])
        
        wb.save(path)  # сохранение книги 