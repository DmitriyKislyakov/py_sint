class Message:
    __count = 0
    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return super().__new__(cls)


    def __init__(self, text: str, fl_like=False):
        self.text = text
        self.fl_like = fl_like
        self.msg_id = self.__count


class Viber:
    msgs = {}

    @classmethod
    def add_message(cls, msg):
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.msgs.pop(id(msg))

    @classmethod
    def show_last_message(cls, n:int):
        values = tuple(cls.msgs.values())
        for m in values[-n:]:
            print(m.text)

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

m1 = Message('asdasd')
m2 = Message('asdasda')
msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(m1)
Viber.add_message(m2)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.show_last_message(5)
Viber.remove_message(msg)
print(Viber.total_messages())
