# Generated by Django 5.0.1 on 2024-01-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristreview',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
