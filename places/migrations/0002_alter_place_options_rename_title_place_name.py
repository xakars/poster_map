# Generated by Django 5.2.3 on 2025-07-03 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='place',
            old_name='title',
            new_name='name',
        ),
    ]
