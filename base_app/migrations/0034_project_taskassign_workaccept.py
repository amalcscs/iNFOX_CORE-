# Generated by Django 4.0.2 on 2022-07-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0033_alter_user_registration_confirm_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_taskassign',
            name='workaccept',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
