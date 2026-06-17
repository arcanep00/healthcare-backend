from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):

    GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
    )

    name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    phone = models.CharField(
        max_length=10
    )

    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="patient")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name