from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    context['flag_index'] = ['active']
    return render(request, 'lamian/index.html', context)


def menu(request):
    context = {}
    context['flag_menu'] = ['active']
    return render(request, 'lamian/menu.html', context)


def contact(request):
    context = {}
    context['flag_contact'] = ['active']
    return render(request, 'lamian/contact.html', context)


def localisation(request):
    context = {}
    context['flag_localisation'] = ['active']
    return render(request, 'lamian/localisation.html', context)


def about(request):
    context = {}
    context['flag_about'] = ['active']
    return render(request, 'lamian/about.html', context)