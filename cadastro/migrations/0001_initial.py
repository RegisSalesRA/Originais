# Generated by Django 3.1.1 on 2020-09-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('sobrenome', models.CharField(max_length=120)),
                ('idade', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('visitante', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Nao', 'Nao')], max_length=10, null=True)),
            ],
        ),
    ]