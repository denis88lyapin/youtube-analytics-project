import pytest


def test_channel_init(channel):
    """Проверка инициализации экземпляра класса Channel"""
    assert channel._channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'
    assert channel.title is not None
    assert channel.description is not None
    assert channel.url is not None
    assert channel.subscriber_count is not None
    assert channel.video_count is not None
    assert channel.view_count is not None


def test_channel_print_info(channel, capsys):
    """Проверка метода print_info"""
    channel.print_info()
    captured = capsys.readouterr()
    assert captured.out != ''


def test_channel_id(channel):
    """Проверка метода channel_id"""
    assert channel._channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'


def test_channel_id_exclusion(channel):
    """Проверка метода channel_id с исключением"""
    with pytest.raises(AttributeError) as e:
        channel._channel_id = "id"
    assert str(e.value) == "property 'channel_id' of 'Channel' object has no setter"


def test_get_service(channel):
    """Проверка метода get_service"""
    service = channel.get_service()
    assert isinstance(service, type(channel.youtube))


def test_channel_to_json(channel, tmp_path):
    """Проверка метода to_json"""
    file_path = tmp_path / 'channel.json'
    channel.to_json(str(file_path))
    assert file_path.exists()
    assert file_path.read_text() != ''


def test_str_method(channel):
    """Проверка метода __str__"""
    assert isinstance(str(channel), str)


def test_add_method(channel, channel1):
    """Проверка метода __add__"""
    assert (channel + channel1) > int(channel.subscriber_count)


def test_sub_method(channel, channel1):
    """Проверка метода __sub__"""
    assert (channel - channel1) < int(channel.subscriber_count)


def test_comparisons_methods(channel, channel1):
    """Проверка методов сравнения"""
    assert (channel > channel1) is False
    assert (channel >= channel1) is False
    assert (channel < channel1) is True
    assert (channel <= channel1) is True
    assert (channel == channel1) is False
