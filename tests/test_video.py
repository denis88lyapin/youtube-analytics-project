from src.video import Video

def test_video_init(video):
    assert video._video_id == "AWX4JnAnjBE"
    assert video.title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert isinstance(video.response, dict)
    assert video.url == "https://youtu.be/AWX4JnAnjBE"
    assert int(video.view_count) > 50
    assert int(video.like_count) > 50
    assert str(video) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video.duration) == "PT56M24S"


def test_video_init_invalid_id():
    video = Video("ivalid_id")
    assert video._video_id == "ivalid_id"
    assert video.title is None
    assert isinstance(video.response, dict)
    assert video.url is None
    assert video.view_count is None
    assert video.like_count is None
    assert str(video) is ''
    assert video.duration is None


def test_pl_video(pl_video):
    assert pl_video._video_id == "4fObz_qw9u4"
    assert pl_video._playlist_id == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
    assert pl_video.title == 'MoscowPython Meetup 78 - вступление'
    assert isinstance(pl_video.response, dict)
    assert pl_video.url == "https://youtu.be/4fObz_qw9u4"
    assert int(pl_video.view_count) > 50
    assert int(pl_video.like_count) > 5
    assert str(pl_video) == 'MoscowPython Meetup 78 - вступление'
    assert str(pl_video.duration) == 'PT4M17S'
