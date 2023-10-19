from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.forms import UserCreationForm 
from myapp.forms import CreatUserForm
from django.views import View
from myapp.models import *

def register(request):
  form = CreatUserForm()
  if request.method == 'POST':
    form = CreatUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')

      group = Group.objects.get(name='customer')
      user.groups.add(group)

      messages.success(request, "Account was created for " + username)
      return redirect('login')

  context = {'form': form} 
  return render(request, 'myapp/register.html', context) 

def login(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #   login(request, user)
    #   messages.success(request, f"You are now logged in as {username}.")
    #   return redirect("myapp/index")
    # else:
    #   messages.error(request,"Invalid username or password.")
        
  context = {}
  return render(request, 'myapp/login.html', context) 

def logout(request):
  logout(request)
  messages.info(request, "You have successfully logged out.")
  return redirect('login')