# Generated by Django 2.2.1 on 2019-06-26 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0009_docente_funcionario_monografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='grau_academico',
            field=models.CharField(blank=True, choices=[('-----', '-----'), ('Licenciado', 'Licenciado'), ('Pós-Graduação', 'Pós-Graduação'), ('Mestre', 'Mestre'), ('Doutor', 'Doutor'), ('Phd', 'Phd')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='docente',
            name='numero_docente',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='grau_academico',
            field=models.CharField(blank=True, choices=[('-----', '-----'), ('Licenciado', 'Licenciado'), ('Pós-Graduação', 'Pós-Graduação'), ('Mestre', 'Mestre'), ('Doutor', 'Doutor'), ('Phd', 'Phd')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Pessoa'),
        ),
    ]
