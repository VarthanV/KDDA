# Generated by Django 2.2 on 2020-09-24 12:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(blank=True, max_length=50, null=True)),
                ('desination', models.CharField(blank=True, max_length=50, null=True)),
                ('desginkdda', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expid', models.CharField(default=uuid.uuid4, max_length=10)),
                ('expname', models.CharField(blank=True, max_length=50, null=True)),
                ('expmode', models.CharField(choices=[('CASH', 'cash'), ('CHEQUE', 'cheque'), ('DEMAND DRAFT', 'demand draft')], max_length=15)),
                ('amount', models.IntegerField(default=0)),
                ('expreason', models.CharField(max_length=50)),
                ('expby', models.CharField(blank=True, max_length=50, null=True)),
                ('expdate', models.DateField()),
                ('detail', models.TextField()),
                ('bankname', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('chequeordd', models.IntegerField(default=0)),
                ('dateinbank', models.DateField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etypeid', models.IntegerField()),
                ('etypename', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incid', models.CharField(default=uuid.uuid4, max_length=10)),
                ('incname', models.CharField(blank=True, max_length=50, null=True)),
                ('incdate', models.DateField()),
                ('incmode', models.CharField(choices=[('CASH', 'cash'), ('CHEQUE', 'cheque'), ('DEMAND DRAFT', 'demand draft')], max_length=15)),
                ('incamt', models.IntegerField(default=0)),
                ('increason', models.CharField(max_length=50)),
                ('incby', models.CharField(max_length=50)),
                ('bankname', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('chequeordd', models.IntegerField(default=0)),
                ('dateinbank', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='IncomeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField()),
                ('typename', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
