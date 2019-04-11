from django.shortcuts import render
from .form import *
from configuration.models import config

def landing(request):
    name = "СЭЭЭР!"
    form = ClientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    c1 = config.objects.all()
    return  render(request, 'landing/home.html', locals())

