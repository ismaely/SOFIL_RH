# Generated by Django 2.2.1 on 2019-12-08 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0046_chaves_modulo_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modulo_disciplina',
            old_name='Horas',
            new_name='horas',
        ),
        migrations.RemoveField(
            model_name='modulo_disciplina',
            name='ano',
        ),
        migrations.RemoveField(
            model_name='modulo_disciplina',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='modulo_disciplina',
            name='especialidade',
        ),
        migrations.RemoveField(
            model_name='modulo_disciplina',
            name='semestre',
        ),
    ]