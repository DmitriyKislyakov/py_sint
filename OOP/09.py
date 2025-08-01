class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)
    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')
        print( f'url:{request["url"]}')
        return f'url:{request["url"]}'

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        f = getattr(self, method.lower(), False)
        if f:
            return f(request)


dv = DetailView()  # по умолчанию methods=('GET',)
dv = DetailView(methods=('PUT', 'POST', 'GET'))
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')