class ActiveEmployeeIterator:
    def __init__(self, employers):
        self.employers = employers
        self.index = 0

    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.employers):
          emp = self.employers[self.index]
          self.index += 1
          if emp.active:
            return emp
        raise StopIteration