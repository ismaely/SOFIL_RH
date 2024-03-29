# Generated by Django 2.2.1 on 2019-12-09 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_help', '0016_estatistica_opcao'),
        ('secretaria', '0049_auto_20191209_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chaves_modulo_especialidade',
            name='especialidade',
        ),
        migrations.RemoveField(
            model_name='chaves_modulo_especialidade',
            name='modulo',
        ),
        migrations.AddField(
            model_name='chaves_modulo_curso',
            name='ano',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Ano'),
        ),
        migrations.AddField(
            model_name='chaves_modulo_curso',
            name='especialidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Especialidade'),
        ),
        migrations.AddField(
            model_name='chaves_modulo_curso',
            name='semestre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Semestre'),
        ),
        migrations.DeleteModel(
            name='Chaves_Modulo_AnoSemestre',
        ),
        migrations.DeleteModel(
            name='Chaves_Modulo_Especialidade',
        ),
    ]
