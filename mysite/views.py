"""Views"""
from django.http import HttpResponse


def index(request):
    """Basic View"""
    return HttpResponse('Hello world!')
