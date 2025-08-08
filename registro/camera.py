import cv2
import os
from gestao.log import log

logger = log(__name__)

class VideoCamera(object):
    # Inicia a camera e carrega o classificador
    def __init__(self):
        self.video =  cv2.VideoCapture(0) # Abertura da camera

        if not self.video.isOpened(): # Verifica se câmera está aberta
            logger.error('Erro ao acessar a câmera!')
    
    # Libera a camera ao destruir a classe
    def __del__(self):
        self.video.release() 

    # Reinicia a camera
    def restart(self):
        self.video.release()
        self.video = cv2.VideoCapture(0)
    
    # Realiza detecção e a captura faces, a conversão para a escala de cinza
    def get_camera(self):
        ret, frame = self.video.read()
        if not ret:
            logger.error("Erro ao capturar o frame!")
            return None
        
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()