# Generated by Django 3.2.16 on 2022-12-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.IntegerField(default=0, verbose_name='Позиция'),
            preserve_default=False,
        ),
    ]
