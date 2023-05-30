import pytest
from src.channel import Channel
from src.video import Video, PLVideo


@pytest.fixture
def channel():
    """Создание экземпляра класса Channel для теста"""
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


@pytest.fixture
def channel1():
    """Создание экземпляра класса Channel для теста"""
    return Channel('UCwHL6WHUarjGfUM_586me8w')


@pytest.fixture
def video():
    """Создание экземпляра класса Video для теста"""
    return Video("AWX4JnAnjBE")


@pytest.fixture
def pl_video():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
