# Generated by Django 2.2.1 on 2019-11-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_help', '0015_descricao_nota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estatistica_Opcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='------', max_length=100)),
            ],
        ),
    ]
