from django.contrib import admin
from registro.models import ColetaFace, Treinamento, Funcionario

# Register your models here.

class ColetasFacesInline(admin.StackedInline):
    model = ColetaFace
    extra = 0

class FuncionarioAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    inlines = (ColetasFacesInline,)

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Treinamento)