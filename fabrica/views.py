from django.shortcuts import render, redirect, get_object_or_404
from .models import Tareas
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.views import LoginView
from .forms import TareaForm,FabricaForm,EstadoForm,CostureraForm, Costureras


def index(request):
    # Aquí puedes incluir cualquier lógica necesaria para la página de inicio
    # Por ejemplo, recuperar datos de la base de datos, procesar formularios, etc.
    return render(request, 'index.html')  # Renderiza la plantilla index.html
class CustomLoginView(LoginView):
    template_name = 'login.html'  # Nombre de la plantilla de inicio de sesión personalizada

def crear_costurera(request):
    if request.method == 'POST':
        form = CostureraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Costurera creada con éxito!') 
            #return redirect('lista_costureras')
    else:
        form = CostureraForm()

    # Si el formulario se ha enviado con éxito o es una solicitud GET, 
    # renderiza un nuevo formulario limpio
    return render(request, 'crear_costurera.html', {'form': form})
  
  #Modificar costureras
def modificar_costurera(request, identificacion):
    # Obtener la costurera a modificar
    costurera = get_object_or_404(Costureras, identificacion=identificacion)

    if request.method == 'POST':
        # Rellenar el formulario con los datos de la costurera y los datos enviados en la solicitud POST
        form = CostureraForm(request.POST, instance=costurera)
        if form.is_valid():
            # Guardar los cambios en la costurera
            form.save()
            # Redireccionar a la página de listar costureras
            return redirect('listar_costureras')
    else:
        # Rellenar el formulario con los datos actuales de la costurera
        form = CostureraForm(instance=costurera)

    # Renderizar la plantilla para modificar la costurera
    return render(request, 'modificar_costurera.html', {'form': form, 'costurera': costurera})

def listar_costureras(request):
    costureras = Costureras.objects.all()
    return render(request, 'listar_costureras.html', {'costureras': costureras})
  
def eliminar_costurera(request, identificacion):
    costurera = get_object_or_404(Costureras, identificacion=identificacion)
    if request.method == 'POST':
        costurera.delete()
      ## return redirect('lista_costureras')  # Redirige a la lista de costureras después de eliminar
    return render(request, 'eliminar_costurera.html', {'costurera': costurera})

def crear_fabrica(request):
    if request.method == 'POST':
        form = FabricaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fabricas')
    else:
        form = FabricaForm()
    return render(request, 'crear_fabrica.html', {'form': form})

def crear_estado(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito o a la lista de estados
           # return redirect('lista_estados')  # Ajusta 'lista_estados' a la URL de tu lista de estados
    else:
        form = EstadoForm()
    return render(request, 'crear_estado.html', {'form': form})

def lista_tareas(request):
    tareas = Tareas.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})

def detalle_tarea(request, id):
    tarea = get_object_or_404(Tareas, id=id)
    return render(request, 'detalle_tarea.html', {'tarea': tarea})

def modificar_tarea(request, id):
    tarea = get_object_or_404(Tareas, id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')  # Redireccionar a la lista de tareas
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'modificar_tarea.html', {'form': form})  

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tareas, id=id)
    tarea.delete()
    return redirect('lista_tareas')


  


