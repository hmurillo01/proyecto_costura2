# En tu archivo urls.py

from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('listar_tareas/', views.lista_tareas, name='lista_tareas'),
    path('crear_estado/', views.crear_estado, name='crear_estado'),
    path('crear_tareas/', views.crear_tarea, name='crear_tarea'),
    path('tareas/modificar/<int:id>/', views.modificar_tarea, name='modificar_tarea'),
    path('tareas/eliminar/<int:id>', views.eliminar_tarea, name='eliminar_tarea'),
    path('crear_fabrica/', views.crear_fabrica, name='crear_fabrica'),
    path('crear_costurera/', views.crear_costurera, name='crear_costurera'),
    path('listar_costureras/', views.listar_costureras, name='listar_costureras'),
    path('modificar_costureras/<str:identificacion>/', views.modificar_costurera, name='modificar_costurera'),
    path('costureras/eliminar/<str:identificacion>', views.eliminar_costurera, name='eliminar_costurera')
    
]
