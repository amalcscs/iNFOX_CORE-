# Generated by Django 4.0.2 on 2022-08-11 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0038_project_taskassign_teamleader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_phase', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
