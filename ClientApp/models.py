from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
