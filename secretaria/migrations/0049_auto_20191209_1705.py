# Generated by Django 2.2.1 on 2019-12-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0048_chaves_modulo_anosemestre_chaves_modulo_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo_disciplina',
            name='credito',
            field=models.CharField(blank=True, default='', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='modulo_disciplina',
            name='sigla_codigo',
            field=models.CharField(blank=True, default='', max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='profissao',
            name='ano_experiencia',
            field=models.CharField(blank=True, default='-----', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='profissao',
            name='area_profissional',
            field=models.CharField(blank=True, default='-----', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profissao',
            name='funcao',
            field=models.CharField(blank=True, default='-----', max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='profissao',
            name='instituicao',
            field=models.CharField(blank=True, default='-----', max_length=190, null=True),
        ),
    ]
