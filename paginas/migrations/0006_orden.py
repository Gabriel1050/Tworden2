# Generated by Django 4.1 on 2022-09-26 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0005_delete_orden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('observacion', models.TextField(blank=True, null=True)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.mesas')),
                ('plato', models.ManyToManyField(blank=True, related_name='orden', to='paginas.menu')),
            ],
        ),
    ]
