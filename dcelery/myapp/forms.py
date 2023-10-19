from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreatUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ShowroomForm(forms.ModelForm):
	class Meta:
		model = Showroom
		fields = "__all__"
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'id': 'nameid'}),
			'location': forms.TextInput(attrs={'class':'form-control', 'id': 'locationid'}),
		}

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control', 'id': 'makeid'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'id': 'modelid'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'id': 'priceid'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'id': 'yearid'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'imageid'}),
        }