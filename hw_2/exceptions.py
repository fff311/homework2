"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __init__(self, message="Уровень топлива слишком низкий!!!!"):
        self.message = message
        super().__init__(self.message)

class NotEnoughFuel(Exception):
    def __init__(self, message="Недостаточно топлива для выполнения операции"):
        self.message = message
        super().__init__(self.message)

class CargoOverload(Exception):
    def __init__(self, message="Перегрузка груза. Превышен допустимый лимит."):
        self.message = message
        super().__init__(self.message)