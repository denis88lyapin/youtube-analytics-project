import datetime
from src.video import PLVideo


def test_playlist_init(playlist):
    assert playlist.playlist_id == 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'
    assert playlist.title == "Moscow Python Meetup №81"
    assert playlist.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
    assert isinstance(playlist.playlist_videos[0], PLVideo)


def test_playlist_total_duration(playlist):
    duration = playlist.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0


def test_show_best_video(playlist):
    assert playlist.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
