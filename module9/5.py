class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start: int, stop: int, step=1):
        if step == 0:
            raise StepValueError
        self.start, self.stop, self.step, self.pointer = start, stop, step, start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.pointer < self.stop < self.start or self.pointer > self.stop > self.start:
            raise StopIteration

        result = self.pointer
        self.pointer += self.step

        return result


try:
    # iter1 = Iterator(100, 200, 0)
    # iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')