# Generated by Django 4.2.6 on 2023-10-27 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_department_employee_feedback_project_requests_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="fed_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="given_feedback",
                to="employee.employee",
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="fed_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recieved_feedback",
                to="employee.employee",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="did",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="employee.department"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="leader_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="employee.employee"
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="req_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="request_made",
                to="employee.employee",
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="req_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="request_recieved",
                to="employee.employee",
            ),
        ),
    ]
