class Message:
    def __init__(self, text: str, fl_like=False):
        self.text = text
        self.fl_like = fl_like

class Viber:
    msgs = {}
    id = 0

    def add_message(self, msg):
        pass