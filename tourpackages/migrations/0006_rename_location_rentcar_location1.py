# Generated by Django 5.0 on 2024-01-08 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourpackages', '0005_alter_rentcar_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentcar',
            old_name='location',
            new_name='location1',
        ),
    ]
