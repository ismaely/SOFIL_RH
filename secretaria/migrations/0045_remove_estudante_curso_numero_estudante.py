# Generated by Django 2.2.1 on 2019-12-06 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0044_estudante_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudante_curso',
            name='numero_estudante',
        ),
    ]
