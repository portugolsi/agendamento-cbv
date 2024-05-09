# Generated by Django 5.0.5 on 2024-05-07 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Laboratorios',
            },
        ),
        migrations.CreateModel(
            name='RecursosDidaticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Recursos didáticos',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor', models.CharField(choices=[('1ANO', '1 ANO'), ('2ANO', '2 ANO'), ('3ANO', '3 ANO'), ('4ANO', '4 ANO'), ('5ANO', '5 ANO'), ('6ANO', '6 ANO'), ('7ANO', '7 ANO'), ('8ANO', '8 ANO'), ('9ANO', '9 ANO'), ('1SERIE', '1 SÉRIE'), ('2SERIE', '2 SÉRIE'), ('3SERIE', '3 SÉRIE')], max_length=150)),
                ('disciplina', models.CharField(max_length=30)),
                ('serie', models.CharField(max_length=30)),
                ('data', models.DateField()),
                ('horario', models.CharField(choices=[('1HORMAN', '07:00 às 07:50'), ('2HORMAN', '07:50 às 08:40'), ('3HORMAN', '08:40 às 09:30'), ('4HORMAN', '10:00 às 10:50'), ('5HORMAN', '10:50 às 11:40'), ('6HORMAN', '11:40 às 12:30')], max_length=150)),
                ('proposta_da_aula', models.TextField()),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.laboratorio')),
                ('recursos_didaticos', models.ManyToManyField(to='app.recursosdidaticos')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.status')),
            ],
            options={
                'verbose_name_plural': 'Agendamentos',
            },
        ),
    ]