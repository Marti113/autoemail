from django.db import models

# Create your models here.
class Mail(models.Model):
    name = models.TextField()
    email = models.EmailField()