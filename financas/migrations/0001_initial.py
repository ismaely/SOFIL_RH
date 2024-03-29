# Generated by Django 2.2.1 on 2019-08-01 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Estudante')),
                ('grau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Grau_academico')),
                ('valor', models.CharField(default='--', max_length=10)),
                ('data_pagamento', models.DateField()),
                ('data_sistema', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
