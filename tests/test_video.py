
def test_video_init(video):
    assert video._video_id == "AWX4JnAnjBE"
    assert video.title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert isinstance(video.response, dict)
    assert video.url == "https://www.youtube.com/watch?v=AWX4JnAnjBE"
    assert int(video.view_count) > 50
    assert int(video.like_count) > 50
    assert str(video) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_pl_video(pl_video):
    assert pl_video._video_id == "4fObz_qw9u4"
    assert pl_video.playlist_id == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
    assert pl_video.title == 'MoscowPython Meetup 78 - вступление'
    assert isinstance(pl_video.response, dict)
    assert pl_video.url == "https://www.youtube.com/watch?v=4fObz_qw9u4"
    assert int(pl_video.view_count) > 50
    assert int(pl_video.like_count) > 5
    assert str(pl_video) == 'MoscowPython Meetup 78 - вступление'

