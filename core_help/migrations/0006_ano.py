# Generated by Django 2.2.1 on 2019-06-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_help', '0005_remove_ano_semestre_semestre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
    ]
