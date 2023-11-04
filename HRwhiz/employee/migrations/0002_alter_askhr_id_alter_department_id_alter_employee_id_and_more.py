# Generated by Django 4.2.6 on 2023-11-04 20:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askhr',
            name='id',
            field=models.CharField(default='bb4fa69e-ae61-40f5-91c0-6423a32001fc', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='4401b8c1-40ac-40e2-b8f5-f52f091201b4', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='ccea65a3-80f3-47c8-ba1e-91b7a9c28f03', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.CharField(default='1de31683-04fb-4bbe-a199-b3d4fcd94520', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='id',
            field=models.CharField(default='7e1e9d3b-e2de-4b12-baac-092413cd484f', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default='4ea1064b-0321-4320-9db9-b208975c7b23', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]