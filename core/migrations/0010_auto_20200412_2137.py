# Generated by Django 2.1.5 on 2020-04-12 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200405_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='category',
            field=models.ManyToManyField(related_name='deals', to='core.Category'),
        ),
    ]
