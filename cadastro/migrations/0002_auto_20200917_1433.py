# Generated by Django 3.1.1 on 2020-09-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='visitante',
            field=models.CharField(blank=True, choices=[('Nao', 'Nao'), ('Sim', 'Sim')], max_length=10, null=True),
        ),
    ]