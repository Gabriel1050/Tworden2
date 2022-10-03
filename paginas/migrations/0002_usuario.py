# Generated by Django 4.1 on 2022-09-23 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cargo', models.CharField(choices=[('Cocinero', 'Cocinero'), ('Mesero', 'Mesero')], max_length=10)),
                ('Rol', models.CharField(choices=[('Cocina1', 'Cocina1'), ('Cocina2', 'Cocina2'), ('Cocina3', 'Cocina3'), ('Bebidas1', 'Bebidas1'), ('Bebidas2', 'Bebidas2')], max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
