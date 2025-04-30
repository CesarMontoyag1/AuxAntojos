from django.urls import path,include
from .views import create_entrepreneur, success, entrepreneur_list, delete_entrepreneur

urlpatterns = [
path('crear-emprendedor/', create_entrepreneur, name='create_entrepreneur'),
path('registro-exitoso/', success, name='success'),
path('emprendedores/', entrepreneur_list, name='entrepreneur_list'),
path('eliminar-emprendedor/<int:pk>/', delete_entrepreneur, name='delete_entrepreneur'),

]