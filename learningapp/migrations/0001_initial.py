# Generated by Django 4.2.2 on 2023-07-01 14:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('createdAt', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material_name', models.CharField(max_length=255)),
                ('material_disc', models.CharField(max_length=255)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('document', models.FileField(upload_to='course_materials/documents')),
                ('video', models.FileField(upload_to='course_materials/videos')),
                ('assignment', models.FileField(upload_to='course_materials/assignments')),
                ('end_date', models.DateField()),
                ('aaignment_grade', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='learningapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('quiz_start_date', models.DateTimeField()),
                ('quiz_due_date', models.DateTimeField()),
                ('marks', models.IntegerField(default=0)),
                ('course_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='learningapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('is_student', models.BooleanField(default=False)),
                ('subscription_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_type', models.CharField(choices=[('none', 'None'), ('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='learningapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('related_id', models.CharField(max_length=255)),
                ('assignment_grade', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learningapp.material')),
                ('quiz_grade', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learningapp.quiz')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learningapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='learningapp.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='learningapp.question')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answers', models.CharField(max_length=255)),
                ('submission_date', models.DateField()),
                ('material_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learningapp.material')),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learningapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('course_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningapp.material')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningapp.users')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='enrolled_student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learningapp.users'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='enrolled_courses', to='learningapp.users'),
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='learningapp.users'),
        ),
    ]
