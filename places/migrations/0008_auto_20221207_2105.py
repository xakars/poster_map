# Generated by Django 3.2.16 on 2022-12-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20221207_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(verbose_name='Долгота'),
        ),
    ]
