# Generated by Django 3.1.1 on 2020-09-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20200917_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='instagram',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]