from django.urls import path, include
# from .views import IndexView
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, ClienteViewSet, CitaViewSet, crear_medico
from . import views

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet),
router.register(r'clientes', ClienteViewSet),
router.register(r'cita', CitaViewSet)

urlpatterns = [
    path('mostrar_medicos/', views.mostrar_medicos, name='mostrar_medicos'),
    path('crear_medico/', crear_medico, name='crear_medico'),
    path('mostrar_clientes/', views.mostrar_clientes, name='mostrar_clientes'),
    path('mostrar_citas/', views.mostrar_citas, name='mostrar_citas'),
    path('', include(router.urls))
]
