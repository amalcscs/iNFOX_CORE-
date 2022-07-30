# Generated by Django 4.0.3 on 2022-04-20 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acnt_monthdays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_fromdate', models.DateField(blank=True, null=True)),
                ('month_todate', models.DateField(blank=True, null=True)),
                ('month_workingdays', models.IntegerField()),
                ('month_holidays', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='acntexpensest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payee', models.CharField(max_length=100)),
                ('payacnt', models.CharField(max_length=200)),
                ('paymethod', models.CharField(max_length=100)),
                ('paydate', models.CharField(max_length=100)),
                ('refno', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('tax', models.IntegerField()),
                ('total', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='branch_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('branch_admin', models.CharField(max_length=100)),
                ('branch_type', models.CharField(max_length=100)),
                ('mobile', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('logo', models.FileField(blank=True, default='', null=True, upload_to='images/')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition1', models.CharField(max_length=1000)),
                ('condition2', models.CharField(max_length=1000)),
                ('condition3', models.CharField(max_length=1000)),
                ('condition4', models.CharField(max_length=1000)),
                ('condition5', models.CharField(max_length=1000)),
                ('condition6', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='create_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('trainer', models.CharField(default='', max_length=200)),
                ('progress', models.IntegerField()),
                ('status', models.CharField(max_length=200)),
                ('team_count', models.IntegerField(default=0)),
                ('team_status', models.CharField(default='0', max_length=200)),
                ('trainer_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departmentbranch', to='base_app.branch_registration')),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='designationbranch', to='base_app.branch_registration')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departmentbranch', to='base_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField(blank=True, null=True)),
                ('fullname', models.CharField(max_length=200)),
                ('collegename', models.CharField(max_length=200)),
                ('reg_no', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('stream', models.CharField(max_length=200)),
                ('platform', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('end_date', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('alternative_no', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('attach_file', models.FileField(blank=True, null=True, upload_to='images/')),
                ('rating', models.CharField(max_length=200)),
                ('hrmanager', models.CharField(max_length=200)),
                ('guide', models.CharField(max_length=200)),
                ('qr', models.CharField(default='', max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('complete_status', models.CharField(default='0', max_length=10)),
                ('verify_status', models.CharField(default='0', max_length=10)),
                ('total_fee', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('pay_date', models.DateField(blank=True, null=True)),
                ('balance', models.IntegerField(default=0)),
                ('total_pay', models.IntegerField(default=0)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internshipbranch', to='base_app.branch_registration')),
            ],
        ),
        migrations.CreateModel(
            name='internship_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('fee', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(blank=True, max_length=100, null=True)),
                ('rejectdate', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('progress', models.CharField(max_length=100)),
                ('user_reason', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='branch', to='base_app.branch_registration')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projectdepartment', to='base_app.department')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projectdesignation', to='base_app.designation')),
            ],
        ),
        migrations.CreateModel(
            name='project_taskassign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('task', models.CharField(blank=True, max_length=200, null=True)),
                ('subtask', models.CharField(blank=True, max_length=200, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('extension', models.IntegerField(blank=True, default='0', null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('extension_status', models.CharField(blank=True, max_length=200, null=True)),
                ('extension_date', models.DateField(blank=True, null=True)),
                ('tl_description', models.CharField(blank=True, max_length=200, null=True)),
                ('submitted_date', models.DateField(blank=True, null=True)),
                ('employee_files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('employee_description', models.TextField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('progress', models.IntegerField(default='0', null=True)),
                ('projectstatus', models.CharField(blank=True, default='In progress', max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('delay', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_designation', models.CharField(max_length=240, null=True)),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('fathername', models.CharField(max_length=240, null=True)),
                ('mothername', models.CharField(max_length=240, null=True)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=240, null=True)),
                ('presentaddress1', models.CharField(max_length=240, null=True)),
                ('presentaddress2', models.CharField(max_length=240, null=True)),
                ('presentaddress3', models.CharField(max_length=240, null=True)),
                ('pincode', models.CharField(max_length=240, null=True)),
                ('district', models.CharField(max_length=240, null=True)),
                ('state', models.CharField(max_length=240, null=True)),
                ('country', models.CharField(max_length=240, null=True)),
                ('permanentaddress1', models.CharField(max_length=240, null=True)),
                ('permanentaddress2', models.CharField(max_length=240, null=True)),
                ('permanentaddress3', models.CharField(max_length=240, null=True)),
                ('permanentpincode', models.CharField(max_length=240, null=True)),
                ('permanentdistrict', models.CharField(max_length=240, null=True)),
                ('permanentstate', models.CharField(max_length=240, null=True)),
                ('permanentcountry', models.CharField(max_length=240, null=True)),
                ('mobile', models.CharField(max_length=240, null=True)),
                ('alternativeno', models.CharField(max_length=240, null=True)),
                ('employee_id', models.CharField(default='', max_length=240, null=True)),
                ('email', models.EmailField(max_length=240, null=True)),
                ('password', models.CharField(max_length=240, null=True)),
                ('idproof', models.FileField(blank=True, null=True, upload_to='images/')),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/')),
                ('attitude', models.IntegerField(default='0')),
                ('creativity', models.IntegerField(default='0')),
                ('workperformance', models.IntegerField(default='0')),
                ('joiningdate', models.DateField(auto_now_add=True, null=True)),
                ('startdate', models.DateField(auto_now_add=True, null=True)),
                ('enddate', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(default='active', max_length=240, null=True)),
                ('tl_id', models.IntegerField(blank=True, default='0', null=True)),
                ('projectmanager_id', models.IntegerField(blank=True, default='0', null=True)),
                ('total_pay', models.IntegerField(default='0')),
                ('payment_balance', models.IntegerField(default='0')),
                ('account_no', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('ifsc', models.CharField(default='', max_length=200, null=True)),
                ('bank_name', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('bank_branch', models.CharField(default='', max_length=240, null=True)),
                ('payment_status', models.CharField(default='', max_length=200, null=True)),
                ('offerqr', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('relieveqr', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('expqr', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('hrmanager', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('confirm_salary', models.CharField(default='', max_length=100)),
                ('confirm_salary_status', models.CharField(default='0', max_length=10)),
                ('payment_file_downlod', models.FileField(blank=True, null=True, upload_to='images/')),
                ('total_amount', models.IntegerField(default='0')),
                ('payment_amount_date', models.DateField(blank=True, null=True)),
                ('salary_pending', models.CharField(default='', max_length=100)),
                ('salary_status', models.CharField(default='', max_length=10)),
                ('trainer_level', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('reg_status', models.CharField(default='0', max_length=10)),
                ('signature', models.FileField(blank=True, null=True, upload_to='images/')),
                ('branch', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userregistrationbranch', to='base_app.branch_registration')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_name', to='base_app.course')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userregistrationdepartment', to='base_app.department')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userregistrationdesignation', to='base_app.designation')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userregistrationteam', to='base_app.create_team')),
            ],
        ),
        migrations.CreateModel(
            name='trainer_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=240)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('submitteddate', models.DateField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(max_length=240)),
                ('user_description', models.TextField(max_length=240)),
                ('user_files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(max_length=200)),
                ('task_status', models.CharField(max_length=200)),
                ('team_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_name', to='base_app.create_team')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer_task_trainee', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=240)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField()),
                ('review', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('topic_status', models.CharField(max_length=200)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topicteam', to='base_app.create_team')),
                ('trainee', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topictrainee', to='base_app.user_registration')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topictrainer', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='tester_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('workdone', models.TextField(blank=True, max_length=200, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('progress', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tester_statusproject', to='base_app.project')),
                ('subtask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tester_statussubtask', to='base_app.project_taskassign')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tester_statustask', to='base_app.project_taskassign')),
                ('tester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tester_statustester', to='base_app.user_registration')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tester_statususer', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='test_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('workdone', models.TextField(null=True)),
                ('json', models.FileField(blank=True, null=True, upload_to='images/')),
                ('json_testerscreenshot', models.JSONField(blank=True, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_statusproject', to='base_app.project')),
                ('subtask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_statustaskname', to='base_app.project_taskassign')),
                ('taskname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_statustaskname', to='base_app.user_registration')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_statususer', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.CharField(max_length=240)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taskdepartment', to='base_app.department')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taskdesignation', to='base_app.designation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taskuser', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='reported_issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField()),
                ('reported_date', models.DateField(blank=True, null=True)),
                ('reply', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('issuestatus', models.CharField(max_length=200)),
                ('designation_id', models.CharField(max_length=200)),
                ('reported_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reported_issuereported_to', to='base_app.user_registration')),
                ('reporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reported_issuereporter', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plustwo', models.CharField(max_length=240, null=True)),
                ('schoolaggregate', models.CharField(max_length=240, null=True)),
                ('schoolcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('ugdegree', models.CharField(max_length=240, null=True)),
                ('ugstream', models.CharField(max_length=240, null=True)),
                ('ugpassoutyr', models.CharField(max_length=240, null=True)),
                ('ugaggregrate', models.CharField(max_length=240, null=True)),
                ('backlogs', models.CharField(max_length=240, null=True)),
                ('ugcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('pg', models.CharField(max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='qualificationuser', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='Promissory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inital_amount', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('inital_paid_on', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('inital_paid_amount', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('inital_paid_date', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('inital_balance_amount', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('inital_due_date', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('inital_total_payment', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('second_amount', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('second_due_on', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('second_paid_amount', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('second_paid_date', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('second_balance_amount', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('second_due_date', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('second_total_payment', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('final_amount', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('final_due_on', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('final_paid_amount', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('final_paid_date', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('final_balance_amount', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('final_due_date', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('final_total_payment', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('complete_status', models.CharField(blank=True, default='0', max_length=100, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='promissory_user', to='base_app.user_registration')),
            ],
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_taskassignuser', to='base_app.user_registration'),
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_taskassignproject', to='base_app.project'),
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='tester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_taskassign_tester', to='base_app.user_registration'),
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='tl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_taskassigntl', to='base_app.user_registration'),
        ),
        migrations.AddField(
            model_name='project',
            name='projectmanager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projectuser', to='base_app.user_registration'),
        ),
        migrations.AddField(
            model_name='project',
            name='tester',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projecttester', to='base_app.user_registration'),
        ),
        migrations.CreateModel(
            name='previousTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pstatus', models.CharField(max_length=200)),
                ('progress', models.IntegerField(default='0')),
                ('teamname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teamname', to='base_app.create_team')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user1', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='paymentlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_pay', models.IntegerField(default='0')),
                ('amount_date', models.DateField(blank=True, null=True)),
                ('current_date', models.DateField(blank=True, null=True)),
                ('amount_status', models.CharField(max_length=200, null=True)),
                ('amount_downlod', models.FileField(blank=True, null=True, upload_to='images/')),
                ('balance_amt', models.IntegerField(default='0')),
                ('course', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='total', to='base_app.course')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userpay', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('reason', models.TextField()),
                ('leave_status', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('designation_id', models.CharField(max_length=200)),
                ('leaveapprovedstatus', models.CharField(max_length=200)),
                ('leave_rejected_reason', models.CharField(max_length=300)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaveuser', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='internship_paydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('internship_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internship_user', to='base_app.internship')),
            ],
        ),
        migrations.AddField(
            model_name='internship',
            name='internshiptype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internship_type', to='base_app.internship_type'),
        ),
        migrations.CreateModel(
            name='extracurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internshipdetails', models.CharField(max_length=240, null=True)),
                ('internshipduration', models.CharField(max_length=240, null=True)),
                ('internshipcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('onlinetrainingdetails', models.CharField(max_length=240, null=True)),
                ('onlinetrainingduration', models.CharField(max_length=240, null=True)),
                ('onlinetrainingcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('projecttitle', models.CharField(max_length=240, null=True)),
                ('projectduration', models.CharField(max_length=240, null=True)),
                ('projectdescription', models.TextField(null=True)),
                ('projecturl', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill1', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill2', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill3', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=240)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extracurricularuser', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=200)),
                ('attendance_status', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendanceuser', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='acntspayslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.IntegerField(default='0')),
                ('eno', models.CharField(max_length=100)),
                ('hra', models.IntegerField(default='0')),
                ('conveyns', models.CharField(max_length=100)),
                ('tax', models.IntegerField(default='0')),
                ('incentives', models.IntegerField(default='0')),
                ('fromdate', models.DateField(blank=True, null=True)),
                ('todate', models.DateField(blank=True, null=True)),
                ('taxengine', models.CharField(max_length=100)),
                ('incometax', models.IntegerField(default='0')),
                ('uan', models.CharField(max_length=100)),
                ('pf', models.IntegerField(default='0')),
                ('esi', models.CharField(max_length=100)),
                ('pro', models.CharField(max_length=100)),
                ('leavesno', models.IntegerField(default='0')),
                ('pf_tax', models.IntegerField(default='0')),
                ('delay', models.IntegerField(default='0')),
                ('basictype', models.CharField(default='', max_length=255)),
                ('hratype', models.CharField(default='', max_length=255)),
                ('contype', models.CharField(default='', max_length=255)),
                ('protype', models.CharField(default='', max_length=255)),
                ('instype', models.CharField(default='', max_length=255)),
                ('deltype', models.CharField(default='', max_length=255)),
                ('leatype', models.CharField(default='', max_length=255)),
                ('pftype', models.CharField(default='', max_length=255)),
                ('esitype', models.CharField(default='', max_length=255)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dept', to='base_app.department')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='desic', to='base_app.designation')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='base_app.user_registration')),
            ],
        ),
    ]
