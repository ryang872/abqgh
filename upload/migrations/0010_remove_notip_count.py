# Generated by Django 2.2.1 on 2019-05-21 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_auto_20190519_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notip',
            name='count',
        ),
    ]