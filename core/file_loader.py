from abc import ABC, abstractmethod
import openpyxl

# Паттерн Strategy - интерфейс загрузки, можно добавить CSVLoader по той же схеме
class BaseLoader(ABC):
    @abstractmethod
    def load(self, path: str):
        pass

# Класс для загрузки данных из книги Excel
class ExcelLoader(BaseLoader):
    def load(self, path: str):
        wb = openpyxl.load_workbook(path)   # метод принимает строку с путём к файлу
        ws = wb.active                       # выбор активного листа
        data = []                            # список для хранения данных
        for row in ws.iter_rows(min_row=2, values_only=True):  # перебор строк начиная со второй
            data.append(row)                                    # добавление строки в список
        return data                                             # возврат заполненного списка