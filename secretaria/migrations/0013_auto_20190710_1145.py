# Generated by Django 2.2.1 on 2019-07-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0012_auto_20190710_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='tema',
            field=models.CharField(default='--', max_length=190),
        ),
    ]
