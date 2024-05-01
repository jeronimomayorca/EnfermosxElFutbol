# Generated by Django 5.0.3 on 2024-04-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bandera', models.ImageField(upload_to='')),
                ('nombre', models.CharField(max_length=20)),
                ('grupo', models.CharField(max_length=10)),
                ('puntos', models.IntegerField()),
                ('partidos_jugados', models.IntegerField()),
                ('partidos_ganados', models.IntegerField()),
                ('partidos_empatados', models.IntegerField()),
                ('partidos_perdidos', models.IntegerField()),
                ('fuerza', models.IntegerField()),
                ('resistencia', models.IntegerField()),
                ('velocidad', models.IntegerField()),
                ('precision', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
