# Generated by Django 3.2.6 on 2024-10-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPatrimonio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=7)),
                ('descricao', models.TextField()),
                ('local', models.CharField(max_length=100)),
            ],
        ),
    ]
