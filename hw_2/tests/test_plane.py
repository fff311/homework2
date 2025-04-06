import pytest

from hw_2.plane import Plane
from hw_2.exceptions import CargoOverload, LowFuelError, NotEnoughFuel


class TestPlane:
    """Набор тестов для проверки функциональности класса Plane."""

    def test_start_with_fuel(self, plane_test: Plane):
        """
        Запуск самолета с топливом.
        """
        plane_test.start()
        assert plane_test.started is True

    def test_start_without_fuel(self, plane_test: Plane):
        """
        Запуск самолета без топлива.
        """
        plane_test.fuel = 0
        with pytest.raises(LowFuelError):
            plane_test.start()

    def test_move_without_enough_fuel(self, plane_test: Plane):
        """
        Запуск самолета с недостаточным количеством топлива.
        """
        plane_test.fuel = 10.0
        plane_test.fuel_consumption = 5.0
        plane_test.start()
        with pytest.raises(NotEnoughFuel):
            plane_test.move(500)

    def test_load_cargo(self, plane_test: Plane):
        """
        Загрузка самолета грузом, не превышающий max_cargo.
        """
        amount_less = 999
        plane_test.load_cargo(amount_less)
        assert plane_test.cargo == 999

    def test_overload(self, plane_test: Plane):
        """
        Загрузка самолета грузом, превышающий max_cargo.
        """
        amount_more = 1001
        with pytest.raises(CargoOverload):
            plane_test.load_cargo(amount_more)
