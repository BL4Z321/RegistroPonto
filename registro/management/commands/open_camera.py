import cv2
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Abre a câmera e exibe o vídeo e, tempo real'

    def handle(self, *args, **kwargs):
        cap = cv2.VideoCapture(0) # Abre a câmera

        if not cap.isOpened: # verifica se está aberta
            self.stdout.write(self.style.ERROR('Erro ao abrir a câmera!'))
            return
        
        self.stdout.write(self.style.SUCCESS('Câmera aberta com sucesso. Pressione "q" para sair!'))

        while True:
            ret, frame = cap.read() # Ler a captura

            if not ret:
                self.stdout.write(self.style.ERROR('Erro ao capturar o frame!'))
                break

            cv2.imshow('Camera', frame) # Exibe a captura


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release() 
        cv2.destroyAllWindows()
        self.stdout.write(self.style.SUCCESS('Câmera fechada!'))