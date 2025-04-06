from abc import ABC
from hw_2.exceptions import LowFuelError, NotEnoughFuel
class Vehicle(ABC):
    def __init__(self, weight=1500, started=False, fuel=600, fuel_consumption=12.0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started:
            raise ValueError("Двигатель уже запущен.")
        if self.fuel <= 0:
            raise LowFuelError("Недостаточно топлива для запуска двигателя.")
        else:
            self.started = True
            return "Машина завелась"

    def move(self, distance):
        if not self.started:
            raise ValueError("Двигатель не запущен. Запустите двигатель перед перемещением.")
        else:
            fuel_needed = (self.fuel_consumption * distance)/100
            if self.fuel < fuel_needed:
                raise NotEnoughFuel("Недостаточно топлива для движения.")
            else:
                self.fuel -= fuel_needed
                return self.fuel

