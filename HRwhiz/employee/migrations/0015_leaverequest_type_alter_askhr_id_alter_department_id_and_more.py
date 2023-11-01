# Generated by Django 4.2.6 on 2023-11-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_alter_askhr_options_alter_feedback_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='type',
            field=models.CharField(default='Casual', max_length=30),
        ),
        migrations.AlterField(
            model_name='askhr',
            name='id',
            field=models.CharField(default='f923af2d-2b98-49c3-977a-c33b243c6c3d', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='118c1c03-a3eb-4ff4-a481-238cc827ac63', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='25d02a3d-e159-4fe6-97cd-eaed46362c44', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.CharField(default='8239ad65-8716-411b-80aa-c087e9bfd50b', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default='b2f8a2a6-aae9-48cd-941f-306b38aa5c50', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]
