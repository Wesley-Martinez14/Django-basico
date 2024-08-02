from django.shortcuts import render, get_object_or_404
from .models import AutorDb
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')

@login_required
def IndexView(request):
    ''' Esto es la pagina principal
    '''
    objeto = AutorDb.objects.all().order_by("id")
    return render(request, "index.html", {"objeto":objeto})

@login_required
def AutorView(request, id):
    autor = get_object_or_404(AutorDb, id=id)
    return render(request, "autor.html", {"objeto":autor})
