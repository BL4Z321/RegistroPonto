from random import randint
from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify

# Create your models here.
class Funcionario(models.Model):
    # Slug -> é a parte amigável e legível que identifica uma página específica dentro de um site,
    # aparecendo após o nome de domínio na URL. 
    slug = models.SlugField(max_length=200, unique=True)
    foto = models.ImageField(upload_to='foto/')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
    def save(self,  *args, **kwargs):
        seq = self.nome + '_FUNC' + str(randint(1000000, 9999999))
        # Slugify -> Processo que converte uma string em um slug, que é uma string amigável para URLs, 
        # são normalmente utilizados em URls para torná-las mais legíveis e otimizadas para SEO (otimização de motores de pesquisa)
        self.slug = slugify(seq)
        super().save(*args, **kwargs)

class ColetaFace(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='funcionario_coletas')
    image = models.ImageField(upload_to='roi/')

class Treinamento(models.Model):
    modelo = models.FileField(upload_to='treinamento/')

    class Meta:
        verbose_name = 'Treinamento'
        verbose_name_plural = 'Treinamentos'

    def __str__(self):
        return 'Classificador (frontalface)'
    
    def clean(self): # Limita a um único arquivo
        model = self.__class__
        if model.objects.exclude(id=self.id).exists():
            raise ValidationError('só pode haver um arquivo salvo.')
        