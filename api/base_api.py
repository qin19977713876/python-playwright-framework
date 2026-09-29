class BaseAPI:
    """所有接口类的父类，封装通用的请求方法。"""

    def __init__(self, request):
        self.request = request

    def get(self, path, **kwargs):
        return self.request.get(path, **kwargs)

    def post(self, path, **kwargs):
        return self.request.post(path, **kwargs)

    def put(self, path, **kwargs):
        return self.request.put(path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request.delete(path, **kwargs)