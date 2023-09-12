from django.http import HttpResponse


def index(request):
    return HttpResponse("THIS IS BACKEND " * 700)
