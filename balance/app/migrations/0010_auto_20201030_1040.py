# Generated by Django 2.2 on 2020-10-30 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_opening_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='number',
        ),
        migrations.AddField(
            model_name='transaction',
            name='account_head',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
