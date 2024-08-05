from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicoDb, ClienteDb, CitaDb
from .serializer import MedicoSerializer, ClienteSerializer, CitaSerializer
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# def IndexView(request):
#     obj = MedicoDb.objects.all().order_by("id")
#     return render(request, 'index.html', {'obj': obj})

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = MedicoDb.objects.all()
    serializer_class = MedicoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = ClienteDb.objects.all()
    serializer_class = ClienteSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = CitaDb.objects.all()
    serializer_class = CitaSerializer


def mostrar_medicos(request):
    url = 'http://127.0.0.1:8080/medicos/'

    response = requests.get(url)

    medicos = []
    if response.status_code == 200:
        medicos = response.json()

    context = {
        'medicos': medicos
    }
    return render(request, 'mostrar_medicos.html', context)

@csrf_exempt
def crear_medico(request):
    if request.method == 'POST':
        nombre_medico = request.POST.get('nombre_medico')
        edad_medico = request.POST.get('edad_medico')
        especialidad = request.POST.get('especialidad')
        sexo_medico = request.POST.get('sexo_medico')

        url = 'http://127.0.0.1:8080/medicos/'

        data = {
            'nombre_medico': nombre_medico,
            'edad_medico': edad_medico,
            'especialidad': especialidad,
            'sexo_medico': sexo_medico
        }

        response = requests.post(url, json=data)

        if response.status_code == 201:
            return redirect('mostrar_medicos')
        else:
            print("error")
            return render(request, 'crear_medico.html', {'error': 'Error al crear médico'})

    return render(request, 'crear_medico.html')

@csrf_exempt
def borrar_medico(request, id):
    url = f'http://127.0.0.1:8080/medicos/{id}'
    if request.method == 'POST':
        response = requests.delete(url)
        if response.status_code == 204:  # No Content
            return redirect('mostrar_medicos')
        else:
            return HttpResponse(status=405)
    return HttpResponse(status=405)

def mostrar_clientes(request):
    url = 'http://127.0.0.1:8080/clientes/'

    response = requests.get(url)

    clientes = []
    if response.status_code == 200:
        clientes = response.json()

    context = {
        'clientes': clientes
    }
    return render(request, 'mostrar_clientes.html', context)

def mostrar_citas(request):
    url = 'http://127.0.0.1:8080/cita/'

    response = requests.get(url)

    citas = []
    if response.status_code == 200:
        citas = response.json()

    context = {
        'citas': citas
    }
    return render(request, 'mostrar_citas.html', context)