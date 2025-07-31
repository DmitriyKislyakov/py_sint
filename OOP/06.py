class Server:
    __ip_s = 0

    def __new__(cls, *args, **kwargs):
        cls.__ip_s += 1
        return super().__new__(cls)

    def __init__(self):
        self.serv_ip = self.__ip_s
        self.storage = []
        self.router = None

    def send_data(self, data):
        if self.router:
           self.router.buffer.append(data)

    def get_data(self):
        buf = self.storage[:]
        self.storage.clear()
        return buf

    def get_ip(self):
        return self.serv_ip


class Router:
    __ip_r = 0

    def __new__(cls, *args, **kwargs):
        cls.__ip_r += 1
        return super().__new__(cls)

    def __init__(self):
        self.rout_ip = self.__ip_r
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.serv_ip] = server
        server.router = self

    def unlink(self, server):
        self.servers.pop(server.serv_ip, False)
        server.router = None

    def send_data(self):
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers[d.ip].storage.append(d.data)
        self.buffer.clear()


class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


sv1 = Server()
sv2 = Server()
print(sv1.get_ip())
print(sv2.get_ip())
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()