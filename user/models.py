from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.firstname