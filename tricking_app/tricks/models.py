from django.db import models

# Create your models here.

class Trick(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    canPerform = models.BooleanField(default=True)   


