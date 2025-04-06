import pytest

from hw_2.car import Car
from hw_2.engine import Engine
from hw_2.exceptions import LowFuelError, NotEnoughFuel


class TestCar:
    """Набор тестов для проверки функциональности класса Car."""

    def test_car_set_engine(self, car_test: Car):
        """
        Установка нового двигателя на автомобиль.
        """
        new_engine = Engine(volume=3.0, pistons=6)
        car_test.set_engine(new_engine)
        assert car_test.engine == new_engine

    def test_car_start_engine(self, car_test: Car):
        """
        Запуск двигателя автомобиля.
        """
        car_test.start()
        assert car_test.started is True

    def test_double_start(self, car_test: Car):
        """
        Повторный запуск двигателя автомобиля.
        """
        car_test.start()
        with pytest.raises(ValueError):
            car_test.start()

    def test_car_dont_start_engine_with_low_fuel(self, car_test: Car):
        """
        Автомобиль не должен запускаться при низком уровне топлива.
        """
        car_test.fuel = 0
        with pytest.raises(LowFuelError):
            car_test.start()

    def test_car_move(self, car_test: Car):
        """
        Передвижение автомобиля на заданное расстояние.
        """
        car_test.start()
        distance = 50
        car_test.move(distance)
        assert car_test.fuel == 64

    def test_not_enough_fuel(self, car_test: Car):
        """
        Передвижение автомобиля на большое расстояние,
        когда топлива не хватит.
        """
        car_test.start()
        distance = 10000
        with pytest.raises(NotEnoughFuel):
            car_test.move(distance)

    def test_car_dont_move(self, car_test: Car):
        """
        Автомобиль не может ехать без запущенного двигателя.
        """
        distance = 50
        with pytest.raises(ValueError):
            car_test.move(distance)
