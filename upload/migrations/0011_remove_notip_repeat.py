# Generated by Django 2.2.1 on 2019-05-21 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0010_remove_notip_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notip',
            name='repeat',
        ),
    ]
