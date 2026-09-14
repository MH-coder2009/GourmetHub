import time

from django.http import HttpResponseForbidden


class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print(f"[MIDDLEWARE] : url path :{request.path}")

        response = self.get_response(request)

        print(f"middleware response state:{response.status_code}")
        return response


class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        print(f"middleware request took {duration} second")
        return response


class BlokcIPMiddleware:
    BLOCK_IPS = ["127.0.0.1"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if ip in self.BLOCK_IPS:
            return HttpResponseForbidden("this ip cant rich to this site")
        return self.get_response(request)
