# Generated by Django 2.2.1 on 2019-07-11 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_help', '0012_auto_20190710_0317'),
        ('secretaria', '0014_auto_20190710_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo_disciplina',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, parent_link=True, to='core_help.Cursos'),
        ),
    ]
