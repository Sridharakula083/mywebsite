from django.db import models

# Create your models here.
class Website(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10)
    message = models.CharField(max_length=50)
