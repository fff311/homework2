"""
создайте класс `Plane`, наследник `Vehicle`
"""
from hw_2.base import Vehicle
from hw_2 import exceptions


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, cargo, max_cargo, **kwargs):
        if 'started' in kwargs:
            del kwargs['started']
        super().__init__(weight, fuel, fuel_consumption, **kwargs)
        self._max_cargo = max_cargo
        self.cargo = cargo
        self.started = False
    @property
    def max_cargo(self):
        return self._max_cargo
    @max_cargo.setter
    def max_cargo(self, value):
        try:
            if value < 0:
                raise ValueError()
            self._max_cargo = value
        except ValueError:
            return 'Максимальная грузоподъемность не может быть отрицательной'
    def load_cargo(self, amount):
        try:
            if amount < 0:
                raise ValueError("Количество груза не может быть отрицательным")
            if self.cargo + amount > self.max_cargo:
                raise exceptions.CargoOverload("Перегрузка груза")
            self.cargo += amount
        except exceptions.CargoOverload as e:
            raise e
        except Exception as e:
            raise e
    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo