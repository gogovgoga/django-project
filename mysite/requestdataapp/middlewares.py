import time
from django.http import HttpRequest, HttpResponseForbidden


def set_useragent_on_request_middleware(get_response):
    print("initial call")

    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response

    return middleware


class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print("requests count", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("responses count", self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print("got", self.exceptions_count, "exceptions so far")


class ThrottlingMiddleware:
    def __init__(self, get_response, requests_per_second=500):
        self.get_response = get_response
        self.requests_per_second = requests_per_second
        self.request_history = {}

    def __call__(self, request):
        ip = self._get_client_ip(request)
        current_time = time.time()

        if ip in self.request_history:
            last_request_time = self.request_history[ip]
            elapsed_time = current_time - last_request_time
            time_per_request = 1 / self.requests_per_second

            if elapsed_time < time_per_request:
                error_message = 'Too many requests. Please try again later.'
                return HttpResponseForbidden(error_message)

        self.request_history[ip] = current_time
        return self.get_response(request)

    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
