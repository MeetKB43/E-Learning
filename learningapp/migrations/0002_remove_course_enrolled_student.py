# Generated by Django 4.2.2 on 2023-07-17 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learningapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='enrolled_student',
        ),
    ]
