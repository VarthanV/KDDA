# Generated by Django 2.2 on 2020-09-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200925_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='bankname',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='dateinbank',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='bankname',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='dateinbank',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]