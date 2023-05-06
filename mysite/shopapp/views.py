from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def shop_index(request: HttpRequest):
    print(request.path)
    print(request.method)
    print(request.headers)
    return HttpResponse('<h1>Hello World</h1>')

