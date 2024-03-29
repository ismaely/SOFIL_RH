# Generated by Django 2.2.1 on 2019-07-17 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0022_auto_20190715_0634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Estudante')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Cursos')),
                ('especialidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, parent_link=True, to='core_help.Especialidade')),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Modulo_Disciplina')),
                ('nota', models.CharField(max_length=2)),
                ('data_entrada', models.DateField()),
                ('data_registo_automatico', models.DateField()),
            ],
        ),
    ]
