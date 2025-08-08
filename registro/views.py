from django.http import StreamingHttpResponse
from django.shortcuts import redirect, render
from gestao.log import log
from registro.camera import VideoCamera
from registro.forms import ColetasFacesForm, FuncionarioForm
from registro.models import ColetaFace, Funcionario

camera_detection = VideoCamera()

logger = log(__name__)

def detected_face_generator(camera_detection):
    while True:
        frame = camera_detection.get_camera()
        if frame is None:
            continue
        
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def face_detection(request):
    return StreamingHttpResponse(detected_face_generator(camera_detection), content_type='multipart/x-mixed-replace; boundary=frame')

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
    logger.info(funcionario_id)
    funcionario = Funcionario.objects.get(id=funcionario_id)

    context = {
        'funcionario': funcionario,
        'face_detection': face_detection,
    }
    
    return render(request, 'criar_coleta_faces.html', context)
    