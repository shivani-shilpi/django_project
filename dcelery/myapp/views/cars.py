from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm 
from myapp.forms import CarForm
from django.views import View
from myapp.models import *

def car(request):
    # cars = Car.objects.all()
    return render(request, 'cars/car.html')

def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car')
    else:
        form = CarForm()
    return render (request, 'cars/new_car.html', {'form': form}) 


def update_car(request, car_id):
    pass

