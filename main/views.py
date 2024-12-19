from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    context = {
        'name': 'Иван',
    }
    return render(request, 'index.html', context=context)