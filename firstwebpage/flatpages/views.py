from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest):
    return render(request, 'static_handler.html')

def hello(request: HttpRequest):
    return HttpResponse("Hello?", content_type="text/plain")