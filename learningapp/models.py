from django.db import models
from django.contrib.auth.models import AbstractUser, User
from datetime import timedelta
import datetime
import json

from django.db.models import JSONField



class Users(User):
    MEMBERSHIP_CHOICE = [
        ('F', 'Free'),
        ('S', 'Silver'),
        ('G', 'Gold'),
        ('P', 'Premium')]

    USER_TYPE = (
        ('0', 'Student'),
        ('1', 'Professor')
    )

    user_type = models.CharField(max_length=255, choices=USER_TYPE, null=True, default='0')
    memberShip = models.CharField(max_length=255, choices=MEMBERSHIP_CHOICE, default='F')

    def __str__(self):
        return self.username


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    #enrolled_student = models.OneToOneField(Users, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='courses_tutored')
    students = models.ManyToManyField(Users, related_name='enrolled_courses')  # adding when student when register
    createdAt = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name


class Material(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    document = models.FileField(upload_to='static/course_materials/documents', null=True)

    # assignment = models.FileField(upload_to='course_materials/assignments')
    # end_date = models.DateField()
    # aaignment_grade = models.IntegerField()

    def __str__(self):
        return self.name


class Assignment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)
    document = models.FileField(upload_to='static/course_materials/documents', null=True)
    due_date = models.DateField(null=True)
    due_time = models.TimeField(null=True)
    grade = models.PositiveIntegerField(default=0)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AssignmentAnswer(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    document = models.FileField(upload_to='static/course_materials/documents')
    submission_date = models.DateTimeField(auto_now_add=True)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.assignment.name




class Result(models.Model):
    TYPE = [
        ('quiz', 'Quiz'),
        ('assignment', 'Assignment')
    ]
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    related_id = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE, default='assignment')
    grade = models.PositiveIntegerField(default=0)
    total_grade = models.PositiveIntegerField(default=0)

class Subscription(models.Model):
    SUBSCRIPTION_CHOICES = [
        ('none', 'None'),
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    ]
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='subscription')
    subscription_type = models.CharField(max_length=20, choices=SUBSCRIPTION_CHOICES)


class Grade(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    course_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)


class StudentCourses(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)




