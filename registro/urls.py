from django.urls import path
from . import views

# lista de URLs para o registro de funcionário
urlpatterns = [
    path('', views.index, name='index'),
]