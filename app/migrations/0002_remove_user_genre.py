# Generated by Django 2.2.5 on 2019-09-09 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='genre',
        ),
    ]