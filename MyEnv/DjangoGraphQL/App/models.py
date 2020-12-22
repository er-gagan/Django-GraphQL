from django.db import models

# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Address = models.TextField()

    def __str__(self):
        return self.Name+str(self.id)