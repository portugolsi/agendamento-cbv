# Generated by Django 5.0.5 on 2024-05-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='desc',
            field=models.CharField(default='Não Agendado', max_length=30),
        ),
    ]
