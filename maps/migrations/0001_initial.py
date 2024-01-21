# Generated by Django 2.2.1 on 2019-05-24 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AptMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complex_name', models.CharField(max_length=30)),
                ('complex_address', models.CharField(max_length=40)),
                ('complex_map', models.ImageField(upload_to='maps')),
            ],
            options={
                'ordering': ['complex_name'],
            },
        ),
    ]
