# Generated by Django 2.2.1 on 2019-05-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_auto_20190519_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notip',
            name='address',
            field=models.CharField(blank=True, default='TEST', max_length=30, null=True),
        ),
    ]
