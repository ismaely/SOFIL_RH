# Generated by Django 2.2.1 on 2019-12-05 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0043_nota_final_monografia_especialidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudante_Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Estudante')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Cursos')),
                ('numero_estudante', models.CharField(blank=True, default='NULL', max_length=15, null=True)),
            ],
        ),
    ]
