from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'profile__role': 'TEACHER'}
    )
    students = models.ManyToManyField(
        'students.Student',
        blank=True
    )

    def __str__(self):
        return f"{self.code} - {self.name}"
