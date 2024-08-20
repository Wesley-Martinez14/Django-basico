from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicoDb, ClienteDb, CitaDb
from .serializer import MedicoSerializer, ClienteSerializer, CitaSerializer
import requests
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import httpx
from django.core.paginator import Paginator
import io
from reportlab.pdfgen import canvas

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


async def mostrar_medicos(request):
    url = 'http://127.0.0.1:8080/medicos/'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    medicos = []
    if response.status_code == 200:
        medicos = response.json()

    paginator = Paginator(medicos, 2)
    page_number =  request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'medicos': page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'mostrar_medicos.html', context)

@csrf_exempt
async def crear_medico(request):
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
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data)

        if response.status_code == 201:
            return redirect('mostrar_medicos')
        else:
            print("error")
            return render(request, 'crear_medico.html', {'error': 'Error al crear médico'})

    return render(request, 'crear_medico.html')


@csrf_exempt
async def editar_medico(request, id):

    url = f'http://127.0.0.1:8080/medicos/{id}/'
    if request.method == 'POST':
        nombre_medico = request.POST.get('nombre_medico')
        edad_medico = request.POST.get('edad_medico')
        especialidad = request.POST.get('especialidad')
        sexo_medico = request.POST.get('sexo_medico')


        data = {
            'nombre_medico': nombre_medico,
            'edad_medico': edad_medico,
            'especialidad': especialidad,
            'sexo_medico': sexo_medico
        }
        async with httpx.AsyncClient() as client:
            response = await client.put(url, json=data)
        
        if response.status_code == 200:
            return redirect('mostrar_medicos')  
        else:
            return HttpResponse(f"Error al actualizar el médico: {response.status_code} - {response.text}", status=response.status_code)


    response = requests.get(url)
    if response.status_code == 200:
        medico = response.json()
        return render(request, 'editar_medico.html', {'medico': medico})
    else:
        return HttpResponse(f"Error al obtener el médico: {response.status_code}", status=response.status_code)

       
@csrf_exempt
async def borrar_medico(request, id):
    url = f'http://127.0.0.1:8080/medicos/{id}/'
    if request.method == 'POST':
        async with httpx.AsyncClient() as client:
            response = await client.delete(url)
        if response.status_code == 204:
            return redirect('mostrar_medicos')
        else:
            return HttpResponse(status=405)
    return HttpResponse(status=405)

async def mostrar_clientes(request):
    url = 'http://127.0.0.1:8080/clientes/'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    clientes = []
    if response.status_code == 200:
        clientes = response.json()

    context = {
        'clientes': clientes
    }
    return render(request, 'mostrar_clientes.html', context)

async def mostrar_citas(request):
    url = 'http://127.0.0.1:8080/cita/'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    citas = []
    if response.status_code == 200:
        citas = response.json()

    context = {
        'citas': citas
    }
    return render(request, 'mostrar_citas.html', context)

def generar_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, "Lista de Medicos")

    medicos = MedicoDb.objects.all()

    y= 720

    p.setFont("Helvetica", 12)
    for m in medicos:
        p.drawString(100, y, f"Nombre: {m.nombre_medico}, Edad: {m.edad_medico}, Especialidad: {m.especialidad} ")
        y -= 20

        if y < 100:
            p.showPage()
            y = 750
    
    p.showPage()
    p.save()


    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename="Lista_medico.pdf")
