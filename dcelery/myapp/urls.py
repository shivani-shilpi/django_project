from django.urls import path
from . import views
from .views.user import *
from .views.view import *
from .views.showrooms import *
from .views.cars import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('result/<str:task_id>', check_result, name='check_result'),
    path('signup/', register, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('showroom/', showroom, name='showroom'),
    path('new_showroom/', create_showroom, name='new_showroom'),
    path('delete/<int:showroom_id>', delete_showroom, name='delete'),
    path('update_showroom/<int:showroom_id>', update_showroom, name='update_showroom'),
    path('car/', car, name='car'),
    path('new_car/', create_car, name='new_car'),
    path('update_car/<int:car_id>', update_car, name='update_car'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)