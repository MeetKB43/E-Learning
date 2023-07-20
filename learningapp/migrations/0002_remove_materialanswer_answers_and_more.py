# Generated by Django 4.2.2 on 2023-07-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialanswer',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='materialanswer',
            name='submission_date',
        ),
        migrations.AddField(
            model_name='materialanswer',
            name='grade',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='materialanswer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]