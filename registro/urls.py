from django.urls import path
from registro.views import criar_funcinario, criar_coleta_faces

# lista de URLs para o registro de funcionário
urlpatterns = [
    path('', criar_funcinario, name='criar_funcionario'),
    path('criar_coleta_faces/<int:funcionario_id>', criar_coleta_faces, name='criar_coleta_faces')
]