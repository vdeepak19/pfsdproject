# Generated by Django 5.0 on 2024-01-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourpackages', '0004_rentcar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcar',
            name='location',
            field=models.TextField(max_length=255),
        ),
    ]
