# Generated by Django 2.2.1 on 2019-05-16 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notip',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='sc'),
        ),
    ]
