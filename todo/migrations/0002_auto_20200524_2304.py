# Generated by Django 3.0.6 on 2020-05-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
