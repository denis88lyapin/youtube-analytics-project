import json


def test_channel_init(channel_mock):
    # Проверяем, что инициализация экземпляра класса Channel проходит успешно
    assert channel_mock.channel_id == 'channel_id'
    assert channel_mock.channel == {
        'items': [{
            'id': 'channel_id',
            'snippet': {'title': 'Channel Title'},
            'statistics': {'viewCount': 100, 'subscriberCount': 500}
        }]
    }

def test_channel_print_info(channel_mock, capsys):
    # Проверяем, что метод print_info выводит информацию о канале в консоль
    channel_mock.print_info()
    captured = capsys.readouterr()
    assert json.loads(captured.out) == {
        'items': [{
            'id': 'channel_id',
            'snippet': {'title': 'Channel Title'},
            'statistics': {'viewCount': 100, 'subscriberCount': 500}
        }]
    }

