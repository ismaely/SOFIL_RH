# Generated by Django 2.2.1 on 2019-10-09 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0032_nota_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulo_disciplina',
            name='tipo',
        ),
    ]
