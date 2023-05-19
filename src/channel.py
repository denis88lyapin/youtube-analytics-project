import json
import os
from datetime import datetime
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = self.channel["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, new_id):
        raise AttributeError("property 'channel_id' of 'Channel' object has no setter")

    @classmethod
    def get_service(cls) -> object:
        """Возвращающий объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, file):
        """Сохраняет в файл значения атрибутов экземпляра `Channel` с указанием даты"""
        channel_json = {
            "id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriber_count,
            "videoCount": self.video_count,
            "viewCount": self.view_count,
            "date_loading": str(datetime.now())
        }

        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = "data"
        directory = os.path.join(current_dir, relative_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, file)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(channel_json, f, ensure_ascii=False, indent=2)
        else:
            with open(file_path, "a", encoding="utf-8") as f:
                json.dump(channel_json, f, ensure_ascii=False, indent=2)
