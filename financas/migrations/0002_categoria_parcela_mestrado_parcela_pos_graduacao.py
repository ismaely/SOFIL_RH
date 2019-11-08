# Generated by Django 2.2.1 on 2019-08-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('valor', models.CharField(blank=True, max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parcela_Mestrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.CharField(blank=True, max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parcela_Pos_Graduacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.CharField(blank=True, max_length=11, null=True)),
            ],
        ),
    ]