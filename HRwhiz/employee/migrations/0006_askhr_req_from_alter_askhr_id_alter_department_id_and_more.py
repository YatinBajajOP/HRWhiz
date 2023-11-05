# Generated by Django 4.2.6 on 2023-11-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_leaverequest_req_from_alter_askhr_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='askhr',
            name='req_from',
            field=models.CharField(default='Shraddha Sharma', max_length=40),
        ),
        migrations.AlterField(
            model_name='askhr',
            name='id',
            field=models.CharField(default='0dbf4bbd-8d9e-48e7-8559-3bab19ee1296', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='6bd84c42-fc78-445b-a66c-62b321b1d4a7', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='638816af-37cd-4bb8-a60d-ab55cadf9822', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.CharField(default='8a314e2a-d86d-4bea-9669-41d46010116e', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='id',
            field=models.CharField(default='fdc0db14-d8bc-4053-abf4-365f52b8cd13', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default='1cfc3751-addf-4c42-9b1f-3e6752b8e6cb', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]
