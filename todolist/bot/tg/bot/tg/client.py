import requests

from bot.tg.bot.tg.dc import GetUpdatesResponse, SendMessageResponse


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str):
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        url = self.get_url("getUpdates")
        params = {
            "offset": offset,
            "timeout": timeout
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Django application",
            "content-type": "application/json"
        }
        response = requests.get(url=url, params=params, headers=headers)
        return GetUpdatesResponse.Schema().load(response.json())

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        url = self.get_url("sendMessage")

        data = {
            "chat_id": chat_id,
            "text": text
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Django application",
            "content-type": "application/json"
        }
        response = requests.post(url=url, headers=headers, json=data)
        return SendMessageResponse.Schema().load(response.json())

