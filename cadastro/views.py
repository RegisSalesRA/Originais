from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from cadastro.models import Cadastro


class CadastroCreateView(CreateView):
    model = Cadastro
    template_name = 'form.html'
    fields = ['nome', 'sobrenome', 'idade', 'email','instagram','visitante']
    success_url = reverse_lazy('successView')


def SuccessPost(request):
    return render(request, 'success.html')
