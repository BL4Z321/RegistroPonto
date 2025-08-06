from django.contrib import admin
from registro.models import ColetaFace, Treinamento, Funcionário

# Register your models here.

class ColetasFacesInline(admin.StackedInline):
    model = ColetaFace
    extra = 0

class FuncionarioAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    inlines = (ColetasFacesInline,)

admin.site.register(Funcionário, FuncionarioAdmin)
admin.site.register(Treinamento)