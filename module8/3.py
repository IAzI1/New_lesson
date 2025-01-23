class IncorrectVinNumber(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

class IncorrectCarNumbers(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

class Car:
    def __init__(self, model, vin, car_number):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(car_number)

    @property
    def vin(self):
        return self.__vin

    @staticmethod
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер', vin_number)
        if 1000000 > vin_number < 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера', vin_number)

    @staticmethod
    def __is_valid_numbers(car_number):
        if not isinstance(car_number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров', car_number)
        if len(car_number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера', car_number)


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
