from django.urls import path
from cadastro.views import CadastroCreateView, SuccessPost

urlpatterns = [
# HTML
path('createForm/', CadastroCreateView.as_view(), name='cadastroView'),
path('successForm/', SuccessPost, name='successView'),
# EndHtml
    ]