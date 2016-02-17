from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello World, Django")
def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s." % my_args)
def acounts(request):
    return HttpResponse(
    '''{
    "local_port": 1080, 
    "method": "aes-256-cfb", 
    "password": "44982810", 
    "server": "us1.iss.tf", 
    "server_port": "443", 
    "timeout": 60
    }''')