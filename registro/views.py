from django.shortcuts import redirect, render
from registro.forms import ColetasFacesForm, FuncionarioForm
from registro.models import ColetaFace, Funcionario

# Create your views here.
def criar_funcinario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            funcionario = form.save()
            return redirect('criar_coleta_faces', funcionario_id=funcionario.id)
    
    else:
        form = FuncionarioForm()
    
    return render(request, 'criar_funcionario.html', {'form': form})

def criar_coleta_faces(request, funcionario_id):
    funcionario = Funcionario.objects.get(id=funcionario_id)

    if request.method == 'POST':
        form = ColetasFacesForm(request.POST, request.FILES)
        if form.is_valid():
            # Itera sobre os arquivos enviados e cria uma entrada para cada imagem
            for image in request.FILES.getlist('images'):
                ColetaFace.objects.create(funcionario=funcionario, image=image)
                
    else:
        form = ColetasFacesForm()

    context = {
        'funcionario': funcionario,
        'form': form
    }
    return render(request, 'criar_coleta_faces.html', context)
    