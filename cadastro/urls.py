from django.urls import path
from cadastro.views import CadastroCreateView, SuccessPost

urlpatterns = [
# HTML
path('', CadastroCreateView.as_view(), name='cadastroView'),
path('successForm/', SuccessPost, name='successView'),
# EndHtml
    ]