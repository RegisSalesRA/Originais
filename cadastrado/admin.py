from django.contrib import admin

# Register your models here.
from cadastrado.models import Cadastro


@admin.register(Cadastro)
class AdminCadastro(admin.ModelAdmin):
    fields = ['nome','sobrenome','idade','email','visitante']