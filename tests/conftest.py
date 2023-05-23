import pytest

from src.channel import Channel


@pytest.fixture
def channel():
    """Создание экземпляра класса Channel для теста"""
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


@pytest.fixture
def channel1():
    """Создание экземпляра класса Channel для теста"""
    return Channel('UCwHL6WHUarjGfUM_586me8w')
