# Generated by Django 4.2.16 on 2024-10-31 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.CharField(max_length=150, verbose_name='Descrição')),
                ('ingredients', models.TextField(verbose_name='Ingredientes')),
                ('directions', models.TextField(verbose_name='Modo de preparo')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Chef')),
            ],
        ),
    ]