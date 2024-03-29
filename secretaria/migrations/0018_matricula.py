# Generated by Django 2.2.1 on 2019-07-14 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0017_auto_20190714_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Estudante')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Cursos')),
                ('especialidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, parent_link=True, to='core_help.Especialidade')),
                ('ano', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Ano')),
                ('semestre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Semestre')),
                ('cadeira_atraso_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Modulo_Disciplina')),
                ('cadeira_atraso_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='cadeira2_chave_modulo', to='secretaria.Modulo_Disciplina')),
                ('cadeira_atraso_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='chave_cadeira3_modulo', to='secretaria.Modulo_Disciplina')),
                ('cadeira_atraso_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='cadeira4_modulo_chave', to='secretaria.Modulo_Disciplina')),
                ('data_matricula', models.DateField()),
            ],
        ),
    ]
