# Generated by Django 2.1.5 on 2020-04-05 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_deal_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deal',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelTable(
            name='deal',
            table='Deals',
        ),
        migrations.AlterModelTable(
            name='location',
            table='locations',
        ),
    ]
