from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    context['index'] = ['active']
    return render(request, 'lamian/index.html', context)


def menu(request):
    context = {}
    context['menu'] = ['active']
    return render(request, 'lamian/menu.html', context)
