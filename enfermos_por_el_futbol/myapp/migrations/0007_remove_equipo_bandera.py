# Generated by Django 5.0.4 on 2024-05-03 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_equipo_precision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='bandera',
        ),
    ]
