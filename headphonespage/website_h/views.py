from django.shortcuts import render
from django.conf import settings

def indexView(request):
    return render(request, 'index.html')

