# Generated by Django 2.2 on 2020-10-11 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_opening'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opening',
            name='balance',
        ),
    ]
