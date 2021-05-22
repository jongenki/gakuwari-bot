from linebot.models import TextSendMessage
from linebot import LineBotApi
import json

file = open("info.json", "r")
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info["CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
print("実行されました")


def main():
    USER_ID = info["USER_ID"]
    messages = TextSendMessage(text="こんにちは！")
    line_bot_api.push_message(USER_ID, messages=messages)


main()
