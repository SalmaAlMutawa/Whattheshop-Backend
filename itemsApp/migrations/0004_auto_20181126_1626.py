# Generated by Django 2.1 on 2018-11-26 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itemsApp', '0003_auto_20181125_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
    ]