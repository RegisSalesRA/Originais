from django.contrib import admin

# Register your models here.
from cadastro.models import Cadastro


@admin.register(Cadastro)
class AdminCadastro(admin.ModelAdmin):
    fields = ['nome','sobrenome','idade','email','instagram','visitante']