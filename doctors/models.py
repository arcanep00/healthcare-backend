from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    experience = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name