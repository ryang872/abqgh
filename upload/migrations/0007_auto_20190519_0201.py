# Generated by Django 2.2.1 on 2019-05-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_notip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notip',
            name='address',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
