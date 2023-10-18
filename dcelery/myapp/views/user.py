from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.forms import UserCreationForm  
from django.views import View

def register(request):  
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()  
        messages.success(request, 'Account created successfully')  
  
    else:  
        form = UserCreationForm()  
        context = {  
            'form':form  
        }  
    return render(request, 'myapp/register.html', context)  