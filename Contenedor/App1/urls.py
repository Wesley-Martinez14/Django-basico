from django.urls import path
from .views import IndexView, AutorView, CustomLoginView

urlpatterns = [
    path('', IndexView),
    path('autor/<int:id>', AutorView),
    path('login/', CustomLoginView.as_view(), name='login'),
]