import pytest

from hw_2.plane import Plane
from hw_2.car import Car
from hw_2.engine import Engine


@pytest.fixture
def engine_test():
    engine = Engine(volume=2.0, pistons=4)
    yield engine


@pytest.fixture
def car_test():
    engine_car = Engine(volume=2.0, pistons=4)
    car = Car(
        weight=1500, started=False, fuel=70,
        fuel_consumption=12.0, engine=engine_car
    )
    yield car


@pytest.fixture
def plane_test():
    plane = Plane(
        weight = 10000, started = False, fuel = 200.0,
        fuel_consumption = 50.0, cargo = 0, max_cargo = 1000
    )
    yield plane
