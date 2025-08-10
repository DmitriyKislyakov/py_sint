class Logger:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, logger=[]):
        self._logger = logger

    def log(self, message:str):
        self._logger.append(message)

    def get_logs(self):
        return self._logger

l1 = Logger()
l2 = Logger()
print(l1 is l2)
l1.log('213')
l2.log('sdfa')
print(l1.get_logs())
print(l2.get_logs())
# logger1 = Logger()
# logger2 = Logger()
#
# logger1.log("First message")
# logger2.log("Second message")
#
# print(assert logger1 is logger2, "Logger is not a singleton!"
# assert logger1.get_logs() == ["First message", "Second message"]
