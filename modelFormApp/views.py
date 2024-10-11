from django.shortcuts import render
from modelFormApp.forms import FormProyecto
from modelFormApp.models import Proyecto
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoProyecto(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request,'proyectos.html',data)
