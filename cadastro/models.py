from django.db import models

# Create your models here.

class Cadastro(models.Model):

    yes_or_nor = {
        ('Sim','Sim'),
        ('Nao','Nao'),
    }

    nome = models.CharField(max_length=120)
    sobrenome = models.CharField(max_length=120)
    idade = models.IntegerField(default=0,blank=True,null=True)
    email = models.EmailField(max_length=120,blank=True,null=True)
    instagram = models.CharField(max_length=120,blank=True,null=True)
    visitante = models.CharField(max_length=10,blank=True,null=True,choices=yes_or_nor)

    def __str__(self):
        return self.nome