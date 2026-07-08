from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Content',
        'list': ['first', 'second', 'third'],
        'dict': {'first': 1},
        'bool': False,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("Hello, world. You're at the polls about.")