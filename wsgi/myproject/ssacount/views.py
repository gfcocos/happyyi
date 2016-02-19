from django.shortcuts import render
from django.http import HttpResponse
from .models import SSAcount

# Create your views here.
def index(request):
    return HttpResponse("Hello World, Django")


def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s." % my_args)


def acounts(request):
    acounts = SSAcount.objects.order_by('ping')
    if len(acounts) > 0:
        acount = acounts[0]
        output = ('{ "local_port": %s, "method": "%s", "password": "%s", "server": "%s", "server_port": "%s"}' % (1080, acount.method, acount.password, acount.server, acount.server_port))
        return HttpResponse(output)
    else:
        return HttpResponse('Error,No Data')
    # acount = acounts.
