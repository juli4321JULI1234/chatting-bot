from transitions.extensions import GraphMachine

from utils import send_text_message


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
        send_text_message(reply_token, "請參考我們的菜單1.飲料2.主菜3.甜點")

    def on_exit_state1(self, event):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "選擇飲料嗎?(是否)")

    def on_exit_state2(self, event):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "選擇主菜嗎?(是否)")

    def on_exit_state3(self, event):
        print("Leaving state3")

    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        send_text_message(reply_token, "選擇甜點嗎?(是否)")

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
        
