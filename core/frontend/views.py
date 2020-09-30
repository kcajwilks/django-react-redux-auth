from django.shortcuts import render

def index(request):
    """ Render React HTML index """
    return render(request, 'frontend/index.html')