from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index),
    url(r'^index$', views.index),
    url(r'^menu$', views.menu),
    url(r'^contact$', views.contact),
    url(r'^about$', views.about),
    url(r'^localisation$', views.localisation),

]