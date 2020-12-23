from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True, max_length=255, verbose_name="email")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Address = models.TextField()

    def __str__(self):
        return self.Name+str(self.id)