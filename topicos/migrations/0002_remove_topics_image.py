# Generated by Django 2.2.14 on 2020-11-02 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topicos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='image',
        ),
    ]
