"""
создайте класс `Car`, наследник `Vehicle`
"""
from hw_2.base import Vehicle
from hw_2.engine import Engine
from hw_2.exceptions import  NotEnoughFuel
class Car(Vehicle):
    def __init__(self, **kwargs):
        engine = kwargs.pop('engine', None)
        super().__init__(**kwargs)
        self.engine = engine

    def set_engine(self, engine: Engine):
        try:
            if isinstance(engine, Engine):
                if not isinstance(engine.volume, (int, float)) or not isinstance(engine.pistons, int):
                    raise TypeError()
                self.engine = engine
                return self.engine
            else:
                raise TypeError()
        except TypeError as t:
            return 'ошибка в типе данных'



