import os
from googleapiclient.discovery import build


class Video:
    """Класс для видео ютуб. Инициализируется по id видео"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        self._video_id = video_id
        try:
            self.response = self.youtube.videos().list(part='snippet,statistics,contentDetails',
                                                       id=self._video_id).execute()
            self.title = self.response["items"][0]["snippet"]["title"]
            self.url = f"https://youtu.be/{self._video_id}"
            self.view_count = self.response["items"][0]["statistics"]["viewCount"]
            self.like_count = self.response["items"][0]["statistics"]["likeCount"]
            self.duration = self.response['items'][0]['contentDetails']['duration']
        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None
            self.duration = None

    def __str__(self) -> str:
        if self.title:
            return self.title
        else:
            return ''


class PLVideo(Video):
    """Класс для видео ютуб. Инициализируется по id видео и id плейлиста."""

    def __init__(self, video_id: str, playlist_id: str) -> None:
        super().__init__(video_id)
        self._playlist_id = playlist_id
