from django.shortcuts import render

def list_view(request):
    context = {
        'items': ['Ассаламу алейкум бро', 'Biloliddin', 'Sodiq - Sariq', 'dalbanutiy'],
    }
    return render(request, 'list.html', context)