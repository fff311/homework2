import pytest
from hw_2.engine import Engine
from dataclasses import is_dataclass

class TestEngine:
    """Набор тестов для проверки функциональности класса Engine."""

    def test_engine_is_dataclass(self, engine_test: Engine):
        """
        Engine является датаклассом.
        """
        assert is_dataclass(engine_test)

    def test_engine_initialization(self):
        """
        Инициализации экземпляра Engine с заданными атрибутами.
        """
        volume = 2.5
        pistons = 4
        engine = Engine(volume=volume, pistons=pistons)
        assert engine.volume == volume
        assert engine.pistons == pistons

    def test_volume_is_float(self, engine_test: Engine):
        """
        Volume является float.
        """
        assert isinstance(engine_test.volume, float)

    def test_pistons_is_int(self, engine_test: Engine):
        """
        Pistons является int.
        """
        assert isinstance(engine_test.pistons, int)
