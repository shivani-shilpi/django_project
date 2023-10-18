from django.urls import path
from . import views
from .views.user import *
from .views.view import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('result/<str:task_id>', check_result, name='check_result'),
    path('signup/', register, name='signup'),
    # path('login', Login.as_view(), name='login'),
    # path('logout', logout , name='logout'),
]
