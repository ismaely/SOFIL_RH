# Generated by Django 2.2.1 on 2019-08-22 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_help', '0015_descricao_nota'),
        ('secretaria', '0031_remove_nota_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='descricao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core_help.Descricao_Nota'),
            preserve_default=False,
        ),
    ]