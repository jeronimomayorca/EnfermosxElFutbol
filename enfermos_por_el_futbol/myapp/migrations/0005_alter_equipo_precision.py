# Generated by Django 5.0.4 on 2024-05-01 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_equipo_fuerza_alter_equipo_partidos_empatados_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='precision',
            field=models.CharField(default='Media', max_length=10),
        ),
    ]
