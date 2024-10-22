# Generated by Django 3.2.6 on 2024-09-19 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('numero_patrimonio', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='Apenas números com até 7 dígitos são permitidos.', regex='^\\d{1,7}$')])),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_aquisicao', models.DateField()),
                ('data_inclusao', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('novo', 'Novo'), ('usado', 'Usado'), ('danificado', 'Danificado')], max_length=10)),
                ('estado', models.CharField(choices=[('bom', 'Bom'), ('regular', 'Regular'), ('ruim', 'Ruim')], max_length=10)),
                ('categoria', models.CharField(choices=[('informatica', 'Informática'), ('mobilia', 'Mobília'), ('outros', 'Outros')], max_length=20)),
                ('origem', models.TextField()),
                ('observacao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
