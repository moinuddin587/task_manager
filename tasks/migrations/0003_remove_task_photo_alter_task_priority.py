# Generated by Django 5.0 on 2023-12-14 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_alter_task_priority"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="photo",
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[("H", "high"), ("M", "Medium"), ("S", "Low")], max_length=1
            ),
        ),
    ]
