from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm 
from myapp.forms import ShowroomForm
from django.views import View
from myapp.models import *
from django.contrib import messages

def showroom(request):
    showrooms = Showroom.objects.all()
    return render (request, "showrooms/showroom.html", {'showrooms': showrooms} )

def create_showroom(request):
    if request.method == 'POST':
       form = ShowroomForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('showroom')
    else: 
        form = ShowroomForm()
    return render(request, 'showrooms/new_showroom.html', {'form': form})

def update_showroom(request, showroom_id):
    showroom = get_object_or_404(Showroom, pk=showroom_id)
    if request.method == 'POST':
        form = ShowroomForm(request.POST, instance=showroom)
        if form.is_valid():
            form.save()
            return redirect('showroom')
    else:
        form = ShowroomForm(instance=showroom)
    return render(request, 'showrooms/update_showroom.html', {'form': form})

def delete_showroom(request, showroom_id):
    showroom = get_object_or_404(Showroom, pk=showroom_id)
    if request.method == "POST":
        showroom.delete()
        messages.success(request,  'The blog has been deleted successfully.')
        return redirect('showroom')



