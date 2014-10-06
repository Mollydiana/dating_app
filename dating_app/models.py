from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Dater(AbstractUser):
    name = models.CharField(max_length=50, help_text="name", null=False)
    age = models.IntegerField(max_length=3, help_text="age", blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    paid = models.BooleanField(default=False)


class Location(models.Model):
    dater = models.ForeignKey(Dater, related_name='locations')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)