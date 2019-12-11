from transitions.extensions import GraphMachine

from flask import Flask, jsonify, request, abort, send_file

from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

from utils import send_text_message

# get channel_secret and channel_access_token from your environment variable
line_bot_api = LineBotApi("yDfS/npqyljNHaMDb96ffIeq5amro6eMZB/lRzDiZSMoeRj6GcVPhNjBepQ3rX3fYo/MVg2s1Ka7TwNjmK31TeOwLX22/jqAGHBT0RCRcHIuIv4ezz+ep2En9YlhkVatV2YPbHfFfNNF4KBlSpJdoAdB04t89/1O/w1cDnyilFU=")

#FSM REPLY
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def waiter1(self, event):
        text = event.message.text
        return text.lower() == "是"

    def waiter0(self, event):
        text = event.message.text
        return text.lower() == "否"

    def menu1(self, event):
        text = event.message.text
        return text.lower() == "飲料"

    def menu2(self, event):
        text = event.message.text
        return text.lower() == "主菜"

    def menu3(self, event):
        text = event.message.text
        return text.lower() == "甜點"

    def order1(self, event):
        text = event.message.text
        return text.lower() == "是"

    def order2(self, event):
        text = event.message.text
        return text.lower() == "是"

    def order3(self, event):
        text = event.message.text
        return text.lower() == "是"

    def order10(self, event):
        text = event.message.text
        return text.lower() == "否"

    def order20(self, event):
        text = event.message.text
        return text.lower() == "否"

    def order30(self, event):
        text = event.message.text
        return text.lower() == "否"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "請看菜單選擇想要的餐點\n1.飲料\n2.主菜\n3.甜點")

    def on_exit_state1(self, event):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "選擇飲料嗎?(是/否)")

    def on_exit_state2(self, event):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "選擇主菜嗎?(是/否)")

    def on_exit_state3(self, event):
        print("Leaving state3")

    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        send_text_message(reply_token, "選擇甜點嗎?(是/否)")

    def on_exit_state4(self, event):
        print("Leaving state4")
    
    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "好的飲料馬上來!")
        self.go_back()

    def on_exit_state5(self):

        print("Leaving state5")
    
    def on_enter_state6(self, event):
        print("I'm entering state6")

        reply_token = event.reply_token
        send_text_message(reply_token, "好的主菜馬上來!")
        self.go_back()

    def on_exit_state6(self):

        print("Leaving state6")
    
    def on_enter_state7(self, event):
        print("I'm entering state7")

        reply_token = event.reply_token
        send_text_message(reply_token, "好的甜點馬上來!")
        self.go_back()

    def on_exit_state7(self):

        print("Leaving state7")
        